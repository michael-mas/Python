import string
from random import randint, choice
from tkinter import *

def generate_password():
    password_min = 6
    password_max = 12
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

window = Tk()
window.title("generateur")
window.geometry("720x480")
window.iconbitmap("logo chat.ico")
window.config(background='#ff0000')

frame = Frame(window, bg='#ff0000')

width = 300
height = 300
image = PhotoImage(file="logo chat.png").zoom(35).subsample(32)
canvas = Canvas(frame, width=width, height=height, bg='#ff0000', bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

right_frame = Frame(frame, bg='#808080')

label_title = Label(right_frame, text="Mot de passe", font=("Helvetica", 20), bg='#808080', fg='white')
label_title.pack()

password_entry = Entry(right_frame, font=("Helvetica", 20), bg='#000000', fg='white')
password_entry.pack()

generate_password_button = Button(right_frame, text="Générer", font=("Helvetica", 20), bg='#808080', fg='white', command=generate_password)
generate_password_button.pack(fill=X)

right_frame.grid(row=0, column=1, sticky=W)

frame.pack(expand=YES)

menu_bar = Menu(window)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label="Fichier", menu=file_menu)

window.config(menu=menu_bar)


window.mainloop()

