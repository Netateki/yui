from tkinter import * 

fenetre=Tk()

#Titre et caractérisituqe de la petite fenetre : 
fenetre.title("Exercice 4") 
fenetre.geometry("500x600")
fenetre.config(background='red')

#Le canvas 

WIDTH = 500
HEIGHT = 500

canvas= Canvas(fenetre, width=WIDTH, height=HEIGHT, bg = "black")
canvas.grid(row=0, column=0) 
#le bouton 

bouton= Button(fenetre, text="Pause" , font=("Courrier", 16), bg='white', fg='Red')
bouton.grid(row=2,column=0)


#Le carré rouge
couleur="red"

c=canvas.create_rectangle(225,225,275,275, fill=couleur)

def changer_couleur(event) :
    global couleur
    if  event.x > 225 and event.x < 275 and event.y > 225 and event.y < 275 :
            if couleur == "red":
               couleur = "blue"
               canvas.itemconfigure(c, fill=couleur)


canvas.bind("<Button-1>", changer_couleur)

#Faire fonctionner
fenetre.mainloop()