from tkinter import (Tk, Canvas, N, W, E, S, Event, Button, Frame, PhotoImage, Menu)
from PIL import Image, ImageTk

class App(Tk):
    def __init__(self,name,width,height):
        super().__init__()
        #définition de la fenêtre principale
        self.name = name
        self.width = width
        self.height = height
        self.canva_bg = "gray"
        
        #variables à utiliser
        self.tk_sticky_all = (N,W,E,S)
        self.middle_width = width//2
        self.middle_height = height//2
        self.focused_tag=None
        self.toggle_remove_flag=False
        
        #dans la fenêtre principale
        self.frame = Frame(self)
        self.canva = Canvas(self.frame, height=self.height-100, width=self.width-120, bg=self.canva_bg)

        #définition du menu
        self.context_menu = Menu(self.canva, tearoff=0)
        self.context_menu.add_command(label = "Modifier le nom")#, command = lambda:self.hey("hi"))
        self.context_menu.add_separator() 
        self.context_menu.add_command(label = "Modifier l'icône")#, command = lambda:self.hey("hello"))

        #définition des images
        self.img_pc = ImageTk.PhotoImage(Image.open("pc.png"))
        self.img_client = ImageTk.PhotoImage(Image.open("router.png"))
        self.img_switch = ImageTk.PhotoImage(Image.open("switch.png"))

        #définition des boutons
        self.button_pc = Button(self.frame,image=self.img_pc, command=lambda: self.spawn(self.img_pc))
        self.button_client = Button(self.frame,image=self.img_client, command=lambda: self.spawn(self.img_client))
        self.button_switch = Button(self.frame,image=self.img_switch, command=lambda: self.spawn(self.img_switch))

        #définition de la grid
        self.canva.grid(row=0, column=1,sticky=self.tk_sticky_all,columnspan=3)
        self.frame.grid(row=0, column=0,sticky=self.tk_sticky_all)
        
        #affichage des boutons par boucle for (f is for flemme)
        x,y = 1,1
        for button in [self.button_pc, self.button_client, self.button_switch]:
            button.grid(row=x, column=y)
            y+=1
        
        self.img_remove = ImageTk.PhotoImage(Image.open("cross.png"))
        self.button_remove = Button(self.frame,image=self.img_remove, command= lambda: self.toggle_remove() ).grid(row=0,column=0)


    #apparition de l'élément selon le bouton sélectionné, héritant donc de l'image adéquat
    def spawn(self,image):
        new_img = self.canva.create_image(350, 350, image=image)

        self.canva.tag_bind(new_img, "<Button-1>", lambda event : self.follow(event,True))
        self.canva.tag_bind(new_img, "<B1-Motion>", self.follow)
        self.canva.tag_bind(new_img, "<Button-3>", self.menu)

    #suivre la souris au déplacement + suppression si le flag renove est True
    def follow(self, event:Event, is_clicked:bool=False):
        x = event.x
        y = event.y
        if is_clicked:
            self.focused_tag = self.canva.find_closest(x,y)[0]
            if self.toggle_remove_flag:
                self.canva.delete(self.focused_tag)
            self.canva.tag_raise(self.focused_tag)
        self.canva.moveto(self.focused_tag, x-24, y-24)

    #lancer programme
    def run(self):
        self.geometry(f'{self.width}x{self.height}')
        self.title(self.name)
        self.iconphoto(True,PhotoImage(file="pc.png"))

        try:
            self.mainloop()
        except KeyboardInterrupt:
            self.destroy()

    #changer le flag pour la suppression
    def toggle_remove(self):
        if self.toggle_remove_flag == False:
            self.toggle_remove_flag = True
            self.config(cursor="tcross")
        else:
            self.toggle_remove_flag = False
            self.config(cursor="arrow")

    #création du menu contextuel au clic droit
    def menu(self, event:Event):
        x, y = event.widget.winfo_pointerxy()
        try: 
            self.context_menu.tk_popup(x,y)
        finally: 
            self.context_menu.grab_release() 

t = App("NDT - Network Drawing Thing",800,800)
t.run()