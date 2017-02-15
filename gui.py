import tkinter
import time
from tkinter import filedialog

# ***** Window Config *****
mainwindow = tkinter.Tk()
mainwindow.title("ATE/Verilog Translator")
mainwindow.configure(background='white')
ws = mainwindow.winfo_screenwidth()
hs = mainwindow.winfo_screenheight()
w = ws/3
h = hs/2
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
mainwindow.geometry('%dx%d+%d+%d' % (w, h, x, y))
topFrame = tkinter.Frame(mainwindow)
topFrame.pack()
frame1 = tkinter.Frame(mainwindow)
frame1.pack()
space = tkinter.Frame(mainwindow)
space.pack()
frame2 = tkinter.Frame(mainwindow)
frame2.pack()
frame3 = tkinter.Frame(mainwindow)
frame3.pack()

# ***** Widgets *****
title = tkinter.Label(topFrame, bg='white', text="Welcome to the ATE/Verilog Translator")
title.pack()
photo = tkinter.PhotoImage(file="images.gif")
L0 = tkinter.Label(topFrame, image=photo, bg='white', bd=0)
L0.pack()
L1 = tkinter.Label(frame1, text="Input File Path  ", padx=2, bg='white', bd=0)
L1.pack(side=tkinter.LEFT)
def getinput():
    mainwindow.inputfileName = filedialog.askopenfilename( filetypes = (("ATE files", "*.cpp"), ("Verilog files", "*.vams")))
    if mainwindow.inputfileName != '':
        inputtext.set(mainwindow.inputfileName)
inputtext = tkinter.StringVar()
B1 = tkinter.Button(frame1, command=getinput, relief=tkinter.SUNKEN, textvariable=inputtext, bg='white', bd=0)
inputtext.set("                                         ")
B1.pack(side=tkinter.LEFT)
spacer = tkinter.Label(space, text="           ", bg='white', bd=0)
spacer.pack()
L2 = tkinter.Label(frame2, text="Output File Path", bg='white', bd=0)
L2.pack(side=tkinter.LEFT)
def getoutput():
    mainwindow.outputfilePath = filedialog.askdirectory()
    if mainwindow.outputfilePath != '':
        outputtext.set(mainwindow.outputfilePath)
outputtext = tkinter.StringVar()
B2 = tkinter.Button(frame2, command=getoutput, relief=tkinter.SUNKEN, textvariable=outputtext, bg='white', bd=0)
outputtext.set("                                         ")
B2.pack(side=tkinter.LEFT)
def helpmenu():
    menu = tkinter.Tk()
    menu.title("Help Menu")
    menu.geometry('%dx%d+%d+%d' % (w, h, x, y))
    menu.configure(background='white')
    inputtitle = tkinter.Label(menu,
                               text="Input File Path:",
                               font="Helvetica 16 bold",
                               bg='white').pack()
    inputhelp1 = tkinter.Label(menu,
                               text="1. Click the box to the right of 'Input File Path' to open file explorer\n2. Select the .cpp or .vams file you want to convert\n3. Click 'Open'. The file path chosen will be displayed.",
                               justify=tkinter.LEFT,
                               font="Helvetica 12",
                               bg='white').pack()
    spacer = tkinter.Label(menu,
                           text=" ",
                           bg='white').pack()
    outputtitle = tkinter.Label(menu,
                                text="Output File Path:",
                                font="Helvetica 16 bold",
                                bg='white').pack()
    outputhelp1 = tkinter.Label(menu,
                                text="1. Click the box to the right of 'Output File Path' to open file explorer\n2. Select the DIRECTORY you want the output file to be in\n3 Click 'Choose'. The file path chosen will be displayed.",
                                justify=tkinter.LEFT,
                                font="Helvetica 12",
                                bg='white').pack()
helpbutton = tkinter.Button(frame3, text="Help", pady=15, command=helpmenu, bg='white', bd=0)
helpbutton.pack()

# ***** Main Function *****
def convert():
    button.destroy()
    button2 = tkinter.Button(frame3, text="Converting...", state=tkinter.DISABLED)
    button2.pack()

    #Put Code Here
        
button = tkinter.Button(frame3, text="Convert", command=convert, bg='white', bd=0)
button.pack()

mainwindow.mainloop()
