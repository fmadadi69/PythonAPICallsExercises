import requests
import tkinter as tk
from PIL import ImageTk, Image
import urllib.request
import io
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def show_random_dog():
    re = requests.get('https://dog.ceo/api/breeds/image/random')
    row_data = urllib.request.urlopen(re.json()['message']).read()
    image = Image.open(io.BytesIO(row_data))
    dog_img1 = ImageTk.PhotoImage(image.resize((400,400), Image.Resampling.LANCZOS))
    label.configure(image=dog_img1)
    label.image = dog_img1


response = requests.get('https://dog.ceo/api/breeds/image/random')
row_data = urllib.request.urlopen(response.json()['message']).read()
image = Image.open(io.BytesIO(row_data))


window = tk.Tk()
window.title('Random Dogs')
window.geometry("600x600")

frame = tk.Frame(window, width=400, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

dog_img = ImageTk.PhotoImage(image.resize((400,400), Image.Resampling.LANCZOS))

label = tk.Label(frame, image=dog_img)
label.image = dog_img
label.pack()

random_button = tk.Button(window, text='New Random Dog', command=show_random_dog)
random_button.pack()
random_button.place(anchor='s', relx=0.5, rely=1)

window.mainloop()
