from tkinter import (Tk, Canvas, N, W, E, S, Event, Button, Frame, RAISED, PhotoImage)
from PIL import Image, ImageTk
from os import getcwd

class App(Tk):
    def __init__(self,name,width,height):
        super().__init__()
        self.name = name
        self.width = width
        self.height = height
        self.middle_width = width//2
        self.middle_height = height//2
        self.canva_bg = "gray"
        self.tk_sticky_all = (N,W,E,S)
        self.focused_tag=None
        self.frame = Frame(self)
        self.canva = Canvas(self.frame, height=self.height-100, width=self.width-120, bg=self.canva_bg)

        #définition des images
        self.img_pc = ImageTk.PhotoImage(Image.open("pc.png"))
        self.img_router = ImageTk.PhotoImage(Image.open("router.png"))
        self.img_switch = ImageTk.PhotoImage(Image.open("switch.png"))


        self.button_pc = Button(self.frame,relief=RAISED,image=self.img_pc, command=lambda: self.spawn(self.img_pc))
        self.button_router = Button(self.frame,relief=RAISED,image=self.img_router, command=lambda : self.spawn(self.img_router))
        self.button_switch = Button(self.frame,relief=RAISED,image=self.img_switch, command=lambda : self.spawn(self.img_switch))

        #définition de la grid
        self.canva.grid(row=0, column=1,sticky=self.tk_sticky_all)
        self.frame.grid(row=0, column=0,sticky=self.tk_sticky_all)
        
        x,y = 1,0
        for button in [self.button_pc, self.button_router, self.button_switch]:
            button.grid(row=x, column=y)
            y+=1

    def spawn(self,image):
        new_img = self.canva.create_image(350, 350, image=image)
        self.canva.tag_bind(new_img, "<Button-1>", lambda event : self.follow(event,True))
        self.canva.tag_bind(new_img, "<B1-Motion>", self.follow)

    def follow(self, event:Event, is_clicked:bool=False):
        x = event.x
        y = event.y
        if is_clicked:
            self.focused_tag = self.canva.find_closest(x,y)[0]
            self.canva.tag_raise(self.focused_tag)
        self.canva.moveto(self.focused_tag, x-24, y-24)

    def run(self):
        self.geometry(f'{self.width}x{self.height}')
        self.title(self.name)
        self.iconphoto(True,PhotoImage(file="pc.png"))
        
        try:
            self.mainloop()
        except KeyboardInterrupt:
            self.destroy()

t = App("NDT - Network Drawing Thing",800,800)
t.run()