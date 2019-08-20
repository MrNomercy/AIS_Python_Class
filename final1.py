# Animated Banner Program

#allows us to clear the console screen.
import os
import time

##Create a list of special characters and numbers.
special_sym = ["1","2","3","4","5","6","7","8","9","0",".",",","`","~","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}","\\","|",":",";","'","\"\"","<",">","?","/"]
##Create a function that will check if there is any characters in the above list.
def check_special_chars(myinput):
    mylist = list(myinput)
    for char in mylist:
        if char in special_sym:
            return True
            break
        else:
            pass

##Create a variable called my_input to get user message.
my_input=input("Enter Your Message : ")
##while loop that will keep running until user enter something.
while my_input == "":
    print("please enter something.") ## Error Message
    my_input=input("Enter Your Message : ")

##while loop that will run until no special characters, numbers or empty message were entered.
while check_special_chars(my_input):
    print("Please do not enter special or numuber.") ## Error Message
    my_input=input("Enter Your Message : ")
    while my_input == "":
        print("please enter something.") ##Error Message
        my_input=input("Enter Your Message : ")

#the width of the display
#(the windows console is 79 characters wide)
WIDTH = 79
##WIDTH = 5
##Change width to 5 and note down the changes.

#the message we want to print
message = my_input.upper()

#the printed banner version of the message
#this is a 7-line display, stored as 7 strings
#initially, these are empty.
printedMessage = [ "","","","","","","" ]

#a dictionary mapping letters to their 7-line
#banner display equivalents. each letter in the dictionary
#maps to 7 strings, one for each line of the display.
characters = { " " : [ " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " ",
                       " " ],

               "A" : [ "******",
                       "*    *",
                       "*    *",
                       "******",
                       "*    *",
                       "*    *",
                       "*    *"],
               
               "S" : [ "*****",
                       "*    ",
                       "*    ",
                       "*****",
                       "    *",
                       "    *",
                       "*****" ], 

               "N" : [ "*****   *",
                       "*   *   *",
                       "*   *   *",
                       "*   *   *",
                       "*   *   *",
                       "*   *   *",
                       "*   *****" ],

               "W" : [ "*    *    *",
                       "*    *    *",
                       "*    *    *",
                       "*    *    *",
                       "*    *    *",
                       "*    *    *",
                       "***********" ],

               "I" : [ "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  " ],

               "B" : [ "*******",
                       "*     *", 
                       "*     *",
                       "*******",
                       "*     *",
                       "*     *",
                       "*******" ],

               "C" : [ "*******",
                       "*      ",
                       "*      ",
                       "*      ",
                       "*      ",
                       "*      ",
                       "*******" ],
               "D" : [ "********",
                       "*      *",
                       "*      *",
                       "*      *",
                       "*      *",
                       "*      *",
                       "********" ],
               "E" : [ "*******",
                       "*      ",
                       "*      ",
                       "*******",
                       "*      ",
                       "*      ",
                       "*******" ],
               "F" : [ "*******",
                       "*      ",
                       "*      ",
                       "*******",
                       "*      ",
                       "*      ",
                       "*      " ],
               "G" : [ "*******",
                       "*      ",
                       "*      ",
                       "*  ****",
                       "*     *",
                       "*     *",
                       "*******" ],
               "H" : [ "*     *",
                       "*     *",
                       "*     *",
                       "*******",
                       "*     *",
                       "*     *",
                       "*     *" ],
               "J" : [ "*********",
                       "     *   ",
                       "     *   ",
                       "     *   ",
                       "     *   ",
                       "     *   ",
                       "******   " ],
               "K" : [ "*   *",
                       "*  * ",
                       "* *  ",
                       "**   ",
                       "* *  ",
                       "*  * ",
                       "*   *" ],
               "L" : [ "*      ",
                       "*      ",
                       "*      ",
                       "*      ",
                       "*      ",
                       "*      ",
                       "*******" ],
               "M" : [ "*     *",
                       "**   **",
                       "* * * *",
                       "*  *  *",
                       "*     *",
                       "*     *",
                       "*     *" ],
               "O" : [ " *** ",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       "*   *",
                       " *** " ],
               "P" : [ "*****",
                       "*   *",
                       "*   *",
                       "*****",
                       "*    ",
                       "*    ",
                       "*    " ],
               "Q" : [ "  *****  ",
                       " *     * ",
                       "*       *",
                       "*    *  *",
                       " *    ** ",
                       "   *** * ",
                       "        *" ],
               "R" : [ "******",
                       "*    *",
                       "*    *",
                       "******",
                       "* *   ",
                       "*   * ",
                       "*    *" ],
               "T" : [ "*****",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  " ],
               "U" : [ "*    *",
                       "*    *",
                       "*    *",
                       "*    *",
                       "*    *",
                       "*    *",
                       "******" ],
               "V" : [ "*        *",
                       "*        *",
                       " *       *",
                       "  *     * ",
                       "   *   *  ",
                       "    * *   ",
                       "     *    " ],
               "W" : [ "*     *",
                       "*     *",
                       "*     *",
                       "*  *  *",
                       "* * * *",
                       "**   **",
                       "*     *" ],
               "X" : [ "*     *",
                       " *   * ",
                       "  * *  ",
                       "   *   ",
                       "  * *  ",
                       " *   * ",
                       "*     *" ],
               "Y" : [ "*   *",
                       "*   *",
                       " * * ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  " ],
               "Z" : [ "*****",
                       "    *",
                       "    *",
                       "*****",
                       "*    ",
                       "*    ",
                       "*****" ],
               "'" : [ "  *  ",
                       "  *  ",
                       "  *  ",
                       "     ",
                       "     ",
                       "     ",
                       "     " ],
               "!" : [ "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "  *  ",
                       "     ",
                       "  *  " ],
               
               }



#build up the printed banner. to do this, the 1st row of the
#display is created for each character in the message, followed by
#the second line, etc..
for row in range(7):
    for char in message:
        printedMessage[row] += (str(characters[char][row]) + "  ")

#Create an absolute path.
my_path = "C:\\Users\\Admin\\Desktop\\my_ASCII.txt"
#Create a function called ASCII_art to store static banner in text file called my_ASCII.txt
def ASCII_art():
    try:
        myfile = open("my_ASCII.txt","w+")
    except:
        myfile = open(my_path,"w+")
    myfile.close()
    try:
        file = open("my_ASCII.txt","a+")
    except:
        file = open(my_path,"a+")
    for line in printedMessage:
        file.write(line)
        file.write("\n")
    file.close()

## using the function.
ASCII_art()



#the offset is how far to the right we want to print the message.
#initially, we want to print the message just off the display.
offset = WIDTH
while True:
    os.system("color a")
    os.system("cls")
    #print each line of the message, including the offset.
    for row in range(7):
        print(" " * offset + printedMessage[row][max(0,offset*-1):WIDTH - offset])
    #move the message a little to the left.
    offset -=1
    #if the entire message has moved 'through' the display then
    #start again from the right hand side.
    if offset <= ((len(message)+2)*6) * -1:
        offset = WIDTH
    #take out or change this line to speed up / slow down the display
    time.sleep(0.001)


