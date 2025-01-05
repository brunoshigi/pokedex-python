from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from dados import pokemon  # Importa o dicionário "pokemon" do arquivo dados.py

############## cores ################
co0 = "#444466"  # preto-azulado
co1 = "#feffff"  # branco 
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"  # texto
co5 = "#ef5350"  # vermelho
co6 = "#d3d3d3"  # cinza claro

# Dicionário de cores de fundo para cada Pokémon
cores_fundo = {
    'Pikachu': "#ffff00",
    'Bulbasaur': "#40e0d0",
    'Charmander': "#ff7f50",
    'Eevee': "#e6daa6",
    'Mew': "#ff81c0",
    'Chikorita': "#90ee90",
    'Gengar': "#c79fef",
    'Squirtle': "#add8e6",
    'Jigglypuff': "#ffb6c1",
    'Snorlax': "#d3d3d3",
    'Dragonite': "#ff4500",
    'Lucario': "#6495ed",
    'Gyarados': "#4169e1"
}

# Criando a janela principal (com tamanho menor)
janela = Tk()
janela.title("Pokédex")
janela.geometry("600x400")
janela.configure(bg=co5)

# ================== FRAME SUPERIOR (Título e Combobox) ==================
frame_top = Frame(janela, bg=co5)
frame_top.pack(side=TOP, fill=X, pady=5)

titulo = Label(frame_top, text="Pokédex", font=("Arial", 20, "bold"), bg=co5, fg=co1)
titulo.pack()

# Combobox para escolher o Pokémon
pokedex_nomes = list(pokemon.keys())  # lista com as chaves do dicionário
selected_pokemon = StringVar()

combo = ttk.Combobox(frame_top, textvariable=selected_pokemon, values=pokedex_nomes, state="readonly", width=15)
combo.pack(pady=5)
combo.set("Pikachu")  # valor inicial

# ================== FRAME PRINCIPAL (onde mostra os detalhes) ==================
frame_info = Frame(janela, bg=co1)
frame_info.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Nome do Pokémon
pok_nome = Label(frame_info, text="", font=("Fixedsys", 16), bg=co1, fg=co0)
pok_nome.pack(pady=5)

# Label para imagem
pok_imagem = Label(frame_info, bg=co1)
pok_imagem.pack()

# Tipo e ID
pok_tipo = Label(frame_info, text="", font=("Ivy", 10, "bold"), bg=co1, fg=co0)
pok_tipo.pack(pady=2)

pok_id = Label(frame_info, text="", font=("Ivy", 10, "bold"), bg=co1, fg=co0)
pok_id.pack(pady=2)

# ========== Frame de "Status" ==========
frame_status = Frame(frame_info, bg=co6)
frame_status.pack(pady=5, fill=X)

lbl_status_titulo = Label(frame_status, text="Status", font=("Verdana", 12, "bold"), bg=co6, fg=co0)
lbl_status_titulo.pack(anchor=NW, padx=5, pady=5)

pok_hp = Label(frame_status, text="", font=("Verdana", 9), bg=co6, fg=co4)
pok_hp.pack(anchor=NW, padx=15)

pok_atack = Label(frame_status, text="", font=("Verdana", 9), bg=co6, fg=co4)
pok_atack.pack(anchor=NW, padx=15)

pok_defesa = Label(frame_status, text="", font=("Verdana", 9), bg=co6, fg=co4)
pok_defesa.pack(anchor=NW, padx=15)

pok_velocidade = Label(frame_status, text="", font=("Verdana", 9), bg=co6, fg=co4)
pok_velocidade.pack(anchor=NW, padx=15)

pok_total = Label(frame_status, text="", font=("Verdana", 9), bg=co6, fg=co4)
pok_total.pack(anchor=NW, padx=15)

# ========== Frame de "Habilidades" ==========
frame_hab = Frame(frame_info, bg=co6)
frame_hab.pack(pady=5, fill=X)

lbl_hab_titulo = Label(frame_hab, text="Habilidades", font=("Verdana", 12, "bold"), bg=co6, fg=co0)
lbl_hab_titulo.pack(anchor=NW, padx=5, pady=5)

pok_hb_1 = Label(frame_hab, text="", font=("Verdana", 9), bg=co6, fg=co4)
pok_hb_1.pack(anchor=NW, padx=15)

pok_hb_2 = Label(frame_hab, text="", font=("Verdana", 9), bg=co6, fg=co4)
pok_hb_2.pack(anchor=NW, padx=15)

# ================== FUNÇÃO PARA TROCAR O POKÉMON ==================
def trocar_pokemon(nome):
    # Dados do arquivo dados.py
    info = pokemon[nome]

    # Atualiza labels: nome, tipo, id
    pok_nome.config(text=nome)
    pok_tipo.config(text=info["tipo"][1])
    pok_id.config(text=info["tipo"][0])

    # Status
    pok_hp.config(text=info["status"][0])
    pok_atack.config(text=info["status"][1])
    pok_defesa.config(text=info["status"][2])
    pok_velocidade.config(text=info["status"][3])
    pok_total.config(text=info["status"][4])

    # Habilidades
    pok_hb_1.config(text=info["habilidades"][0])
    pok_hb_2.config(text=info["habilidades"][1])

    # Imagem do Pokémon
    img = Image.open(info["tipo"][2])
    img = img.resize((120, 120))  # Reduzir a imagem para caber melhor
    img = ImageTk.PhotoImage(img)
    pok_imagem.config(image=img)
    pok_imagem.image = img  # referência

    # Mudar a cor de fundo do "frame_info" para a cor do Pokémon
    cor_fundo = cores_fundo.get(nome, co1)
    frame_info.config(bg=cor_fundo)
    pok_nome.config(bg=cor_fundo)
    pok_imagem.config(bg=cor_fundo)
    pok_tipo.config(bg=cor_fundo)
    pok_id.config(bg=cor_fundo)

# Quando o usuário seleciona um Pokémon no Combobox
def on_select(event):
    escolhido = combo.get()
    trocar_pokemon(escolhido)

combo.bind("<<ComboboxSelected>>", on_select)

# Inicializa mostrando Pikachu
trocar_pokemon("Pikachu")

# Inicia o loop da janela
janela.mainloop()
