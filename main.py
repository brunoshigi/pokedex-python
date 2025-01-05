from tkinter import * 
from tkinter import ttk

# importando pillow
from PIL import Image, ImageTk

from dados import * 

############## cores ################
co0 = "#444466" # preta 
co1 = "#feffff" # branca 
co2 = "#6f9fbd" # azul
co3 = "#38576b" # valor
co4 = "#403d3d" # letra
co5 = "#ef5350" # vermelha
co6 = "#d3d3d3" # cinza claro

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

# criando janela 
janela = Tk()
janela.title('Pokédex')
janela.geometry('600x600')
janela.configure(bg=co1)

# Adicionando bordas e detalhes
frame_borda = Frame(janela, width=600, height=600, bg=co6, relief='flat')
frame_borda.grid(row=0, column=0, padx=10, pady=10)

frame_pokemon = Frame(frame_borda, width=580, height=290, relief='flat', bg=co1)
frame_pokemon.grid(row=0, column=0, padx=10, pady=10)

# Separador
ttk.Separator(frame_borda, orient=HORIZONTAL).grid(row=1, columnspan=1, ipadx=272)

style = ttk.Style(janela)
style.theme_use("clam")

def trocar_pokemon(i):
    global pok_nome, pok_tipo, pok_id, pok_hp, pok_atack, pok_defesa, pok_velocidade, pok_total, pok_hb_1, pok_hb_2, pok_imagem, imagem_pokemon

    # Atualizar tipo de pokemon
    pok_nome.config(text=i)
    pok_tipo.config(text=pokemon[i]['tipo'][1])
    pok_id.config(text=pokemon[i]['tipo'][0])

    # Atualizar status
    pok_hp.config(text=pokemon[i]["status"][0])
    pok_atack.config(text=pokemon[i]["status"][1])
    pok_defesa.config(text=pokemon[i]["status"][2])
    pok_velocidade.config(text=pokemon[i]["status"][3])
    pok_total.config(text=pokemon[i]["status"][4])

    # Atualizar habilidades
    habilidades = pokemon[i]["habilidades"]
    pok_hb_1.config(text=habilidades[0])
    pok_hb_2.config(text=habilidades[1])

    # Atualizar imagem do Pokémon
    imagem_pokemon = Image.open(pokemon[i]['tipo'][2])
    imagem_pokemon = imagem_pokemon.resize((238,238))
    imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)
    pok_imagem.config(image=imagem_pokemon)

    # Atualizar cor de fundo do frame e nome do Pokémon
    cor_fundo = cores_fundo.get(i, co1)  # Cor padrão se não estiver na lista
    frame_pokemon.config(bg=cor_fundo)
    pok_nome.config(bg=cor_fundo)
    pok_tipo.config(bg=cor_fundo)
    pok_id.config(bg=cor_fundo)
    pok_imagem.config(bg=cor_fundo)

# nome 
pok_nome = Label(frame_pokemon, text='Pikachu', relief='flat', anchor=CENTER, font='fixedsys 20', bg=co1, fg=co0)
pok_nome.place(x=12, y=15)

