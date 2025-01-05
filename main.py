from tkinter import *
from PIL import Image, ImageTk
from dados import pokemon  # Importa o dicionário "pokemon" do arquivo dados.py
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

############## cores ################
co0 = "#444466"  # preto-azulado
co1 = "#feffff"  # branco 
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"  # texto
co5 = "#ef5350"  # vermelho
co6 = "#d3d3d3"  # cinza claro
co7 = "#ffcc00"  # amarelo (detalhes da Pokédex)

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
janela = ttk.Window(themename="darkly")
janela.title("Pokédex")
janela.geometry("600x400")
janela.configure(bg=co5)

# ================== FRAME SUPERIOR (Título e Combobox) ==================
frame_top = ttk.Frame(janela, bootstyle=PRIMARY)
frame_top.pack(side=TOP, fill=X, pady=5)

titulo = ttk.Label(frame_top, text="Pokédex", font=("Arial", 20, "bold"), bootstyle=INVERSE)
titulo.pack()

# Combobox para escolher o Pokémon
pokedex_nomes = list(pokemon.keys())  # lista com as chaves do dicionário
selected_pokemon = StringVar()

combo = ttk.Combobox(frame_top, textvariable=selected_pokemon, values=pokedex_nomes, state="readonly", width=15)
combo.pack(pady=5)
combo.set("Pikachu")  # valor inicial

# ================== FRAME PRINCIPAL (onde mostra os detalhes) ==================
frame_info = ttk.Frame(janela, bootstyle=SECONDARY, padding=10)
frame_info.pack(fill=BOTH, expand=True, padx=10, pady=10)

# Nome do Pokémon
pok_nome = ttk.Label(frame_info, text="", font=("Fixedsys", 16), bootstyle=INVERSE)
pok_nome.pack(pady=5)

# Label para imagem
pok_imagem = ttk.Label(frame_info)
pok_imagem.pack()

# Tipo e ID
pok_tipo = ttk.Label(frame_info, text="", font=("Ivy", 10, "bold"), bootstyle=INVERSE)
pok_tipo.pack(pady=2)

pok_id = ttk.Label(frame_info, text="", font=("Ivy", 10, "bold"), bootstyle=INVERSE)
pok_id.pack(pady=2)

# ========== Frame de "Status" ==========
frame_status = ttk.Frame(frame_info, bootstyle=LIGHT, padding=10)
frame_status.pack(pady=5, fill=X)

lbl_status_titulo = ttk.Label(frame_status, text="Status", font=("Verdana", 12, "bold"), bootstyle=INVERSE)
lbl_status_titulo.pack(anchor=NW, padx=5, pady=5)

pok_hp = ttk.Label(frame_status, text="", font=("Verdana", 9), bootstyle=INVERSE)
pok_hp.pack(anchor=NW, padx=15)

pok_atack = ttk.Label(frame_status, text="", font=("Verdana", 9), bootstyle=INVERSE)
pok_atack.pack(anchor=NW, padx=15)

pok_defesa = ttk.Label(frame_status, text="", font=("Verdana", 9), bootstyle=INVERSE)
pok_defesa.pack(anchor=NW, padx=15)

pok_velocidade = ttk.Label(frame_status, text="", font=("Verdana", 9), bootstyle=INVERSE)
pok_velocidade.pack(anchor=NW, padx=15)

pok_total = ttk.Label(frame_status, text="", font=("Verdana", 9), bootstyle=INVERSE)
pok_total.pack(anchor=NW, padx=15)

# ========== Frame de "Habilidades" ==========
frame_hab = ttk.Frame(frame_info, bootstyle=LIGHT, padding=10)
frame_hab.pack(pady=5, fill=X)

lbl_hab_titulo = ttk.Label(frame_hab, text="Habilidades", font=("Verdana", 12, "bold"), bootstyle=INVERSE)
lbl_hab_titulo.pack(anchor=NW, padx=5, pady=5)

pok_hb_1 = ttk.Label(frame_hab, text="", font=("Verdana", 9), bootstyle=INVERSE)
pok_hb_1.pack(anchor=NW, padx=15)

pok_hb_2 = ttk.Label(frame_hab, text="", font=("Verdana", 9), bootstyle=INVERSE)
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
    frame_info.config(bootstyle=cor_fundo)
    pok_nome.config(bootstyle=cor_fundo)
    pok_imagem.config(bootstyle=cor_fundo)
    pok_tipo.config(bootstyle=cor_fundo)
    pok_id.config(bootstyle=cor_fundo)
    frame_status.config(bootstyle=cor_fundo)
    lbl_status_titulo.config(bootstyle=cor_fundo)
    pok_hp.config(bootstyle=cor_fundo)
    pok_atack.config(bootstyle=cor_fundo)
    pok_defesa.config(bootstyle=cor_fundo)
    pok_velocidade.config(bootstyle=cor_fundo)
    pok_total.config(bootstyle=cor_fundo)
    frame_hab.config(bootstyle=cor_fundo)
    lbl_hab_titulo.config(bootstyle=cor_fundo)
    pok_hb_1.config(bootstyle=cor_fundo)
    pok_hb_2.config(bootstyle=cor_fundo)

# Quando o usuário seleciona um Pokémon no Combobox
def on_select(event):
    escolhido = combo.get()
    trocar_pokemon(escolhido)

combo.bind("<<ComboboxSelected>>", on_select)

# Inicializa mostrando Pikachu
trocar_pokemon("Pikachu")

# Inicia o loop da janela
janela.mainloop()
