from tkinter import *


class Application():
    def __init__(self, master=None):

        # Criação do container
        self.widget1 = Frame(master)
        self.widget1.pack(side=RIGHT)

        # Criação de label dentro do container principal
        self.msg = Label(self.widget1, text='Primeiro widget')
        self.msg['font'] = ('Verdana', '10', 'italic', 'bold')
        self.msg.pack()

        # Botão de saída
        self.sair = Button(self.widget1)
        self.sair['text'] = 'Sair'
        self.sair['font'] = ('Calibri', '10')
        self.sair['width'] = 5
        self.sair.bind('<Button-1>', self.alter_text)
        self.sair.pack()

    def alter_text(self, event):
        if self.msg['text'] == 'Primeiro widget':
            self.msg['text'] = 'O botão recebeu um clique'
        else:
            self.msg['text'] = 'Primeiro widget'


root = Tk()
Application(root)
root.mainloop()
