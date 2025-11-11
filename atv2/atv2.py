# app.py
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
from pymongo import MongoClient
import base64, io, os

# ------------------ Config MongoDB ------------------
client = MongoClient("mongodb://localhost:27017/")
db = client["fatec_app"]
usuarios_col = db["usuarios"]
pessoas_col = db["pessoas"]
veiculos_col = db["veiculos"]
lugares_col = db["lugares_turisticos"]

# cria usuário padrão se não existir
if not usuarios_col.find_one({"usuario": "admin"}):
    usuarios_col.insert_one({"usuario":"admin","senha":"123"})

# ------------------ Helpers de imagem ------------------
def carregar_imagem(nome_arquivo, tam=None):
    """Tenta abrir a imagem e retornar ImageTk.PhotoImage redimensionada.
       Se não existir, retorna None."""
    if not nome_arquivo:
        return None
    if not os.path.exists(nome_arquivo):
        return None
    try:
        img = Image.open(nome_arquivo)
        if tam:
            img = img.resize(tam, Image.ANTIALIAS)
        return ImageTk.PhotoImage(img)
    except Exception:
        return None

def img_para_base64(caminho):
    if not caminho or not os.path.exists(caminho):
        return None
    with open(caminho, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def base64_para_photo(base64_str, tam=(120,120)):
    if not base64_str:
        return None
    try:
        img = Image.open(io.BytesIO(base64.b64decode(base64_str)))
        img = img.resize(tam, Image.ANTIALIAS)
        return ImageTk.PhotoImage(img)
    except Exception:
        return None

# ------------------ Janela principal ------------------
root = tk.Tk()
root.title("Sistema - Fatec (Tkinter + MongoDB)")
root.geometry("900x600")
root.resizable(False, False)

# Carrega ícones padrão (podem faltar, ok)
ICONS = {
    "access": carregar_imagem("icon_access.png", (48,48)),
    "exit": carregar_imagem("icon_exit.png", (48,48)),
    "menu_person": carregar_imagem("icon_menu_person.png", (80,80)),
    "menu_vehicle": carregar_imagem("icon_menu_vehicle.png", (80,80)),
    "menu_place": carregar_imagem("icon_menu_place.png", (80,80)),
    "avatar_person": carregar_imagem("avatar_person.png", (140,140)),
    "vehicle_placeholder": carregar_imagem("vehicle_placeholder.png", (140,140)),
    "place_placeholder": carregar_imagem("place_placeholder.png", (140,140)),
    "btn_add": carregar_imagem("btn_add.png", (48,48)),
    "btn_edit": carregar_imagem("btn_edit.png", (48,48)),
    "btn_view": carregar_imagem("btn_view.png", (48,48)),
    "btn_delete": carregar_imagem("btn_delete.png", (48,48)),
    "btn_choose": carregar_imagem("btn_choose_image.png", (36,36)),
    "bg_menu": carregar_imagem("background_menu.png", (900,400)),
}

# ------------------ Função: limpar tela ------------------
def limpar_janela():
    for w in root.winfo_children():
        w.destroy()

# ------------------ TELA DE LOGIN ------------------
def abrir_login():
    limpar_janela()
    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=1, relheight=1)

    tk.Label(frame, text="Acesso ao Sistema", font=("Arial", 18), bg="white").place(x=40, y=30)

    tk.Label(frame, text="Usuário:", bg="white").place(x=40, y=100)
    usuario_entry = tk.Entry(frame, width=25)
    usuario_entry.place(x=120, y=100)

    tk.Label(frame, text="Senha:", bg="white").place(x=40, y=140)
    senha_entry = tk.Entry(frame, show="*", width=25)
    senha_entry.place(x=120, y=140)

    # ícone de usuário (opcional)
    if ICONS["avatar_person"]:
        lbl = tk.Label(frame, image=ICONS["avatar_person"], bg="white")
        lbl.image = ICONS["avatar_person"]
        lbl.place(x=520, y=80)

    def validar_login():
        u = usuario_entry.get()
        s = senha_entry.get()
        if usuarios_col.find_one({"usuario":u,"senha":s}):
            abrir_menu()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos.")

    # botões Acessar / Sair (com ícones se existirem)
    if ICONS["access"]:
        b_acc = tk.Button(frame, image=ICONS["access"], command=validar_login)
        b_acc.image = ICONS["access"]
        b_acc.place(x=420, y=180)
    else:
        tk.Button(frame, text="Acessar", command=validar_login).place(x=420,y=180)

    if ICONS["exit"]:
        b_sair = tk.Button(frame, image=ICONS["exit"], command=root.quit)
        b_sair.image = ICONS["exit"]
        b_sair.place(x=490, y=180)
    else:
        tk.Button(frame, text="Sair", command=root.quit).place(x=490,y=180)

