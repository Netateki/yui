from tkinter import *

window = Tk()
window.title(" Exercice 1")
window.geometry("500x600")

WIDTH = 500
HEIGHT = 500

c = Canvas(window, width=WIDTH, height=HEIGHT, bg = "black")

b = Button(window, text= "start", font=("Courrier", 20), bg='white', fg='#00758F')

r = [2,4,8,16]

for i in range (10) :
    for j in range (10) :
        carre = c.create_rectangle((i * 50, j * 50),((i + 1) * 50, (j + 1) * 50), fill="red")

for i in range (0,550,50) :
    c.create_line((i, 0), (i,WIDTH), fill="white")
    c.create_line((0, i), ( WIDTH,i), fill="white")

id_line = []
false_id = []
for i in range (101,121) :
    id_line.append(i)
for i in id_line :
    false_id.append((i,))

pp = []
ppp = []
a = 0
def change_color(event):
    global pp, object, a
    objet = c.find_closest(event.x, event.y)
    if not objet in false_id :

        c.delete(objet[0])

        pp.append((objet[0],))
        ppp.append(objet[0])
        print(objet)
        print(pp)


c.bind("<Button-1>", change_color)



c.grid(column = 0, row = 0)
b.grid(column = 0, row = 1)

window.mainloop()