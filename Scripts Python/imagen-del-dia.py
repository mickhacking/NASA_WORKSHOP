import requests
import tkinter as tk
from PIL import Image, ImageTk

def obtener_imagen_apod():
    api_key = "fFdf5rcSxZXiMEK8LgAng0nOHOxKrcylhcnnZNWw"
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"
    
    try:
        response = requests.get(url)
        data = response.json()
        return data['url']
    except Exception as e:
        print("Error al obtener la imagen:", str(e))
        return None

def visualizar_imagen(url_imagen, title=""):
    root = tk.Tk()
    root.title(title)

    if url_imagen:
        image = Image.open(requests.get(url_imagen, stream=True).raw)
        image_widht = image.width // 2
        image_height = image.height // 2
        image = image.resize((image_widht, image_height))
        
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(root, image=photo)
        label.photo = photo
        label.pack()

    root.mainloop()

url_imagen = obtener_imagen_apod()
visualizar_imagen(url_imagen, "Visualizador de Imagen Astronómica del Día")
