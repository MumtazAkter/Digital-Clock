import tkinter as tk
from time import strftime
root = tk.Tk()
root.title("Digital Clock")
clock_label = tk.Label(root, font=("Helvetica", 48), background="black", foreground="cyan")
clock_label.pack(anchor="center")
def update_clock():
    current_time = strftime("%H:%M:%S %p")
    clock_label.config(text=current_time)
   
    clock_label.after(1000, update_clock)
update_clock()
root.mainloop()