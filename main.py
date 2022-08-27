import tkinter

import interface


class windom_tk(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.title('Exchange Rates Table (Currency)')
        self.geometry('655x340')

        self.label = tkinter.Label(self, text='EXCHANGE RATES TABLE')
        fonte_1 = tkinter.font.Font(size=16, family='Arial', weight='bold')
        self.label.configure(font=fonte_1, relief='ridge', borderwidth=6,
                             width=100, foreground='gold', background='grey1')
        self.label.pack(side='top')

        self.tex = tkinter.Label(
            self, text='Click the button below to start...')
        fonte_2 = tkinter.font.Font(size=16, family='Menlo')
        self.tex.configure(font=fonte_2, foreground='black')
        self.tex.pack()


if __name__ == '__main__':
    root = interface.view()
    root.widget_table()
    root.mainloop()
