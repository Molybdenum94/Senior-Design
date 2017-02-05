import tkinter
from tkinter import filedialog

# ***** Window Config *****
mainwindow = tkinter.Tk()
mainwindow.title("ATE/Verilog Translator")
mainwindow.geometry("400x320")
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
title = tkinter.Label(topFrame, text="Welcome to the ATE/Verilog Translator")
title.pack()
photo = tkinter.PhotoImage(file="images.gif")
L0 = tkinter.Label(topFrame, image=photo)
L0.pack()
L1 = tkinter.Label(frame1, text="Input File Path  ", padx=2)
L1.pack(side=tkinter.LEFT)
def getinput():
    mainwindow.inputfileName = filedialog.askopenfilename( filetypes = (("ATE files", "*.cpp"), ("Verilog files", "*.vams")))
    if mainwindow.inputfileName != '':
        inputtext.set(mainwindow.inputfileName)
inputtext = tkinter.StringVar()
B1 = tkinter.Button(frame1, command=getinput, relief=tkinter.SUNKEN, textvariable=inputtext)
inputtext.set("                                         ")
B1.pack(side=tkinter.LEFT)
spacer = tkinter.Label(space, text="           ")
spacer.pack()
L2 = tkinter.Label(frame2, text="Output File Path")
L2.pack(side=tkinter.LEFT)
def getoutput():
    mainwindow.outputfileName = filedialog.askdirectory()
    if mainwindow.outputfileName != '':
        outputtext.set(mainwindow.outputfileName)
outputtext = tkinter.StringVar()
B2 = tkinter.Button(frame2, command=getoutput, relief=tkinter.SUNKEN, textvariable=outputtext)
outputtext.set("                                         ")
B2.pack(side=tkinter.LEFT)
def helpmenu():
    menu = tkinter.Tk()
    menu.title("Help Menu")
helpbutton = tkinter.Button(frame3, text="Help", pady=15, command=helpmenu)
helpbutton.pack()

# ***** Main Function *****
def convert():
    button.destroy()
    button2 = tkinter.Button(frame3, text="Converting...", state=tkinter.DISABLED)
    button2.pack()

    #Put Code Here
        
button = tkinter.Button(frame3, text="Convert", command=convert)
button.pack()

mainwindow.mainloop()
