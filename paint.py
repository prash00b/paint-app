from tkinter import *
from tkinter import filedialog,messagebox,colorchooser
from PIL import  Image, ImageDraw
import PIL
import os
import datetime

#defining window size
WIDTH=500
HEIGHT =500
BLACK=(0,0,0)
CENTER = WIDTH//2

class PaintGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Paint Clone") 

        #brush width
        self.brush_width=15
        self.current_color="white"


        #setting width, height and color of cnavas
        self.cnv=Canvas(self.root,width=WIDTH-10,height=HEIGHT-10,bg ="black")
        self.cnv.pack()  #to pack widgets
        self.cnv.bind("<B1-Motion>", self.paint) #trigger when pressing right click

        self.image=PIL.Image.new("RGB",(WIDTH,HEIGHT),BLACK)
        self.draw=ImageDraw.Draw(self.image)

        self.btn_frame=Frame(self.root)
        self.btn_frame.pack(fill=X)

        self.btn_frame.columnconfigure(0,weight=1)
        self.btn_frame.columnconfigure(1,weight=1)
        self.btn_frame.columnconfigure(2,weight=1)

        self.clear_btn=Button(self.btn_frame,text="Clear",command=self.clear)
        self.clear_btn.grid(row=1,column=1, sticky = W+E)

        self.save_btn=Button(self.btn_frame,text="Save square",command=self.save_square)
        self.save_btn.grid(row=1,column=2, sticky = W+E)

        self.save_btn=Button(self.btn_frame,text="Save triangle",command=self.save_triangle)
        self.save_btn.grid(row=1,column=3, sticky = W+E)

        self.save_btn=Button(self.btn_frame,text="Save circle",command=self.save_circle)
        self.save_btn.grid(row=1,column=4, sticky = W+E)



        
        self.bplus_btn=Button(self.btn_frame,text="B+",command=self.brush_plus) #increase brush size
        self.bplus_btn.grid(row=0,column=1, sticky = W+E)

        self.bminus_btn=Button(self.btn_frame,text="B-",command=self.brush_minus)#decrease brush size
        self.bminus_btn.grid(row=0,column=0, sticky = W+E)

        # self.color_btn=Button(self.btn_frame,text="Change color",command=self.change_color)
        # self.color_btn.grid(row=0,column=2, sticky = W+E)

        self.root.protocol("WM_DELETE_WINDOW",self.close)
        self.root.attributes("-topmost",True)
        self.root.mainloop()

        
    def paint(self,event):
        x1,y1=(event.x-1),(event.y-1)
        x2,y2=(event.x+1),(event.y+1)
        self.cnv.create_rectangle(x1,y1,x2,y2,outline=self.current_color,fill=self.current_color,width=self.brush_width)
        self.draw.rectangle([x1,y1,x2+self.brush_width,y2+self.brush_width],outline = self.current_color, fill=self.current_color,width=self.brush_width)
    
    def clear(self): #clearing the screen
        self.cnv.delete("all")
        self.draw.rectangle([0,0,1000,1000],fill="black")

    def save_square(self):
        now = datetime.datetime.now()
        filename="image_{:%Y-%m-%d_%H-%M-%S}.png".format(now)
        default_dir = os.path.expanduser('square')
        # filename = filedialog.asksaveasfilename(
        #                                         initialdir=default_dir,
        #                                         initialfile=filename,
        #                                         defaultextension="png",
        #                                         filetypes=[("PNG","JPG"),(".png",".jpg")])
        filename = os.path.join(default_dir, filename)
        self.image.save(filename)

    def save_triangle(self):
        now = datetime.datetime.now()
        filename="image_{:%Y-%m-%d_%H-%M-%S}.png".format(now)
        default_dir = os.path.expanduser('triangle')
        # filename = filedialog.asksaveasfilename(
        #                                         initialdir=default_dir,
        #                                         initialfile=filename,
        #                                         defaultextension="png",
        #                                         filetypes=[("PNG","JPG"),(".png",".jpg")])
        filename = os.path.join(default_dir, filename)
        self.image.save(filename)

    def save_circle(self):
        now = datetime.datetime.now()
        filename="image_{:%Y-%m-%d_%H-%M-%S}.png".format(now)
        default_dir = os.path.expanduser('circle')
        # filename = filedialog.asksaveasfilename(
        #                                         initialdir=default_dir,
        #                                         initialfile=filename,
        #                                         defaultextension="png",
        #                                         filetypes=[("PNG","JPG"),(".png",".jpg")])
        filename = os.path.join(default_dir, filename)
        self.image.save(filename)


    def brush_plus(self):
        self.brush_width +=1

    def brush_minus(self):
        if self.brush_width>1:
            self.brush_width -=1

    # def change_color(self):
    #     pass
    def close(self):
        quitorsave=messagebox.askyesnocancel("Quit","Do you want to save your work?",parent=self.root)
        if quitorsave is not None:
            if quitorsave:
                self.save()
            self.root.destroy()
            exit(0)

PaintGUI()