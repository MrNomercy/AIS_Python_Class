

import os
import time

##task 5: check special character and num
special_sym = ["1","2","3","4","5","6","7","8","9","0",".",",","`","~","@","#","$","%","^","&","*","(",")","-","_","=","+","[","]","{","}","\\","|",":",";","'","\"\"","<",">","?","/"]
def check_special(myinput):
    mylist = list(myinput)
    for i in mylist:
        if i in special_sym:
            return True
            break
        else:
            pass

##task comment, explain the changes and slide for presentation


## task3: get user input to print banner
name=input("Enter Your Message : ")
while name == "":
    print("please enter something.")
    name=input("Enter Your Message : ")

##task 5: check special characters, number and empty message
while check_special(name):
    print("Please do not enter special or numuber.")
    name=input("Enter Your Message : ")
    while name == "":
        print("please enter something.")
        name=input("Enter Your Message : ")

WIDTH = 79
##WIDTH = 5
##Task 1: change width to 5 and note down what happen?
##Then change back to 79 

message = name.upper()


printedMessage = [ "","","","","","","" ]


##Task 2: add more characters to dictionary
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



for row in range(7):
    for char in message:
        printedMessage[row] += (str(characters[char][row]) + "  ")

#task 4: save message in txt file
def ASCII_art():
    myfile = open("my_ASCII.txt","w+")
    myfile.close()
    file = open("my_ASCII.txt","a+")
    for line in printedMessage:
        file.write(line)
        file.write("\n")
    file.close()

ASCII_art()




offset = WIDTH
while True:
    os.system("color a")
    os.system("cls")
    for row in range(7):
        print(" " * offset + printedMessage[row][max(0,offset*-1):WIDTH - offset])
    offset -=1
    if offset <= ((len(message)+2)*6) * -1:
        offset = WIDTH
    time.sleep(0.05)


