from requests import get
from tkinter import Tk, Label, Entry, Button, Frame, CENTER, W
from pyladies.settings import TOKEN

class Asteroids:
    def __init__(self):
        self.root = Tk()
        self.root.title = "Asteroides Cercanos"
        self.root.geometry("500x400")
        self.header()
        self.form_frame = Frame()
        self.form_frame.pack(pady=20)
        self.day = Entry(self.form_frame)
        self.month = Entry(self.form_frame)
        self.year = Entry(self.form_frame)
  
    def  __call__(self):
        self.root.mainloop()
        
    def restart(self):
        self.root.destroy()
        self.__init__()
        
    def header(self):
        text = Label(self.root, text="Asteroides Cercanos")
        text.config(
            font = ("Arial", 25),
            width=500,
            bg="#134394",
            fg = "#FFFFFF"
        )
        text.pack(anchor=CENTER)
        
    def label(self, text):
        label = Label(self.form_frame, text=text)
        label.config(font = ("Arial", 16))
        return label
     
    def form(self):
        self.label("Day").pack(anchor=W, pady=5)
        self.day.config(
            font = ("Arial", 16)
        )
        self.day.pack(anchor=W)
        self.label("Month").pack(anchor=W, pady=5)
        self.month.config(
            font = ("Arial", 16)
        )
        self.month.pack(anchor=W)
        self.label("Year:").pack(anchor=W, pady=5)
        self.year.config(
            font = ("Arial", 16)
        )
        self.year.pack(anchor=W)
        self.button()
        
    def button(self):
        btn = Button(self.form_frame, text="Buscar", command=self.asteroid)
        btn.config(
            font = ("Arial", 14),
        )
        btn.config(
            bg="#134394",
            fg="#FFFFFF",
            activebackground="#f30a0d",
            activeforeground="#FFFFFF"
        )
        btn.pack(anchor=CENTER, pady=15)
        
    def asteroid(self):
        DATE = self.get_date()
        URL = "https://api.nasa.gov/neo/rest/v1/feed?"
        PATH = f"start_date={DATE}&end_date={DATE}&api_key={TOKEN}"
        print(URL, PATH)
        data = get(URL+PATH).json()
        self.restart()
        self.label(f"El número de asteroides cercanos a la Tierra el {DATE} es: {data['element_count']}").pack(anchor=W, pady=5)
        self.label(f"Los nombres, IDs y distancias mínimas de los asteroides son:").pack(anchor=W, pady=5)
        for asteroid in data["near_earth_objects"][DATE]:
            name = asteroid["name"]
            id = asteroid["id"]
            distance = asteroid["close_approach_data"][0]["miss_distance"]["kilometers"]
            self.label(f"- {name} ({id}): {distance} km").pack(anchor=W, pady=5)
        
        
    def get_date(self):
        day = self.day.get()
        month = self.month.get()
        year = self.year.get()
        return "{}-{}-{}".format(year, month, day)
    

if __name__ == "__main__":
    asteroids = Asteroids()
    asteroids.form()
    asteroids()
