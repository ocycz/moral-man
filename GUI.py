import tkinter as tk
from PIL import Image, ImageTk
import time
import random
from variables import *

root = tk.Tk()

root.geometry('400x400')
root.title("GUI")

def name_gen():
    global randomName
    while True:
        randomName = random.choice(names)
        time.sleep(1)
        return randomName

count = 1
count2 = 0
stop = False

def start():
    button.destroy()
    play_icon_frames()
    label.grid(row = 0, column = 0, pady = 2)

def next():
    global label2
    label.destroy()
    label2 = tk.Label(root, text=f"{randomName} has no moral compass.", font=('Arial', 18))
    label2.grid(row=0, column=0, pady = 2)

def next2():
    global label3
    label2.destroy()
    label3 = tk.Label(root, text=f"That\'s where you come in.", font=('Arial', 18))
    label3.grid(row=0, column=0, pady = 2)

def destroy_label3():
    global stop
    stop = True
    label3.destroy()
    button2.destroy()
    icon.destroy()
    


def begin():
    global button2
    button2 = tk.Button(root, text="Begin", font=('Arial', 18), command=destroy_label3)
    button2.grid(row=2, column = 0)

def play_icon_frames():
    global count
    global count2
    global photo
    global icon
    global img
    if stop:
        count=0
        return None
    elif count == 1:
        photo = ImageTk.PhotoImage(img)
        icon = tk.Label(root, image=photo, width=300, height=300)
        icon.grid(row = 1, column = 0, pady = 2)
        count += 1
        count2 += 1
        print(count2)
        root.after(300, play_icon_frames)
    elif count == 2:
        photo = ImageTk.PhotoImage(img2)
        icon = tk.Label(root, image=photo)
        icon.grid(row = 1, column = 0, pady = 2)
        count += 1
        count2 += 1
        print(count2)
        root.after(300, play_icon_frames)
    else:
        photo = ImageTk.PhotoImage(img3)
        icon = tk.Label(root, image=photo)
        icon.grid(row = 1, column = 0, pady = 2)
        count = 1
        count2 += 1
        print(count2)
        if count2 == 9:
            print("finished")
            next()
        if count2 == 18:
            next2()
        if count2 == 24:
            begin()
        root.after(300, play_icon_frames)

label = tk.Label(root, text=f"This is {name_gen()}.", font=('Arial', 18))

img = Image.open(icons[0])
img2 = Image.open(icons[1])
img3 = Image.open(icons[2])
photo = ImageTk.PhotoImage(img)
icon = tk.Label(root, image=photo, width=300, height=300)



button = tk.Button(root, text="Start", font=('Arial', 18), command=start)
button.grid(row=2, column = 0)



root.mainloop()