# ------------------ MENU PRINCIPAL ------------------
def abrir_menu():
    limpar_janela()
    frame = tk.Frame(root)
    frame.place(relwidth=1, relheight=1)

    # se background disponível, usa
    if ICONS["bg_menu"]:
        bg_lbl = tk.Label(frame, image=ICONS["bg_menu"])
        bg_lbl.image = ICONS["bg_menu"]
        bg_lbl.place(x=0, y=0)

    tk.Label(frame, text="Menu Principal", font=("Arial", 22, "bold")).place(x=40, y=30)

    # botões grandes centrais (Pessoas, Veículos, Lugares)
    x0 = 120
    y0 = 120
    gapx = 260

    # Pessoas
    if ICONS["menu_person"]:
        btn_p = tk.Button(frame, image=ICONS["menu_person"], command=lambda: abrir_cadastro_pessoas())
        btn_p.image = ICONS["menu_person"]
        btn_p.place(x=x0, y=y0)
        tk.Button(frame, text="Pessoas", width=12, command=lambda: abrir_cadastro_pessoas()).place(x=x0, y=y0+110)
    else:
        tk.Button(frame, text="Pessoas", width=20, height=6, command=lambda: abrir_cadastro_pessoas()).place(x=x0, y=y0)

    # Veículos
    if ICONS["menu_vehicle"]:
        btn_v = tk.Button(frame, image=ICONS["menu_vehicle"], command=lambda: abrir_cadastro_veiculos())
        btn_v.image = ICONS["menu_vehicle"]
        btn_v.place(x=x0+gapx, y=y0)
        tk.Button(frame, text="Veículos", width=12, command=lambda: abrir_cadastro_veiculos()).place(x=x0+gapx, y=y0+110)
    else:
        tk.Button(frame, text="Veículos", width=20, height=6, command=lambda: abrir_cadastro_veiculos()).place(x=x0+gapx, y=y0)

    # Lugares Turísticos
    if ICONS["menu_place"]:
        btn_l = tk.Button(frame, image=ICONS["menu_place"], command=lambda: abrir_cadastro_lugares())
        btn_l.image = ICONS["menu_place"]
        btn_l.place(x=x0+2*gapx, y=y0)
        tk.Button(frame, text="Lugares", width=12, command=lambda: abrir_cadastro_lugares()).place(x=x0+2*gapx, y=y0+110)
    else:
        tk.Button(frame, text="Lugares Turísticos", width=20, height=6, command=lambda: abrir_cadastro_lugares()).place(x=x0+2*gapx, y=y0)

    # botão sair
    if ICONS["exit"]:
        b_s = tk.Button(frame, image=ICONS["exit"], command=abrir_login)
        b_s.image = ICONS["exit"]
        b_s.place(x=800, y=20)
    else:
        tk.Button(frame, text="Sair", command=abrir_login).place(x=800,y=20)

