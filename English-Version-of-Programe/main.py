from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from dados import *  # Assuming your data is in 'dados'

############## colors ################
co0 = "#444466"  # black 
co1 = "#feffff"  # white 
co2 = "#6f9fbd"  # blue
co3 = "#38576b"  # value
co4 = "#403d3d"  # text
co5 = "#ef5350"  # red

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

# Create the main window
window = Tk()
window.title('')
window.geometry('550x510')
window.configure(bg=co1)

# Add separator
ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=272)

style = ttk.Style(window)
style.theme_use("clam")

# Create frame for Pokémon details
frame_pokemon = Frame(window, width=550, height=290, relief='flat')
frame_pokemon.grid(row=1, column=0)

def change_pokemon(name):
    global pokemon_image

    # Update Pokémon name, type, and ID
    pok_name.config(text=name)
    pok_type.config(text=pokemon[name]['type'][1])
    pok_id.config(text=pokemon[name]['type'][0])

    # Update Pokémon stats
    pok_hp.config(text=f"HP: {pokemon[name]['stats'][0]}")
    pok_attack.config(text=f"Attack: {pokemon[name]['stats'][1]}")
    pok_defense.config(text=f"Defense: {pokemon[name]['stats'][2]}")
    pok_speed.config(text=f"Speed: {pokemon[name]['stats'][3]}")
    pok_total.config(text=f"Total: {pokemon[name]['stats'][4]}")

    # Update abilities
    pok_ability_1.config(text=f"Ability 1: {pokemon[name]['abilities'][0]}")
    pok_ability_2.config(text=f"Ability 2: {pokemon[name]['abilities'][1]}")

    # Update Pokémon image
    pokemon_image = Image.open(pokemon[name]['type'][2])
    pokemon_image = pokemon_image.resize((238, 238))
    pokemon_image = ImageTk.PhotoImage(pokemon_image)
    pok_image.config(image=pokemon_image)

    # Update background color
    background_color = background_colors.get(name, co1)  # Default color if not found
    frame_pokemon.config(bg=background_color)
    pok_name.config(bg=background_color)
    pok_type.config(bg=background_color)
    pok_id.config(bg=background_color)
    pok_image.config(bg=background_color)

# Labels for Pokémon attributes
pok_name = Label(frame_pokemon, text='Pikachu', relief='flat', anchor=CENTER, font='fixedsys 20', bg=co1, fg=co0)
pok_name.place(x=12, y=15)

pok_type = Label(frame_pokemon, text='Electric', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pok_type.place(x=12, y=50)

pok_id = Label(frame_pokemon, text='#025', relief='flat', anchor=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0)
pok_id.place(x=12, y=75)

# Pokémon stats (HP, Attack, Defense, Speed, Total)
pok_hp = Label(window, text='HP:', font=('Ivy 10 bold'), bg=co1, fg=co4)
pok_hp.place(x=12, y=300)

pok_attack = Label(window, text='Attack:', font=('Ivy 10 bold'), bg=co1, fg=co4)
pok_attack.place(x=12, y=320)

pok_defense = Label(window, text='Defense:', font=('Ivy 10 bold'), bg=co1, fg=co4)
pok_defense.place(x=12, y=340)

pok_speed = Label(window, text='Speed:', font=('Ivy 10 bold'), bg=co1, fg=co4)
pok_speed.place(x=12, y=360)

pok_total = Label(window, text='Total:', font=('Ivy 10 bold'), bg=co1, fg=co4)
pok_total.place(x=12, y=380)

# Pokémon abilities
pok_ability_1 = Label(window, text='Ability 1:', font=('Ivy 10 bold'), bg=co1, fg=co4)
pok_ability_1.place(x=12, y=420)

pok_ability_2 = Label(window, text='Ability 2:', font=('Ivy 10 bold'), bg=co1, fg=co4)
pok_ability_2.place(x=12, y=440)

# Initial Pokémon image (Pikachu)
pokemon_image = Image.open('imagens/pikatcu-3D.png')
pokemon_image = pokemon_image.resize((238, 238))
pokemon_image = ImageTk.PhotoImage(pokemon_image)

pok_image = Label(frame_pokemon, image=pokemon_image, relief='flat', bg=co1, fg=co0)
pok_image.place(x=60, y=50)

# Button creation for Pokémon
pokemon_list = list(pokemon.keys())  # Assumes you have a dictionary `pokemon` from 'dados'

for i, name in enumerate(pokemon_list):
    img = Image.open(f'imagens/{name.lower()}-img.png')  # Assuming filenames match Pokémon names
    img = img.resize((40, 40))
    img = ImageTk.PhotoImage(img)
    button = Button(window, command=lambda name=name: change_pokemon(name),
                    image=img, text=name, width=150, relief='raised', overrelief=RIDGE, 
                    compound=LEFT, anchor=NW, padx=5, font=('verdana 12'), bg=co1, fg=co0)
    button.place(x=375, y=10 + i * 55)

# Set initial Pokémon to Pikachu
change_pokemon('Pikachu')

# Start the Tkinter main loop
window.mainloop()
