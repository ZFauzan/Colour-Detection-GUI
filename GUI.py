import cv2    #pip install opencv-python
import tkinter as tk  #pip install tk
from tkinter import ttk, filedialog, Radiobutton,Button,Tk,StringVar 
from tkinter.messagebox import askretrycancel, showinfo
from PIL import Image, ImageTk
from subprocess import call

#contrast, brightness -> save edited pic
# camera

# primary, secondary, complementary color, 

#compare py code with matlab code

pic = None

root = tk.Tk()
frame = tk.Frame(root)
frame.grid(column=0, row=0)
root.title("App Name Placeholder")
root.geometry('640x400')

# configure the grid
#root.columnconfigure(0, weight=1)
#root.columnconfigure(1, weight=3)

choice1 = ttk.Label(root, text = "Get an Image: ")
choice1.grid(column=0, row=0, padx=10,pady=25,sticky="n")

def chooseFile():
    global pic
    filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
    (("jpeg files","*.jpg"),("all files","*.*")) )
    label = ttk.Label(root, text = "")
    label.configure(text = filename)
    pic = filename

chooseFileBtn = tk.Button(frame,
                  text="Browse For an Image",
                  width=25,
                  pady=10,
                  command=chooseFile)
chooseFileBtn.grid(column=0, row=2, padx=10,pady=25)

def camera():
    exec(open("camera.py").read())
    #root.destroy()

camera = tk.Button(frame,
                  text="Use Camera",
                  width=25,
                  pady=10,
                  command=camera)
camera.grid(column=1, row=2, padx=10,pady=25)

'''
button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   width=25,
                   pady=10,
                   command=quit)
    #button.place(x=90,y=90)
button.grid(column=0, row=0, sticky=tk.W, pady=15)
'''
choice1 = ttk.Label(root, text = "Analyze Your Image: ")
choice1.grid(column=0, row=0, padx=10,pady=25)

def noPic():
    answer = askretrycancel(
        title='Error Information',
        message='No image was selected. Do you want to retry?'
    )
    if answer:
        chooseFile()

def domCol():
    global pic
    """Enable scanning by setting the global flag to True."""   
    if pic != None:
        exec(open("dominantColors.py").read())
    else:
        noPic()

    #root.destroy()

domCol = tk.Button(frame,
                  text="Color Pallete",
                  width=25,
                  pady=10,
                  command=domCol)
domCol.grid(column=0, row=3, padx=10,pady=15)

def whichCol():
    global pic
    #root.destroy()
    if pic != None:
        exec(open("whichColor.py").read())
    else:
        noPic()

whichCol = tk.Button(frame,
                  text="Identify a Color",
                  width=25,
                  pady=10,
                  command=whichCol)
whichCol.grid(column=1, row=3, padx=10,pady=15)

#label_1 = tk.Label(frame, text="Identify a Color",width=20,font=("bold", 10))
#label_1.place(x=30,y=180)

##
palette_picker = tk.StringVar()
Com = Radiobutton(root, text='complementary', variable=palette_picker, value='S')
Tri = Radiobutton(root, text='triadic', variable=palette_picker, value='M')
Tet = Radiobutton(root, text='tetradic', variable=palette_picker, value='L')
#Ana = Radiobutton(root, text='analogous', variable=palette_picker, value='XL'),
#Neu = Radiobutton(root, text='neutral', variable=palette_picker, value='XXL'),
#Sha = Radiobutton(root, text='shades', variable=palette_picker, value='A'),
#Tin = Radiobutton(root, text='tints', variable=palette_picker, value='B'),
#Ton = Radiobutton(root, text='tones', variable=palette_picker, value='C')

Com.grid(column=0, row=7, padx=5, pady=5, sticky='w')
Tri.grid(column=0, row=8, padx=5, pady=5, sticky='w')
Tet.grid(column=0, row=9, padx=5, pady=5, sticky='w')

# label
label = ttk.Label(text="Related Colors")
label.grid(column=0, row=5, padx=5, pady=5)
##

root.mainloop()