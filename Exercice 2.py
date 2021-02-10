from tkinter import *

window = Tk()
window.title(" Exercice 1")
window.geometry("500x600")
window.config(background='red')

WIDTH = 500
HEIGHT = 500

c = Canvas(window, width=WIDTH, height=HEIGHT, bg = "white")
n = Button(window, text= "pause", font=("Courrier", 16), bg='white', fg='#00758F')

#c.create_line(x0,y0,x1,y1, fill=couleur)

#varaible des droites 
a=0
b=0
couleur = "blue"
def line (event) : 
    global x0,x1,y0,y1,a,couleur,b
    if b==0 : 
        if a==0 : 
            x0=event.x
            y0=event.y
            a+=1
        elif a==1 :     
            x1=event.x
            y1=event.y
            a-=1
            c.create_line(x0,y0,x1,y1, fill=couleur) 
            b+=1
    elif b==1 : 
        if a==0 : 
            x0=event.x
            y0=event.y
            a+=1
        elif a==1 :     
            x1=event.x
            y1=event.y
            c.create_line(x0,y0,x1,y1, fill='red')
            a-=1 
            b+=1
    elif b==2 : 
        c.delete('all')
        b=0

        


                
        



        



#Positionnement 
c.grid(column = 0, row = 0)
n.grid(column = 0, row = 1)


i = c.bind("<Button-1>",line )
window.mainloop()