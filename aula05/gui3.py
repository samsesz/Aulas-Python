from tkinter import *

#criação d variavel
tela = Tk()

tela.title("Fatec Registro")
tela.geometry("700x600")
tela.resizable(True, True)
tela.maxsize(width=800, height=700)
tela.minsize(width=500, height=300)

lbl_nome = Label (tela, text="Nome", font="Arial 20 bold italic", fg="#FF8C00").place(x=10, y=10)
lbl_cpf = Label (tela, text="CPF", font="Time 15 italic", fg="#7CFC00").place(x=10, y=50)

tela.mainloop()