# ------------------ TELA PADRÃO DE CADASTRO (helper) ------------------
def criar_tela_cadastro(titulo, campos, colecao, bg_color, left_image_name):
    """Gera tela de CRUD com layout parecido às imagens; retorna nada."""
    limpar_janela()
    frame = tk.Frame(root, bg=bg_color)
    frame.place(relwidth=1, relheight=1)

    tk.Label(frame, text=titulo, font=("Arial", 16, "bold"), bg=bg_color).place(x=20, y=12)

    # imagem à esquerda (avatar/placeholder)
    left_img = carregar_imagem(left_image_name, (140,140))
    img_lbl = tk.Label(frame, bg=bg_color)
    if left_img:
        img_lbl.config(image=left_img)
        img_lbl.image = left_img
    else:
        img_lbl.config(text="[Imagem]", width=18, height=9, bg=bg_color)
    img_lbl.place(x=20, y=60)

    # campos (arranjo semelhante à imagem)
    entries = {}
    x_label = 200
    x_entry = 280
    y = 60
    for i, campo in enumerate(campos):
        tk.Label(frame, text=campo + ":", bg=bg_color).place(x=x_label, y=y + i*35)
        e = tk.Entry(frame, width=30)
        e.place(x=x_entry, y=y + i*35)
        entries[campo] = e

    # área de descrição maior se houver campo 'Descrição'
    if "Descrição" in campos:
        desc = tk.Text(frame, width=38, height=4)
        desc.place(x=x_entry, y=y + (len(campos))*35)
        # substituir entry por text
        entries["Descrição"] = desc

    # variável para caminho imagem escolhida
    img_path = [None]

    def escolher_imagem_local():
        caminho = filedialog.askopenfilename(filetypes=[("Imagens", "*.png;*.jpg;*.jpeg")])
        if caminho:
            img_path[0] = caminho
            photo = Image.open(caminho).resize((140,140))
            photo = ImageTk.PhotoImage(photo)
            img_lbl.config(image=photo, text="")
            img_lbl.image = photo

    # CRUD functions
    def inserir():
        doc = {}
        for c in campos:
            if c == "Descrição":
                doc[c] = entries[c].get("1.0", "end").strip()
            else:
                doc[c] = entries[c].get().strip()
        if not doc.get(campos[0]):
            messagebox.showwarning("Aviso", f"Preencha o campo {campos[0]}")
            return
        doc["imagem"] = img_para_base64(img_path[0])
        colecao.insert_one(doc)
        messagebox.showinfo("Sucesso", "Registro inserido.")
        listar()

    def alterar():
        chave = entries[campos[0]].get().strip()
        if not chave:
            messagebox.showwarning("Aviso", "Informe o código para alterar.")
            return
        novo = {}
        for c in campos:
            if c == "Descrição":
                novo[c] = entries[c].get("1.0", "end").strip()
            else:
                novo[c] = entries[c].get().strip()
        if img_path[0]:
            novo["imagem"] = img_para_base64(img_path[0])
        colecao.update_one({campos[0]: chave}, {"$set": novo})
        messagebox.showinfo("Sucesso", "Registro alterado.")
        listar()

    def excluir():
        chave = entries[campos[0]].get().strip()
        if not chave:
            messagebox.showwarning("Aviso", "Informe o código para excluir.")
            return
        colecao.delete_one({campos[0]: chave})
        messagebox.showinfo("Sucesso", "Registro excluído.")
        listar()

    def consultar():
        chave = entries[campos[0]].get().strip()
        if not chave:
            messagebox.showwarning("Aviso", "Informe o código para consultar.")
            return
        doc = colecao.find_one({campos[0]: chave})
        if not doc:
            messagebox.showinfo("Resultado", "Registro não encontrado.")
            return
        # preenche campos
        for c in campos:
            if c == "Descrição":
                entries[c].delete("1.0", "end")
                entries[c].insert("1.0", doc.get(c, ""))
            else:
                entries[c].delete(0, "end")
                entries[c].insert(0, doc.get(c, ""))
        # imagem
        foto = base64_para_photo(doc.get("imagem"))
        if foto:
            img_lbl.config(image=foto, text="")
            img_lbl.image = foto
        listar()

    # treeview para listar registros
    cols = campos
    tree = ttk.Treeview(frame, columns=cols, show="headings", height=8)
    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, width=120)
    tree.place(x=200, y=300)

    def listar():
        for it in tree.get_children():
            tree.delete(it)
        for d in colecao.find():
            vals = [d.get(c, "") for c in cols]
            tree.insert("", "end", values=vals)

    # botões grandes com ícones similares à imagem
    bx = 200
    by = 200
    spacing = 80

    # Escolher imagem
    if ICONS["btn_choose"]:
        b_choose = tk.Button(frame, image=ICONS["btn_choose"], command=escolher_imagem_local)
        b_choose.image = ICONS["btn_choose"]
        b_choose.place(x=50, y=220)
    else:
        tk.Button(frame, text="Escolher Imagem", command=escolher_imagem_local).place(x=40, y=220)

    # Inserir
    if ICONS["btn_add"]:
        b_add = tk.Button(frame, image=ICONS["btn_add"], command=inserir)
        b_add.image = ICONS["btn_add"]
        b_add.place(x=bx, y=by)
    else:
        tk.Button(frame, text="Incluir", width=10, command=inserir).place(x=bx,y=by)

    # Alterar
    if ICONS["btn_edit"]:
        b_edit = tk.Button(frame, image=ICONS["btn_edit"], command=alterar)
        b_edit.image = ICONS["btn_edit"]
        b_edit.place(x=bx+spacing, y=by)
    else:
        tk.Button(frame, text="Alterar", width=10, command=alterar).place(x=bx+spacing,y=by)

    # Consultar
    if ICONS["btn_view"]:
        b_view = tk.Button(frame, image=ICONS["btn_view"], command=consultar)
        b_view.image = ICONS["btn_view"]
        b_view.place(x=bx+2*spacing, y=by)
    else:
        tk.Button(frame, text="Consultar", width=10, command=consultar).place(x=bx+2*spacing,y=by)

    # Excluir
    if ICONS["btn_delete"]:
        b_del = tk.Button(frame, image=ICONS["btn_delete"], command=excluir)
        b_del.image = ICONS["btn_delete"]
        b_del.place(x=bx+3*spacing, y=by)
    else:
        tk.Button(frame, text="Excluir", width=10, command=excluir).place(x=bx+3*spacing,y=by)

    # Botão voltar
    if ICONS["exit"]:
        b_back = tk.Button(frame, image=ICONS["exit"], command=abrir_menu)
        b_back.image = ICONS["exit"]
        b_back.place(x=800, y=20)
    else:
        tk.Button(frame, text="Voltar", command=abrir_menu).place(x=800,y=20)

    # preencher a listagem inicial
    listar()

# ------------------ Telas específicas ------------------
def abrir_cadastro_pessoas():
    campos = ["Código", "Nome", "Altura", "Peso", "Idade", "Data Cadastro", "Sexo"]
    criar_tela_cadastro("Cadastro de Pessoas", campos, pessoas_col, bg_color="#d0d0d0", left_image_name="avatar_person.png")

def abrir_cadastro_veiculos():
    campos = ["Código", "Marca", "Modelo", "Ano", "Cor", "Placa", "Proprietário"]
    criar_tela_cadastro("Cadastro de Veículos", campos, veiculos_col, bg_color="#410202", left_image_name="vehicle_placeholder.png")

def abrir_cadastro_lugares():
    campos = ["Código", "Nome", "Cidade", "País", "Descrição"]
    criar_tela_cadastro("Cadastro de Lugares Turísticos", campos, lugares_col, bg_color="#2d5336", left_image_name="place_placeholder.png")

# inicia no login
abrir_login()
root.mainloop()
