import tkinter as tk
from tkinter import filedialog, Text
import os

apps = []

def findbot():
    for widget in frame.winfo_children():
        widget.destroy()
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select file", filetypes = (("all files", "*.*"), ("executables", "*.exe")))
    apps.append(filename)
    print(filename)


    for app in apps:
        label = tk.Label(frame, text = app, bg ="gray")
        label.pack()
def runbot():
    for app in apps:
        os.startfile(app)



root = tk.Tk()
root.title("Kresent Enabler")
root.configure(bg = "red")
root.geometry("600x400")
#Introductory Text
mylabel = tk.Label(root, text= "Welcome to Kresent Enabler! This is an app that enables the Kresent bot by opening up a file finder dialog box!")
mylabel.pack()

#This creates a frame of white color in the Red window
frame = tk.Frame(root, bg = "white")
frame.place(relwidth = 0.8, relheight= 0.8, relx =0.1, rely = 0.1)

findbot = tk.Button(root, text = "Locate your bot", padx = 10, pady =5, fg = "white", bg = "black", command = findbot)
findbot.pack()
runbot = tk.Button(root, text = "Run The bot", padx = 10, pady =5, fg = "white", bg = "black", command = runbot)
runbot.pack()
root.mainloop()
