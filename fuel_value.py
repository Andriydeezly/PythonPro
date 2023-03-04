# "Росхід палива на 100 км"
#
# import tkinter as tk
#
# win = tk.Tk()
# win.geometry(f'950x500+100+200')
# win['bg'] = '#33ffe6'
# win.title('Шпіліанський росхід бензи')
#
# label_probig = tk.Label(win, text ="Пробіг (км)", font=('Arial', 15))
# label_probig.pack()
#
#
# win.mainloop()

import django
import requests as rec
import enum

class FuelType(enum.Enum):
    A95 = 'a95f'
    A95P = 'a95pf'
    A92 = 'a92f'
    Diesel = 'dtf'

def Milage(fuelPrice, distance, fuelPerKilometr):

    fuelLiters = distance/ fuelPerKilometr
    totalPrice = fuelLiters * fuelPrice
    return totalPrice

def getFuelPrice(fuelType):
    link = "https://auto.ria.com/content/news/templetify/fuel_price_page"
    data = rec.get(link).json()
    fuelList = data['buckets']
    for item in fuelList:
        return item[fuelType.value]['avg']



