# importe les librairies nécessaires
from tkinter import *
from PIL import Image, ImageTk
from random import randint

# fenetre principal
root = Tk()
root.title("Pierre Papier Ciseaux !")
root.configure(background="#d3c5d8")

# images du jeu
pierre_img = ImageTk.PhotoImage(Image.open("pierre.png")) #méthode imageTK
papier_img = ImageTk.PhotoImage(Image.open("papier.png"))
ciseaux_img = ImageTk.PhotoImage(Image.open("ciseaux.png"))
pierre_img_ia = ImageTk.PhotoImage(Image.open("pierre_aversaire.png"))
papier_img_ia = ImageTk.PhotoImage(Image.open("papier_adversaire.png"))
ciseaux_img_ia = ImageTk.PhotoImage(Image.open("ciseaux_adversaire.png"))

# insert les images
joueur_label = Label(root, image=ciseaux_img, bg="#d3c5d8") #méthode label
ia_label = Label(root, image=ciseaux_img_ia, bg="#d3c5d8")
ia_label.grid(row=1, column=0) #méthode grid
joueur_label.grid(row=1, column=4)


# scores
joueurScore = Label(root, text=0, font=100, bg="#d3c5d8", fg="white")
iaScore = Label(root, text=0, font=100, bg="#d3c5d8", fg="white")
iaScore.grid(row=1, column=1)
joueurScore.grid(row=1, column=3)

# indicateurs
joueur_indicator = Label(root, font=50, text="JOUEUR", bg="#d3c5d8", fg="white")
ia_indicator = Label(root, font=50, text="ADVERSAIRE",
                       bg="#d3c5d8", fg="white")
joueur_indicator.grid(row=0, column=3)
ia_indicator.grid(row=0, column=1)

# messages
msg = Label(root, font=50, bg="#d3c5d8", fg="white")
msg.grid(row=3, column=2)

# met en place messages
def updateMessage(x):
    msg['text'] = x

# met en place le score du joueur
def updateJoueurScore():
    score = int(joueurScore["text"])
    score += 1
    joueurScore["text"] = str(score)

# met en place le score de l'IA
def updateIaScore():
    score = int(iaScore["text"])
    score += 1
    iaScore["text"] = str(score)

# défini le gagnant
def checkGagnant(joueur, ia):
    if joueur == ia:
        updateMessage("Egalité!!!")
    elif joueur == "pierre":
        if ia == "papier":
            updateMessage("Tu as perdu")
            updateIaScore()
        else:
            updateMessage("Tu gagnes")
            updateJoueurScore()
    elif joueur == "papier":
        if ia == "ciseaux":
            updateMessage("Tu as perdu")
            updateIaScore()
        else:
            updateMessage("Tu gagnes")
            updateJoueurScore()
    elif joueur == "ciseaux":
        if ia == "pierre":
            updateMessage("Tu as perdu")
            updateIaScore()
        else:
            updateMessage("Tu gagnes")
            updateJoueurScore()

    else:
        pass


# créer choix
choix = ["pierre", "papier", "ciseaux"]


def updateChoix(x):

    # pour l'IA
    iaChoix = choix[randint(0, 2)] #méthode randint
    if iaChoix == "pierre":
        ia_label.configure(image=pierre_img_ia)
    elif iaChoix == "paper":
        ia_label.configure(image=papier_img_ia)
    else:
        ia_label.configure(image=ciseaux_img_ia)


# pour le joueur
    if x == "pierre":
        joueur_label.configure(image=pierre_img)
    elif x == "papier":
        joueur_label.configure(image=papier_img)
    else:
        joueur_label.configure(image=ciseaux_img)

    checkGagnant(x, iaChoix)

# bouttons
pierre = Button(root, width=20, height=2, text="PIERRE", #méthode Button (tkinter)
              bg="#FF3E4D", fg="white", command=lambda: updateChoix("pierre")).grid(row=2, column=1)
papier = Button(root, width=20, height=2, text="PAPIER",
               bg="#FAD02E", fg="white", command=lambda: updateChoix("papier")).grid(row=2, column=2)
ciseaux = Button(root, width=20, height=2, text="CISEAUX",
                 bg="#0ABDE3", fg="white", command=lambda: updateChoix("ciseaux")).grid(row=2, column=3)

root.mainloop() ##boucle while qui 'execute' tous les events
