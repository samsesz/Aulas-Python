from tkinter import *

#config tela
tela = Tk()
tela.title("Cadastro de Cliente")
tela.configure(background= "#464457")
tela.geometry("700x600")
tela.resizable(True, True)
tela.maxsize(width=800, height=700)
tela.minsize(width=500, height=300)

#def de cadastro
def cad():
    nome = txt_nome.get()
    idade = txt_idade.get()
    telefone = txt_telefone.get()
    parentesco = txt_parentesco.get()
    policia = var_policia.get()

#verificação da idade
    try:
        idade_num = int(idade)
        maiorDidade = "Maior de idade" if idade_num >= 18 else "Menor de idade"
    except ValueError:
        idade_num = idade
        maiorDidade = "Idade inválida"

#Verificação da passagem pela policia
    if policia == "Sim":
        status = "Tá sendo procurado!"
    else:
        status = "Não tem passagem"

        # Exibir no Text
    resultado["text"] += f"\n{nome} | {idade} anos | {telefone} | {parentesco} | {maiorDidade} |  {status}"

    # Limpar campos
    txt_nome.delete(0, END)
    txt_idade.delete(0, END)
    txt_telefone.delete(0, END)
    txt_parentesco.delete(0, END)


#estilo das label
label_font = ("Comic Sans MS", 12, "bold")
label_fg = "#44574F"

#nome
Label(tela, text="Nome:", font=label_font, fg="#FFFFFF", bg="#464457").place(x=10, y=20)
txt_nome = Entry(tela, width=20, borderwidth=5, fg="#919476", bg="#57444C", font=("Arial", 11))
txt_nome.place(x=150, y=20)

#idade
Label(tela, text="Idade:", font=label_font, fg="#FFFFFF", bg="#464457").place(x=10, y=60)
txt_idade = Entry(tela, width=25, borderwidth=2, fg="#919476", bg="#57444C", font=("Arial", 11))
txt_idade.place(x=150, y=60)

#telefone
Label(tela, text="Telefone:", font=label_font, fg="#FFFFFF", bg="#464457").place(x=10, y=100)
txt_telefone = Entry(tela, width=25, borderwidth=2, fg="#919476", bg="#57444C", font=("Arial", 11))
txt_telefone.place(x=150, y=100)

#parentesco
Label(tela, text="Parentesco:", font=label_font, fg="#FFFFFF", bg="#464457").place(x=10, y=140)
txt_parentesco = Entry(tela, width=25, borderwidth=2, fg="#919476", bg="#57444C", font=("Arial", 11))
txt_parentesco.place(x=150, y=140)

#polícia
Label(tela, text="Passagem pela polícia:", font=label_font, fg="#FFFFFF", bg="#464457").place(x=10, y=180)
var_policia = StringVar(value="Não") #definição padrão
#opções de escolha, ta meio bugado, tentei arrumar mas não consegui não
Radiobutton(tela, text="Sim", variable=var_policia, value="Sim", bg="#464457", fg="#FFFFFF").place(x=180, y=180)
Radiobutton(tela, text="Não", variable=var_policia, value="Não", bg="#464457", fg="#FFFFFF").place(x=250, y=180)

#botão de cadastrar
Button(tela, text="Cadastrar", command=cad, bg="#44574F", fg="white", font=("Comic Sans MS", 12, "bold")).place(x=150, y=220)

resultado = Label(tela, text="Familiares cadastrados:", justify="left", anchor="w", bg="#464457", fg="white")
resultado.place(x=20, y=260)

#dados fixos
#professor, não vou colocar os dados originais da minha familia, fiz de personagens ficticios que gosto, espero q entenda!!
resultado["text"] += "\nDexter Morgan | 38 anos | 13 99999-9999 | Irmão | Maior de idade | Não tem passagem "
resultado["text"] += "\nBrian Moser | 40 anos | 13 99888-8888 | Irmão | Maior de idade | Procurado!! "
resultado["text"] += "\nHannibal Lecter | 52 anos | 13 99777-7777 | Mãe | Maior de idade | Não tem passagem "
resultado["text"] += "\nWill Graham | 50 anos | 13 99666-6666 | Pai | Maior de idade | Procurado!!"


tela.mainloop()