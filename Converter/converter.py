import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image

root = Tk()
root.title("PNG to JPG converter")
class ResizingCanvas(Canvas):
    def __init__(self,parent,**kwargs):
        Canvas.__init__(self,parent,**kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self,event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width)/self.width
        hscale = float(event.height)/self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all",0,0,wscale,hscale)



def main():

    myframe = Frame(root)
    myframe.pack(fill=BOTH, expand=YES)
    mycanvas = ResizingCanvas(myframe,width=350, height=200, bg="black", highlightthickness=0)
    mycanvas.pack(fill=BOTH, expand=YES)
    label1 = tk.Label(root, text="File conversion tool")
    label1.config(font=('helvetica', 20))
    mycanvas.create_window(175,40, window = label1)
    BrowseButton_PNG = tk.Button(text = "     Import PNG File     ",
    command = getPNG, bg='green', fg='white', font=('helvetica', 12))
    mycanvas.create_window(175,80, window =BrowseButton_PNG)
    SaveAsButton_JPG = tk.Button(text = "     Convert PNG To JPG     ",
    command = ConvertToJPG, bg='green', fg='white', font=('helvetica', 12))
    mycanvas.create_window(175,120, window = SaveAsButton_JPG)
    root.mainloop()

def getPNG():

    global im1

    import_file_path = filedialog.askopenfilename()
    im1 = Image.open(import_file_path)

def ConvertToJPG():

    global im1
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    im1.save(export_file_path)

if __name__ == "__main__":
    main()
    

