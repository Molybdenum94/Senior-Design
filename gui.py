import tkinter
import time
from tkinter import filedialog

# ***** Window Config *****
mainwindow = tkinter.Tk()
mainwindow.title("ATE/Verilog Translator")
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

# ***** Main Window Widgets *****
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
        mainwindow.inputtext.set(mainwindow.inputfileName)
mainwindow.inputtext = tkinter.StringVar()  #Contains the input file path
mainwindow.B1 = tkinter.Button(frame1, command=getinput, relief=tkinter.SUNKEN, textvariable=mainwindow.inputtext)
mainwindow.inputtext.set("                                         ")
mainwindow.B1.pack(side=tkinter.LEFT)
spacer = tkinter.Label(space, text="           ")
spacer.pack()
L2 = tkinter.Label(frame2, text="Output File Path")
L2.pack(side=tkinter.LEFT)
def getoutput():
    mainwindow.outputfilePath = filedialog.askdirectory()
    if mainwindow.outputfilePath != '':
        mainwindow.outputtext.set(mainwindow.outputfilePath)
mainwindow.outputtext = tkinter.StringVar() #Contains the output file path and name with proper extension
mainwindow.B2 = tkinter.Button(frame2, command=getoutput, relief=tkinter.SUNKEN, textvariable=mainwindow.outputtext)
mainwindow.outputtext.set("                                         ")
mainwindow.B2.pack(side=tkinter.LEFT)

# ***** Help Menu *****
def helpmenu():
    menu = tkinter.Tk()
    menu.title("Help Menu")
    menu.geometry('%dx%d+%d+%d' % (w, h, x+w, y))
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
    spacer1 = tkinter.Label(menu,
                            text=" ",
                            bg='white').pack()
    outputtitle = tkinter.Label(menu,
                                text="Output File Path:",
                                font="Helvetica 16 bold",
                                bg='white').pack()
    outputhelp1 = tkinter.Label(menu,
                                text="1. Click the box to the right of 'Output File Path' to open file explorer\n2. Select the DIRECTORY you want the output file to be in\n3. Click 'Choose'. The file path chosen will be displayed.",
                                justify=tkinter.LEFT,
                                font="Helvetica 12",
                                bg='white').pack()
    spacer2 = tkinter.Label(menu,
                            text=" ",
                            bg='white').pack()
    converttitle = tkinter.Label(menu,
                                text="Pressing the CONVERT button",
                                font="Helvetica 16 bold",
                                bg='white').pack()
    converthelp = tkinter.Label(menu,
                                text="1. A pop up should come up\n2. Enter the desired output filename (exclude the file extension)\n3. Click the DONE button to execute translation\n*Note: DONE button will not execute if entry is blank",
                                justify=tkinter.LEFT,
                                font="Helvetica 12",
                                bg='white').pack()
helpbutton = tkinter.Button(frame3, text="Help", pady=15, command=helpmenu)
helpbutton.pack()



# ********** MAIN FUNCTION **********
def main():
    #Put main function here
    time.sleep(3)





# ***** Program Execution Button and Widgets *****
def kill(error):
    error.destroy()
    
def done(getname):
    getname.grab_release()
    if mainwindow.outputname.get() != '' and not "." in mainwindow.outputname.get() and not "\\" in mainwindow.outputname.get() and not "/" in mainwindow.outputname.get() and not ":" in mainwindow.outputname.get() and not "*" in mainwindow.outputname.get() and not "?" in mainwindow.outputname.get() and not '"' in mainwindow.outputname.get() and not "<" in mainwindow.outputname.get() and not ">" in mainwindow.outputname.get() and not "|" in mainwindow.outputname.get():
        getname.destroy()
        if ".cpp" in mainwindow.inputtext.get():
            mainwindow.outputtext.set(mainwindow.outputfilePath+"/"+mainwindow.outputname.get()+".vams")
            convert()
        if ".vams" in mainwindow.inputtext.get():
            mainwindow.outputtext.set(mainwindow.outputfilePath+"/"+mainwindow.outputname.get()+".cpp")
            convert()
    else:
        error1 = tkinter.Toplevel()
        error1.configure(background='red')
        error1.attributes("-topmost", True)
        error1.title("Error")
        errormessage = tkinter.Label(error1, text="Please enter an output filename with no extension", font="Helvetica 16 bold", bg='red').pack()
        errorbutton = tkinter.Button(error1, text="OK",command= lambda: kill(error1)).pack()
        error1.grab_set()
    
def convert():
    mainwindow.B1.config(state="disabled")
    mainwindow.B2.config(state="disabled")
    mainwindow.button.destroy()
    mainwindow.button2 = tkinter.Button(frame3, text="Converting...", state=tkinter.DISABLED)
    mainwindow.button2.pack()
    mainwindow.update_idletasks()
    mainwindow.update()
    main()
    mainwindow.B1.config(state="active")
    mainwindow.B2.config(state="active")
    mainwindow.outputtext.set(mainwindow.outputfilePath)
    mainwindow.outputname.set("")
    mainwindow.button2.destroy()
    mainwindow.button = tkinter.Button(frame3, text="Convert", command=getoutputname)
    mainwindow.button.pack()
    mainwindow.update_idletasks()
    mainwindow.update()
    
def getoutputname():
    if mainwindow.inputtext.get() == '                                         ' or mainwindow.outputtext.get() == '                                         ':
        error2 = tkinter.Toplevel()
        error2.configure(background='red')
        error2.attributes("-topmost", True)
        error2.title("Error")
        errormessage = tkinter.Label(error2, text="****Please enter an input and output filepath****", font="Helvetica 20 bold", bg='red').pack()
        errorbutton = tkinter.Button(error2, text="OK",command= lambda: kill(error2)).pack()
        error2.grab_set()
        return
    getname = tkinter.Toplevel()
    getname.title("Output Filename")
    getname.geometry('%dx%d+%d+%d' % (w, h/2, x, y))
    outputfilename = tkinter.Label(getname,
                                   text="Enter the Output filename desired:",
                                   font="Helvetica 16 bold").pack()
    note = tkinter.Label(getname,
                         text="***** Note: Do not include file extension *****",
                         font="Helvetica 12").pack()
    mainwindow.outputname = tkinter.StringVar()
    outputentry = tkinter.Entry(getname, textvariable=mainwindow.outputname)
    outputentry.pack()
    convertbutton = tkinter.Button(getname, text="Done", pady=15, command= lambda: done(getname))
    convertbutton.pack()
    exitbutton = tkinter.Button(getname, text="Exit", command=getname.destroy)
    exitbutton.pack()
    getname.update_idletasks()
    getname.update()
    getname.grab_set()

       
mainwindow.button = tkinter.Button(frame3, text="Convert", command=getoutputname)
mainwindow.button.pack()
mainwindow.mainloop()
