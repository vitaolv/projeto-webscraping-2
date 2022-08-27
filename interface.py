import time
import tkinter
import tkinter.font
import tkinter.ttk
from turtle import back

import bs4
import requests
import tabulate

import main
import modelo


class view(main.windom_tk):
    def __init__(self):
        super().__init__()

        self.text_Out = None
        self.display = None
        self.values = []
        self.table = []

    def widget_table(self):
        self.text_Out = tkinter.Text(self, height=200, width=200, bg="grey90")
        self.display = tkinter.Button(
            self, text='CLICK HERE TO UPDATE', command=lambda: fun_called())
        self.display.configure(highlightbackground='gold', highlightthickness=0.5, borderwidth=0.5, relief="groove",
                               fg='black', bg='gold', font=('arial', 14))

        self.display.pack(side='bottom', fill='x')

        def fun_called():
            self.tex.forget()

            try:
                headers = {'User-Agent': 'Mozilla/5.0'}

                resposta = requests.get(
                    'https://br.investing.com/currencies/exchange-rates-table', headers=headers)
                soup = bs4.BeautifulSoup(resposta.text, 'html.parser')
                linhas = soup.find(id='leftColumn').find(
                    id='exchange_rates_1').find('tbody').find_all('tr')

                result = []
                values = []

                for linha in linhas:
                    valores = linha.find_all('td')

                    col1 = valores[1].text
                    col2 = valores[2].text
                    col3 = valores[3].text
                    col4 = valores[4].text
                    col5 = valores[5].text
                    col6 = valores[6].text
                    col7 = valores[7].text
                    col8 = valores[8].text

                    test = modelo.moedas(
                        col1, col2, col3, col4, col5, col6, col7, col8)

                    result.append(test)

                for element in result:
                    values.append(
                        [element.v1, element.v2, element.v3, element.v4, element.v5, element.v6, element.v7,
                         element.v8])

                codeID_y = ['BRL', 'USD', 'EUR',
                            'GBP', 'JPY', 'CHF', 'CAD', 'AUD']
                codeID_x = ['ID CODES', 'BRL', 'USD', 'EUR',
                            'GBP', 'JPY', 'CHF', 'CAD', 'AUD']

                self.table = tabulate.tabulate(values, headers=codeID_x, tablefmt="fancy_grid", showindex=codeID_y,
                                               stralign="center")

                # open
                self.text_Out.config(state='normal', foreground='black')
                self.text_Out.delete("1.0", tkinter.END)
                self.text_Out.insert(
                    'end', f'{self.table}\n UPDATED: {time.strftime("%d/%m/%Y - %H:%M:%S")}')
                self.text_Out.config(state='disabled', foreground='black')
                self.text_Out.pack(side='top', fill='x')
                # closed

            except requests.exceptions.RequestException as err:
                # open
                self.text_Out.config(state='normal', foreground='black')
                # Here delete the text after a new click
                self.text_Out.delete("1.0", tkinter.END)
                self.text_Out.insert('end', f'INFORMATION:\n\n{err}\n\n')
                self.text_Out.insert(
                    'end', f'UPDATED: {time.strftime("%d/%m/%Y - %H:%M:%S")}\n\n')
                self.text_Out.insert(
                    'end', '\nPlease try to update again...\n')
                self.text_Out.config(state='disabled', foreground='black')
                self.text_Out.pack(side='top', fill='x')
                # closed

            except AttributeError as e:
                # open
                self.text_Out.config(state='normal', foreground='black')
                # Here delete the text after a new click
                self.text_Out.delete("1.0", tkinter.END)
                self.text_Out.insert(
                    'end', f'INFORMATION:\n\nURL is invalid or incorrect.\n\n{e}\n\n')
                self.text_Out.insert(
                    'end', f'UPDATED: {time.strftime("%d/%m/%Y - %H:%M:%S")}\n\n')
                self.text_Out.insert(
                    'end', '\nClose the window and check the URL.\n')
                self.text_Out.config(state='disabled', foreground='black')
                self.text_Out.pack(side='top', fill='x')
                # closed
