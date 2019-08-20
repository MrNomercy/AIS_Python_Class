from tkinter import *
import tkinter.messagebox
import random

window = Tk()
window.title('Roll Dice Game')
##window.geometry('500x500')
window.resizable(0,0)
myList1=[]
myList2=[]

#==================Function here=======================
def doSomething():
    print("hello")

def Roll_D1():
    if len(myList1)<6:
        dice = random.randint(1,6)
        myList1.append(dice)
        text1.insert(INSERT,dice)
        text1.insert(INSERT,"\n")
    else:
        pass

def Roll_D2():
    if len(myList2)<6:
        dice = random.randint(1,6)
        myList2.append(dice)
        text2.insert(INSERT,dice)
        text2.insert(INSERT,"\n")
    else:
        pass

def Clear_D1():
    text1.delete('1.0',END)
    while myList1:
        myList1.pop()

def Clear_D2():
    text2.delete('1.0',END)
    while myList2:
        myList2.pop()

def Roll_D1_X6():
    while len(myList1)<6:
        dice = random.randint(1,6)
        myList1.append(dice)
        text1.insert(INSERT,dice)
        text1.insert(INSERT,"\n")

def Roll_D2_X6():
    while len(myList2)<6:
        dice = random.randint(1,6)
        myList2.append(dice)
        text2.insert(INSERT,dice)
        text2.insert(INSERT,"\n")

def Roll_Both():
    while len(myList1)<6:
        dice = random.randint(1,6)
        myList1.append(dice)
        text1.insert(INSERT,dice)
        text1.insert(INSERT,"\n")
    while len(myList2)<6:
        dice = random.randint(1,6)
        myList2.append(dice)
        text2.insert(INSERT,dice)
        text2.insert(INSERT,"\n")

def Clear_All():
    text1.delete('1.0',END)
    while myList1:
        myList1.pop()
    text2.delete('1.0',END)
    while myList2:
        myList2.pop()
    
def myExit():
    myexit=tkinter.messagebox.askquestion("warning","Are you sure want to close the App?")
    if myexit == 'yes':
        window.destroy()
    else:
        pass

def myRule():
    tkinter.messagebox.showinfo("Rule","The rule is very simple.\nJust click whatever you can.")

def myHelp():
    tkinter.messagebox.showinfo("Help","ONLY IDIOT NEED HELP!\nI hope you are not.")

def myAboutUs():
    tkinter.messagebox.showinfo("About Us","Author: Ricky\nDate:12 NOV 2018")
#======================================================
menuBar = Menu(window)
window.config(menu=menuBar)

playMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Play", menu=playMenu)
playMenu.add_command(label="Roll D1 x 6 times", command=Roll_D1_X6)
playMenu.add_command(label="Roll D2 x 6 times", command=Roll_D2_X6)
playMenu.add_command(label="Roll Both x 6 times", command=Roll_Both)
playMenu.add_command(label="Clear All", command=Clear_All)
playMenu.add_separator()
playMenu.add_command(label="Exit",command=myExit)

supportMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Support", menu=supportMenu)
supportMenu.add_command(label="Rule", command=myRule)
supportMenu.add_command(label="Help", command=myHelp)
supportMenu.add_separator()
supportMenu.add_command(label="About Us", command=myAboutUs)

toolBar = Frame(window, bg="purple")
dice_1_button = Button(toolBar, text="Roll Dice 1", fg="white", bg="green",command=Roll_D1)
dice_1_button.pack(side=LEFT,padx=50,pady=10)
dice_2_button = Button(toolBar, text="Roll Dice 2", fg="white", bg="green",command=Roll_D2)
dice_2_button.pack(side=LEFT,padx=50,pady=10)
toolBar.pack(side=TOP,fill=X)

myCanvas = Canvas(window,width=400,height=200)
myCanvas.pack()
##middleLine = myCanvas.create_line(200,0,200,200,fill="orange")

text1 = Text(myCanvas,bg="cyan")
text2 = Text(myCanvas,bg="magenta")
text1.place(x=0,y=0)
text2.place(x=200,y=0)

text1.config(font=('Arial', 16, 'bold'))
text2.config(font=('Arial', 16, 'bold'))

myNote = Label(window, text="Note: you can roll only 6 times, after that you need to clear.",bd=3, relief=SUNKEN,anchor=W)
myNote.pack(side=BOTTOM,fill=X)

toolBar = Frame(window, bg="blue")
dice_1_button = Button(toolBar, text="Clear Dice 1", fg="white", bg="red",command=Clear_D1)
dice_1_button.pack(side=LEFT,padx=50,pady=10)
dice_2_button = Button(toolBar, text="Clear Dice 2", fg="white", bg="red",command=Clear_D2)
dice_2_button.pack(side=LEFT,padx=50,pady=10)
toolBar.pack(side=BOTTOM,fill=X)


#====================mainloop==============================
window.mainloop()
