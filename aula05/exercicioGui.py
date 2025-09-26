from tkinter import *

#config tela
tela = Tk()
tela.title("Cadastro de Cliente")
tela.configure(background= "#4a4e7d")
tela.geometry("700x600")
tela.resizable(True, True)
tela.maxsize(width=800, height=700)
tela.minsize(width=500, height=300)

lbl_cad = Label(tela, text="Cadastrados:", justify="left", anchor="w")
lbl_cad.place(x=20, y=260)

txt_nome = Entry(tela, width=20, borderwidth=5, fg="blue", bg="white")
txt_nome.pack()
txt_nome.insert(0, "Digite o seu nome: ")

txt_nome = Entry(tela, width=20, borderwidth=5, fg="blue", bg="white")
txt_nome.pack()
txt_nome.insert(0, "Digite o seu email: ")

txt_nome = Entry(tela, width=20, borderwidth=5, fg="blue", bg="white")
txt_nome.pack()
txt_nome.insert(0, "Digite o seu telefone: ")

txt_nome = Entry(tela, width=20, borderwidth=5, fg="blue", bg="white")
txt_nome.pack()
txt_nome.insert(0, "Digite o seu endereço: ")

def meu_click():
    lbl_hello = Label(tela, text="" + txt_nome.get())
    lbl_hello.pack()
btn_botao = Button(tela, text="Click", command=meu_click)
btn_botao.pack()


tela.mainloop();