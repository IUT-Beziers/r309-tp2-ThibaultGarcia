import tkinter as tk
from tkinter import (Event, N, W, E, S, Frame)
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('800x800')
root.title('Sis-co Paquette Tasoeur')
root.grid()

canvas = tk.Canvas(root, height=700, width=700, bg='white')
canvas.grid(row=0, column=1,sticky=(N,W,E,S))

img1 = ImageTk.PhotoImage(Image.open("./pc.png"))
img2 = ImageTk.PhotoImage(Image.open("./router.png"))
img3 = ImageTk.PhotoImage(Image.open("./switch.png"))

def suivre(event:Event):
    x = event.x
    y = event.y
    focused_tag = canvas.find_closest(x, y)[0]
    canvas.moveto(focused_tag, x-24, y-24)
    return

dict = {}
def apparition(passe):
    dict[f"{350}/{350}"] = canvas.create_image(350, 350, image=passe)
    canvas.tag_bind(dict[f"{350}/{350}"], "<B1-Motion>", suivre)


rectan=Frame(root).grid(column=1,row=1)

bouton1= tk.Button(rectan, relief=tk.RAISED, image=img1, command=lambda: apparition(img1))
bouton1.grid(row=1, column=0)
bouton2= tk.Button(rectan, relief=tk.RAISED, image=img2, command=lambda: apparition(img2))
bouton2.grid(row=1, column=1)
bouton3= tk.Button(rectan, relief=tk.RAISED, image=img3, command=lambda: apparition(img3))
bouton3.grid(row=1, column=2)


root.mainloop()