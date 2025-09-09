from tkinter import *

#criação d variavel
tela = Tk()

tela.title("Fatec Registro")

#Dimensoes da janela
largura = 800
altura = 300

#resolução do sistema(tela)
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

print(largura_screen, altura_screen)

tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
tela.mainloop()