# categoria 
pok_tipo = Label(frame_pokemon, text='Eletrico', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pok_tipo.place(x=12, y=50)

# id
pok_id = Label(frame_pokemon, text='#025', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pok_id.place(x=12, y=75)

# image do pokemon
imagem_pokemon = Image.open('imagens/pikatcu-3D.png')
imagem_pokemon = imagem_pokemon.resize((238,238))
imagem_pokemon = ImageTk.PhotoImage(imagem_pokemon)

pok_imagem = Label(frame_pokemon, image=imagem_pokemon, relief='flat', bg=co1, fg=co0)
pok_imagem.place(x=60, y=50)

pok_tipo.lift()

# status
pok_status = Label(frame_borda, text='Status', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_status.place(x=15, y=310)

#hp
pok_hp = Label(frame_borda, text='HP: 500', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hp.place(x=15, y=360)

#atack
pok_atack = Label(frame_borda, text='Ataque: 600', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_atack.place(x=15, y=385)

#defesa
pok_defesa= Label(frame_borda, text='Defesa: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_defesa.place(x=15, y=410)

#velocidade
pok_velocidade = Label(frame_borda, text='Velocidade: 100', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_velocidade.place(x=15, y=435)

#total
pok_total = Label(frame_borda, text='Total: 1.700', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_total.place(x=15, y=460)

# Habilidades
pok_status = Label(frame_borda, text='Habilidades', relief='flat', anchor=CENTER, font=('Verdana 20'), bg=co1, fg=co0)
pok_status.place(x=180, y=310)

#hb
pok_hb_1 = Label(frame_borda, text='Choque do trovão', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hb_1.place(x=195, y=360)

#atack
pok_hb_2 = Label(frame_borda, text='soco eletrico', relief='flat', anchor=CENTER, font=('Verdana 10'), bg=co1, fg=co4)
pok_hb_2.place(x=195, y=385)

# Criando botões para pokemon

# imagem do pokemon
imagem_pokemon_1 = Image.open('imagens/cabeca-pikachu.png')
imagem_pokemon_1 = imagem_pokemon_1.resize((40,40))
imagem_pokemon_1 = ImageTk.PhotoImage(imagem_pokemon_1)

b_pok_1 = Button(frame_borda,command=lambda:trocar_pokemon('Pikachu'), image=imagem_pokemon_1, text='Pikachu', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
b_pok_1.place(x=375, y=10)

# imagem do pokemon
imagem_pokemon_2 = Image.open('imagens/cabeca-bulbasaur.png')
imagem_pokemon_2 = imagem_pokemon_2.resize((40,40))
imagem_pokemon_2 = ImageTk.PhotoImage(imagem_pokemon_2)

b_pok_2 = Button(frame_borda,command=lambda:trocar_pokemon('Bulbasaur'), image=imagem_pokemon_2, text='Bulbasaur', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
b_pok_2.place(x=375, y=65)

# imagem do pokemon
imagem_pokemon_3 = Image.open('imagens/cabeca-charmander.png')
imagem_pokemon_3 = imagem_pokemon_3.resize((40,40))
imagem_pokemon_3 = ImageTk.PhotoImage(imagem_pokemon_3)

b_pok_3 = Button(frame_borda,command=lambda:trocar_pokemon('Charmander'), image=imagem_pokemon_3, text='Charmander', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
b_pok_3.place(x=375, y=120)

# imagem do pokemon
imagem_pokemon_4 = Image.open('imagens/cabeça-evee.png')
imagem_pokemon_4 = imagem_pokemon_4.resize((40,40))
imagem_pokemon_4 = ImageTk.PhotoImage(imagem_pokemon_4)

b_pok_4 = Button(frame_borda,command=lambda:trocar_pokemon('Eevee'), image=imagem_pokemon_4, text='Eevee', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
b_pok_4.place(x=375, y=175)

# imagem do pokemon
imagem_pokemon_5 = Image.open('imagens/mew.cabeça.jpeg')
imagem_pokemon_5 = imagem_pokemon_5.resize((40,40))
imagem_pokemon_5 = ImageTk.PhotoImage(imagem_pokemon_5)

b_pok_5 = Button(frame_borda,command=lambda:trocar_pokemon('Mew'), image=imagem_pokemon_5, text='Mew', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
b_pok_5.place(x=375, y=230)

# imagem do pokemon
imagem_pokemon_6 = Image.open('imagens\chikorita-cabeça.png')
imagem_pokemon_6 = imagem_pokemon_6.resize((40,40))
imagem_pokemon_6 = ImageTk.PhotoImage(imagem_pokemon_6)

b_pok_6 = Button(frame_borda,command=lambda:trocar_pokemon('Chikorita'), image=imagem_pokemon_6, text='Chikorita', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
b_pok_6.place(x=375, y=285)

# imagem do pokemon
imagem_pokemon_7 = Image.open('imagens/cabeca-gengar.png')
imagem_pokemon_7 = imagem_pokemon_7.resize((40,40))
imagem_pokemon_7 = ImageTk.PhotoImage(imagem_pokemon_7)

b_pok_7 = Button(frame_borda,command=lambda:trocar_pokemon('Gengar'), image=imagem_pokemon_7, text='Gengar', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
b_pok_7.place(x=375, y=340)

# imagem do pokemon
imagem_pokemon_8 = Image.open('imagens/squirtlecabeça.img.png')
imagem_pokemon_8 = imagem_pokemon_8.resize((40,40))
imagem_pokemon_8 = ImageTk.PhotoImage(imagem_pokemon_8)

b_pok_8 = Button(frame_borda,command=lambda:trocar_pokemon('Squirtle'), image=imagem_pokemon_8, text='Squirtle', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
b_pok_8.place(x=375, y=395)

# Adicionar novos botões para os novos Pokémon

# imagem do pokemon
imagem_pokemon_9 = Image.open('imagens/jigglypuff.cabeça.png')
imagem_pokemon_9 = imagem_pokemon_9.resize((40,40))
imagem_pokemon_9 = ImageTk.PhotoImage(imagem_pokemon_9)

b_pok_9 = Button(frame_borda,command=lambda:trocar_pokemon('Jigglypuff'), image=imagem_pokemon_9, text='Jigglypuff', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
b_pok_9.place(x=375, y=450)

# imagem do pokemon
imagem_pokemon_10 = Image.open('imagens/lucario.cabeça.png')
imagem_pokemon_10 = imagem_pokemon_10.resize((40,40))
imagem_pokemon_10 = ImageTk.PhotoImage(imagem_pokemon_10)

b_pok_10 = Button(frame_borda,command=lambda:trocar_pokemon('Lucario'), image=imagem_pokemon_10, text='Lucario', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
b_pok_10.place(x=375, y=505)

# imagem do pokemon
imagem_pokemon_11 = Image.open('imagens/gyarados.cabeça.png')
imagem_pokemon_11 = imagem_pokemon_11.resize((40,40))
imagem_pokemon_11 = ImageTk.PhotoImage(imagem_pokemon_11)

b_pok_11 = Button(frame_borda,command=lambda:trocar_pokemon('Gyarados'), image=imagem_pokemon_11, text='Gyarados', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
b_pok_11.place(x=375, y=560)

# imagem do pokemon
imagem_pokemon_12 = Image.open('imagens/dragonite.cabeça.png')
imagem_pokemon_12 = imagem_pokemon_12.resize((40,40))
imagem_pokemon_12 = ImageTk.PhotoImage(imagem_pokemon_12)

b_pok_12 = Button(frame_borda,command=lambda:trocar_pokemon('Dragonite'), image=imagem_pokemon_12, text='Dragonite', width=150, relief='raised', overrelief=RIDGE, compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
b_pok_12.place(x=375, y=615)

# chamar a funçao para definir a imagem inicial como pikachu
trocar_pokemon('Pikachu')

# iniciar o loop inicial do tkinter
janela.mainloop()


