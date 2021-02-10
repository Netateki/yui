from tkinter import *

window = Tk()
window.title(" 8888888888888888888888")
window.geometry("600x700")

w = 600
z = 600

c = Canvas(window, width=w, height=z, bg = "white")

red = 200
blue = 400
red_line = c.create_line((red, 0), (red, 600), fill="red")
blue_line = c.create_line((blue, 0), (blue, 600), fill="blue")

def move_objet(event):
    global red
    global blue

    if event.x < red :
        c.move(red_line, -10,0)
        red -= 10
    elif event.x > red :
        c.move(red_line, 10,0)
        red += 10

    if event.x < blue :
        c.move(blue_line, -10,0)
        blue -= 10
    elif event.x > blue :
        c.move(blue_line, 10,0)
        blue += 10

def restart () :
    global red, blue, red_line, blue_line
    red = 200
    blue = 400
    c.delete(red_line)
    c.delete(blue_line)
    red_line = c.create_line((red, 0), (red, 600), fill="red")
    blue_line = c.create_line((blue, 0), (blue, 600), fill="blue")

b = Button(window, text="Redémarrer" , font=("Courrier", 16), bg='white', fg='BLUE',command = restart )


c.bind("<Button-1>", move_objet)

c.grid(column = 0, row = 0)
b.grid(column = 0, row = 1)
window.mainloop()