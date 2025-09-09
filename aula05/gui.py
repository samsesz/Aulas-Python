from tkinter import *

#criação d variavel
tela = Tk()

#titulo barra de tarefas
tela.title("Fatec Registro")
#configuração cor da tela
tela.configure(background= '#1e3743')
#configuração tamanho da tela
tela.geometry("700x600")

#tela pode aumentar e diminuir
tela.resizable(True, True)
#tamanho maximo da tela
tela.maxsize(width=800, height=700)
#tamanho minimo da tela
tela.minsize(width=500, height=300)

lbl_nome = Label(tela, text="Nome").place (x=10, y=10)
lbl_cpf = Label(tela, text="CPF").place (x=10, y=50)

#lbl_teste = Label(tela, text="TESTE").place (x=10, y=10)
#lbl_teste é o nome de identificação interno da label
#label é o tipo do componente
#tela a variavel que a label esta ligado
#text="" e o texto a ser exibido na tela
#place o posicionamento a tela

tela.mainloop()