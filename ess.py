from tkinter import *

window = Tk()
window.title("Exercice 1")
window.geometry("500x600")

w = 500
z = 500

c = Canvas(window, width=w, height=z, bg = "black")

couleur = ["red","blue"]
v = c.create_rectangle((100, 100), (400, 300), fill="red")

def changer_couleur(event) :
    global couleur
    if event.x > 100 and event.x < 400 and event.y > 100 and event.y < 300:
            for i in  couleur :
                if i == "blue":

                c.itemconfigure(v, fill=i)

                    i -= 1
    elif couleur == "blue" and event.x > 100 and event.x < 400 and event.y > 100 and event.y < 300 :
             couleur = "red"
             c.itemconfigure(v, fill=couleur)
             return
    else:
        couleur = couleur
        c.itemconfigure(v, fill=couleur)


b = Button(window, text="Redémarrer" , font=("Courrier", 16), bg='white', fg='BLUE' )
i = c.bind("<Button-1>", changer_couleur)
c.grid(column = 0, row = 0)
b.grid(column = 0, row = 1)
window.mainloop()