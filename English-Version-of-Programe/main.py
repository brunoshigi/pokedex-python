from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from data import * 

############## colors ################
co0 = "#444466" # black 
co1 = "#feffff" # white 
co2 = "#6f9fbd" # blue
co3 = "#38576b" # value
co4 = "#403d3d" # text
co5 = "#ef5350" # red

# Background color dictionary for each Pokémon
background_colors = {
    'Pikachu': "#ffff00",
    'Bulbasaur': "#40e0d0",
    'Charmander': "#ff7f50",
    'Eevee': "#e6daa6",
    'Mew': "#ff81c0",
    'Chikorita': "#90ee90",
    'Gengar': "#c79fef",
    'Squirtle': "#add8e6"
}

# creating window 
window = Tk()
window.title('')
window.geometry('550x510')
window.configure(bg=co1)

ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(window)
style.theme_use("clam")

# creating frame 
frame_pokemon = Frame(window, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

def change_pokemon(name):
    global pok_name, pok_type, pok_id, pok_hp, pok_attack, pok_defense, pok_speed, pok_total, pok_ability_1, pok_ability_2, pok_image, pokemon_image

    # Update Pokémon type
    pok_name.config(text=name)
    pok_type.config(text=pokemon[name]['type'][1])
    pok_id.config(text=pokemon[name]['type'][0])

    # Update stats
    pok_hp.config(text=pokemon[name]["stats"][0])
    pok_attack.config(text=pokemon[name]["stats"][1])
    pok_defense.config(text=pokemon[name]["stats"][2])
    pok_speed.config(text=pokemon[name]["stats"][3])
    pok_total.config(text=pokemon[name]["stats"][4])

    # Update abilities
    abilities = pokemon[name]["abilities"]
    pok_ability_1.config(text=abilities[0])
    pok_ability_2.config(text=abilities[1])

    # Update Pokémon image
    pokemon_image = Image.open(pokemon[name]['type'][2])
    pokemon_image = pokemon_image.resize((238,238))
    pokemon_image = ImageTk.PhotoImage(pokemon_image)
    pok_image.config(image=pokemon_image)

    # Update background color of frame and Pokémon name
    background_color = background_colors.get(name, co1)  # Default color if not in list
    frame_pokemon.config(bg=background_color)
    pok_name.config(bg=background_color)
    pok_type.config(bg=background_color)
    pok_id.config(bg=background_color)
    pok_image.config(bg=background_color)

# name 
pok_name = Label(frame_pokemon, text='Pikachu', relief='flat', anchor=CENTER, font='fixedsys 20', bg=co1, fg=co0)
pok_name.place(x=12, y=15)

# category 
pok_type = Label(frame_pokemon, text='Electric', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pok_type.place(x=12, y=50)

# id
pok_id = Label(frame_pokemon, text='#025', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pok_id.place(x=12, y=75)

# Pokémon image
pokemon_image = Image.open('images/pikachu-3D.png')
pokemon_image = pokemon_image.resize((238,238))
pokemon_image = ImageTk.PhotoImage(pokemon_image)

pok_image = Label(frame_pokemon, image=pokemon_image, relief='flat', bg=co1, fg=co0)
pok_image.place(x=60, y=50)

# Pokémon images (to be updated dynamically)
pokemon_image_files = [
    'images/pikachu-3D.png',
    'images/bulbasaur-img.png',
    'images/charmander.png',
    'images/eevee-preview.png',
    'images/mew-img.png',
    'images/chikorita_0.png',
    'images/gengar-img.png',
    'images/squirtle-img.png'
]

# Creating buttons for Pokémon

for i, pokemon_image_file in enumerate(pokemon_image_files):
    img = Image.open(pokemon_image_file)
    img = img.resize((40,40))
    img = ImageTk.PhotoImage(img)
    button = Button(window, command=lambda name=list(pokemon.keys())[i]: change_pokemon(name),
                    image=img, text=list(pokemon.keys())[i], width=150, relief='raised', overrelief=RIDGE, 
                    compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
    button.place(x=375, y=10 + i * 55)

# Initial Pokémon set to Pikachu
change_pokemon('Pikachu')

# start the tkinter main loop
window.mainloop()
