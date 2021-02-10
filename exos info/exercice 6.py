from tkinter import *

window = Tk()
window.title(" Exercice 1")
window.geometry("700x500")

w = 500
z = 500

vert = "#20FF00"
jaune = "#FFFB00"
bleu = "#0003FF"
noir = "black"

c = Canvas(window, width=w, height=z, bg = "white")

carre_vert = c.create_rectangle((0,0),(50,50), fill = vert )
carre_jaune = c.create_rectangle((50,0),(100,50),fill = jaune)
carre_bleu = c.create_rectangle((100,0),(150,50), fill =bleu)
cercle = c.create_oval((225, 225),(275,275), fill = noir)

last_color = []

def change_culeur (event) :
    global vert, jaune, bleu, noir, last_color
    if event.x >= 0 and event.x <= 50 and event.y >= 0 and event.y<= 50 :
        c.itemconfigure(cercle, fill = vert )
        last_color.append(vert)
    elif event.x >= 50 and event.x <= 100 and event.y >= 0 and event.y<= 50 :
        c.itemconfigure(cercle, fill= jaune)
        last_color.append(jaune)
    elif event.x >= 100 and event.x <= 150 and event.y >= 0 and event.y<= 50 :
        c.itemconfigure(cercle, fill=bleu)
        last_color.append(bleu)
    else:
        c.itemconfigure(cercle, fill=noir)
        last_color.append(noir)

retour = 0

def annuler () :
    global vert, jaune, bleu, noir, last_color, retour
    if last_color == [] :
        c.itemconfigure(cercle, fill="black")
        return
    else:
        retour = last_color[-1]
        del last_color [-1]
        c.itemconfigure(cercle, fill=retour)



b = Button(window, text="Annuler", font=("Courrier", 16), bg='white', fg='BLUE', command = annuler )

c.bind("<Button-1>", change_culeur)

c.grid(column=0, row=0)
b.grid(column=1, row=0)
window.mainloop()