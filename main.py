from tkinter import *
from PIL import Image, ImageTk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Importa os dados
from dados import pokemon

class PokedexApp:
    def __init__(self, root):
        self.root = root
        self.config_window()
        self.create_widgets()
        self.trocar_pokemon("Pikachu")

    def config_window(self):
        self.root.title("Pokédex")
        self.root.geometry("600x400")

        # Cores
        self.co0 = "#444466"  # preto-azulado
        self.co1 = "#feffff"  # branco
        self.co2 = "#6f9fbd"  # azul
        self.co3 = "#38576b"  # valor
        self.co4 = "#403d3d"  # texto
        self.co5 = "#ef5350"  # vermelho
        self.co6 = "#d3d3d3"  # cinza claro
        self.co7 = "#ffcc00"  # amarelo (detalhes da Pokédex)

        self.root.configure(bg=self.co5)

        self.cores_fundo = {
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

    def create_widgets(self):
        # Frame Superior
        frame_top = ttk.Frame(self.root, bootstyle=PRIMARY)
        frame_top.pack(side=TOP, fill=X, pady=5)

        titulo = ttk.Label(frame_top, text="Pokédex", font=("Arial", 20, "bold"), bootstyle=INVERSE)
        titulo.pack()

        # Combobox
        pokedex_nomes = list(pokemon.keys())
        self.selected_pokemon = StringVar()
        self.combo = ttk.Combobox(frame_top, textvariable=self.selected_pokemon, values=pokedex_nomes, state="readonly", width=15)
        self.combo.pack(pady=5)
        self.combo.set("Pikachu")
        self.combo.bind("<<ComboboxSelected>>", self.on_select)

        # Frame Principal
        self.frame_info = ttk.Frame(self.root, bootstyle=SECONDARY, padding=10)
        self.frame_info.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Nome
        self.pok_nome = ttk.Label(self.frame_info, text="", font=("Fixedsys", 16), bootstyle=INVERSE)
        self.pok_nome.pack(pady=5)

        # Imagem
        self.pok_imagem = ttk.Label(self.frame_info)
        self.pok_imagem.pack()

        # Tipo e ID
        self.pok_tipo = ttk.Label(self.frame_info, text="", font=("Ivy", 10, "bold"), bootstyle=INVERSE)
        self.pok_tipo.pack(pady=2)

        self.pok_id = ttk.Label(self.frame_info, text="", font=("Ivy", 10, "bold"), bootstyle=INVERSE)
        self.pok_id.pack(pady=2)

        # Frame Status
        self.frame_status = ttk.Frame(self.frame_info, bootstyle=LIGHT, padding=10)
        self.frame_status.pack(pady=5, fill=X)

        self.lbl_status_titulo = ttk.Label(self.frame_status, text="Status", font=("Verdana", 12, "bold"), bootstyle=INVERSE)
        self.lbl_status_titulo.pack(anchor=NW, padx=5, pady=5)

        self.status_labels = []
        for _ in range(5):
            lbl = ttk.Label(self.frame_status, text="", font=("Verdana", 9), bootstyle=INVERSE)
            lbl.pack(anchor=NW, padx=15)
            self.status_labels.append(lbl)

        # Frame Habilidades
        self.frame_hab = ttk.Frame(self.frame_info, bootstyle=LIGHT, padding=10)
        self.frame_hab.pack(pady=5, fill=X)

        self.lbl_hab_titulo = ttk.Label(self.frame_hab, text="Habilidades", font=("Verdana", 12, "bold"), bootstyle=INVERSE)
        self.lbl_hab_titulo.pack(anchor=NW, padx=5, pady=5)

        self.hab_labels = []
        for _ in range(2):
            lbl = ttk.Label(self.frame_hab, text="", font=("Verdana", 9), bootstyle=INVERSE)
            lbl.pack(anchor=NW, padx=15)
            self.hab_labels.append(lbl)

    def trocar_pokemon(self, nome):
        if nome not in pokemon:
            return

        info = pokemon[nome]

        # Atualiza labels
        self.pok_nome.config(text=nome)
        self.pok_tipo.config(text=info["tipo"][1])
        self.pok_id.config(text=info["tipo"][0])

        # Status
        for i, lbl in enumerate(self.status_labels):
            lbl.config(text=info["status"][i])

        # Habilidades
        for i, lbl in enumerate(self.hab_labels):
            if i < len(info["habilidades"]):
                lbl.config(text=info["habilidades"][i])
            else:
                lbl.config(text="")

        # Imagem
        image_path = info["tipo"][2]
        try:
            img = Image.open(image_path)
            img = img.resize((120, 120))
            img = ImageTk.PhotoImage(img)
            self.pok_imagem.config(image=img)
            self.pok_imagem.image = img
        except Exception as e:
            print(f"Erro ao carregar imagem: {e}")
            self.pok_imagem.config(image='', text="Imagem não encontrada")


        # Cores
        cor_fundo = self.cores_fundo.get(nome, self.co1)
        self.update_colors(cor_fundo)

    def update_colors(self, cor):
        self.frame_info.config(bootstyle=cor)
        self.pok_nome.config(bootstyle=cor)
        self.pok_imagem.config(bootstyle=cor)
        self.pok_tipo.config(bootstyle=cor)
        self.pok_id.config(bootstyle=cor)
        self.frame_status.config(bootstyle=cor)
        self.lbl_status_titulo.config(bootstyle=cor)
        for lbl in self.status_labels:
            lbl.config(bootstyle=cor)
        self.frame_hab.config(bootstyle=cor)
        self.lbl_hab_titulo.config(bootstyle=cor)
        for lbl in self.hab_labels:
            lbl.config(bootstyle=cor)

    def on_select(self, event):
        escolhido = self.combo.get()
        self.trocar_pokemon(escolhido)

if __name__ == "__main__":
    janela = ttk.Window(themename="darkly")
    app = PokedexApp(janela)
    janela.mainloop()
