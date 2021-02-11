from tkinter import *
import random as rd

window = Tk()
window.title(" Exercice 1")
window.geometry("600x500")

WIDTH = 600
HEIGHT = 400
couleur = "red"
dx = 1
dy = 2

c = Canvas(window, width=WIDTH, height=HEIGHT, bg="black")

def creer_balle() :
    global b,balle
    b = c.create_oval((290, 190), (310, 210), fill="#1000FF")
    balle = c.coords(b)
    rdm1 = rd.randint(1,7)
    rdm2 = rd.randint(1,7)
    balle.append(rdm1)
    balle.append(rdm2)

v = creer_balle()

def rebond1():
    global dx,dy
    balle = c.coords(b)
    if balle[1] <= 0 or balle[3] >= HEIGHT:
        dy = - dy

    if balle[0] <= 0 or balle[2] >= WIDTH:
        dx = - dx


def get_color(r=0, g=0, b=0):
    """ Retourne une couleur à partir de ses composantes r, g, b"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def change_color ():
    balle = c.coords(b)
    if balle[1] <= 0 or balle[3] >= HEIGHT:
        col = get_color(rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255))
        c.itemconfigure(b, fill = col)
    if balle[0] <= 0 or balle[2] >= WIDTH:
        col = get_color(rd.randint(0, 255), rd.randint(0, 255), rd.randint(0, 255))
        c.itemconfigure(b, fill=col)
def mouvement() :
    global dx, dy, move

    c.move(b, dx, dy)
    move = c.after(10, mouvement)
    button.config(text="pause")
    rebond1()
    change_color()


def stop():

    """ stoppe le mouvement des balles"""
    if move is None:
         return
    c.after_cancel(move)

nb = 0

def command ():
    global move
    global nb
    if nb == 0 :
        mouvement()
        button.config(text="stop")
        nb += 1
    elif nb == 1 :
        stop()
        button.config(text="restart")
        nb -= 1



button = Button(window, text= "Démarrer", font=("Courrier", 20), bg='white', fg='#00758F',command =command)

c.grid(column=0, row=0)
button.grid(column = 0, row = 1)
window.mainloop()