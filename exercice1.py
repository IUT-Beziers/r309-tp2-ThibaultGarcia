import tkinter as tk
from tkinter import Event
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry('800x800')
root.title('Sis-co Paquette Tasoeur')

canvas = tk.Canvas(root, width=700, height=700, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)


img = ImageTk.PhotoImage(Image.open("./broken.png"))

def suivre(event:Event):
    x = event.x
    y = event.y
    focused_tag = canvas.find_closest(x, y)[0]
    print(focused_tag)
    canvas.moveto(focused_tag, x-32, y-32)
    return

dict = {}
def apparition():
    dict[f"{350}/{350}"] = canvas.create_image(350, 350, image=img)
    canvas.tag_bind(dict[f"{350}/{350}"], "<B1-Motion>", suivre)
    

bouton = tk.Button(root, relief=tk.RAISED, image=img, command=apparition).pack()

root.mainloop()