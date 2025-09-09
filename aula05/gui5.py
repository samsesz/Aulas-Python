from tkinter import *
tela = Tk()

txt_nome = Entry(tela, width=20, borderwidth=5, fg="blue", bg="white")
txt_nome.pack()
txt_nome.insert(0, "Digite o seu nome ")

def meu_click():
    lbl_hello = Label(tela, text="Bem vindo " + txt_nome.get())
    lbl_hello.pack()
btn_botao = Button(tela, text="Click", command=meu_click)
btn_botao.pack()

tela.mainloop()