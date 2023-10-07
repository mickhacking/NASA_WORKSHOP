from tkinter import *

class GUI:
    def __init__(self, title, geometry=None):
        self.root = Tk()
        self.root.title = title
        if geometry != None:
            self.root.geometry(geometry)
    def __call__(self):
        self.main()    
    def main(self):
        self.root.mainloop()
    def frame(self, width, height):
        frame = Frame(self.root, width=width, height=height)
        frame.config(
            relief="solid"
        )
        return frame
    def add_title(self, text):
        text = self.add_text(text)
        text.config(
            font = ("Arial", 25),
            fg = "#000000"
        )
        return text
    def add_text(self, text):
        text = Label(self.root, text=text)
        return text
    def input(self):
        in_text = Entry(self.root)
        return in_text
    def button(self, text):
        btn = Button(self.root, text=text)
        return btn

gui = GUI("Test", "400x400")
gui.add_title("Mars Weather").pack()


day = 0
gui.add_text("Day:").pack(anchor=W)
gui.input().pack(anchor=W)

month = 0
gui.add_text("Month:").pack(anchor=W)
gui.input().pack(anchor=W)

year = 0
gui.add_text("Year:").pack(anchor=W)
gui.input().pack(anchor=W)

def hola():
    print("Hola Mundo")
gui.frame(15, 15).pack()
btn = gui.button("Consultar")
btn.command = hola()
btn.pack(anchor=W)

gui()
        