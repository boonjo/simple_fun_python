import psutil, time
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

while True:
    battery = psutil.sensors_battery()
    if getattr(battery, 'percent') >= 95 and getattr(battery, 'power_plugged'):
        messagebox.showinfo(message='🔋 Battery is charged to full, unplug the charger 🔋', parent=root)
    time.sleep(20)
    