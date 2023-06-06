import requests
from datetime import datetime
from dateutil import tz
import tkinter as tk

response = requests.get('https://api.sunrise-sunset.org/json?lat=35.7219&lng=51.3347')
#print(response.json())
print(response.json()['results']['sunrise'])
print(response.json()['results']['sunset'])


from_zone = tz.tzutc()
to_zone = tz.tzlocal()
utc_sunrise = datetime.strptime(response.json()['results']['sunrise'], '%I:%M:%S %p').replace(tzinfo=from_zone)
tehran_sunrise = utc_sunrise.astimezone(to_zone).strftime('%I:%M:%S %p')

utc_sunset = datetime.strptime(response.json()['results']['sunset'], '%I:%M:%S %p').replace(tzinfo=from_zone)
tehran_sunset = utc_sunset.astimezone(to_zone).strftime('%I:%M:%S %p')

# print(f'Sunrise in Tehran is at : {tehran_sunrise}')
# print(f'Sunset in Tehran is at : {tehran_sunset}')

window = tk.Tk()
window.title('Sunrise/Sunset')
window.geometry("200x200")
greeting = tk.Label(window, text='Sunrise and Sunset Times')
city = tk.Label(text='For Tehran')
sunrise = tk.Label(text=f'Sunrise is at : {tehran_sunrise}')
sunset = tk.Label(text=f'Sunset is at : {tehran_sunset}')

greeting.pack()
city.pack()
sunrise.pack()
sunset.pack()

window.mainloop()
