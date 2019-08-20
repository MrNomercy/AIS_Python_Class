from tkinter import *
import tkinter.messagebox

window = Tk()
window.title('Roll Dice Game')
##window.geometry('500x500')
window.resizable(0,0)

#==================Function here=======================
def doSomething():
    print("hello")

def myExit():
    myexit=tkinter.messagebox.askquestion("warning","Are you sure want to close the App?")
    if myexit == 'yes':
        window.destroy()
    else:
        pass

def myRule():
    tkinter.messagebox.showinfo("Rule","The rule is very simple.\nOnly 2 button just click it.")

def myHelp():
    tkinter.messagebox.showinfo("Help","ONLY IDIOT NEED HELP!\nI hope you are not.")

def myAboutUs():
    tkinter.messagebox.showinfo("About Us","Author: Ricky\nDate:12 NOV 2018")
#======================================================
menuBar = Menu(window)
window.config(menu=menuBar)

playMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Play", menu=playMenu)
playMenu.add_command(label="Roll D1 x 6 times", command=doSomething)
playMenu.add_command(label="Roll D2 x 6 times", command=doSomething)
playMenu.add_command(label="Roll Both x 6 times", command=doSomething)
playMenu.add_command(label="Clear All", command=doSomething)
playMenu.add_separator()
playMenu.add_command(label="Exit",command=myExit)

supportMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Support", menu=supportMenu)
supportMenu.add_command(label="Rule", command=myRule)
supportMenu.add_command(label="Help", command=myHelp)
supportMenu.add_separator()
supportMenu.add_command(label="About Us", command=myAboutUs)

toolBar = Frame(window, bg="purple")
dice_1_button = Button(toolBar, text="Roll Dice 1", fg="white", bg="green",command=doSomething)
dice_1_button.pack(side=LEFT,padx=50,pady=10)
dice_2_button = Button(toolBar, text="Roll Dice 2", fg="white", bg="green",command=doSomething)
dice_2_button.pack(side=LEFT,padx=50,pady=10)
toolBar.pack(side=TOP,fill=X)

myCanvas = Canvas(window,width=400,height=200)
myCanvas.pack()
##middleLine = myCanvas.create_line(200,0,200,200,fill="orange")

text1 = Text(myCanvas,bg="cyan")
text2 = Text(myCanvas,bg="magenta")
text1.place(x=0,y=0)
text2.place(x=200,y=0)


toolBar = Frame(window, bg="blue")
dice_1_button = Button(toolBar, text="Clear Dice 1", fg="white", bg="red",command=doSomething)
dice_1_button.pack(side=LEFT,padx=50,pady=10)
dice_2_button = Button(toolBar, text="Clear Dice 2", fg="white", bg="red",command=doSomething)
dice_2_button.pack(side=LEFT,padx=50,pady=10)
toolBar.pack(side=BOTTOM,fill=X)
#====================mainloop==============================
window.mainloop()
