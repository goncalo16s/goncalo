###############################################################
#                   Written in Python 3.11.0                  #
#                                                             #
#                Copyright © 2022 Jelmar Orapa                #
###############################################################

from tkinter import *
from tkinter.ttk import *
import tkinter
import subprocess
import re
import sys
import tkinter.messagebox
import datetime

root = tkinter.Tk()
root.title("Wi-Fi Retriever By Jelmar Orapa")
root.geometry("514x300")
root.configure(bg='#F4F4F4')

# set colours
bg_colour = "#3d6466"
    
#Popup message
def onstart():
    tkinter.messagebox.showinfo("Welcome to Wi-Fi Retriever!",  "Please use with permission!")  



#Print Youtube Channel
def myYTchannel():
        import sys
        file = open('wifi.txt', 'a') 
        sys.stdout = file
        print("\nThank you for using this simple program! \nPlease support my Youtube Channel... \nhttps://www.youtube.com/@thetechinquirer5477 \nCopyright © 2022 Jelmar Orapa \n")
        now = datetime.datetime.now()
        print("Retrieved Date:", now)
        print("\n----------------Wi-Fi Password Retriever v4---------------- \n")
        file.close() 

#function to print subprocess on gui screen
def readwifi():
        f = open("wifi.txt", "r")
        wipass = f.read()
        text.insert(END, wipass)
        f.close()

# Group1 Frame ----------------------------------------------------
group1 = tkinter.LabelFrame(root, text="Wi-Fi Retriever v4", padx=5, pady=5)
group1.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky=tkinter.E+tkinter.W+tkinter.N+tkinter.S)

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

group1.rowconfigure(0, weight=1)
group1.columnconfigure((0,1), weight=1)

text = tkinter.Text(group1)
text.pack()

btn_Image = tkinter.Button(root, text='Retrieve Wi-Fi Passwords',
                           bg='gray', fg='white', font='Arial 10 bold',
                           command= lambda:[getwifi(), myYTchannel(), readwifi()])
btn_Image.grid(row=2, column=0, padx=(10), pady=10, sticky=tkinter.S)
btn_Image.config(width=23, height=1, bg=bg_colour)

#Centering on screen
root.eval('tk::PlaceWindow . center')

#Starting popup message
onstart()
#getwifi()
#readwifi()

#starting the application
root.mainloop()

###############################################################
#                   Written in Python 3.11.0                  #
#                                                             #
#                Copyright © 2022 Jelmar Orapa                #
###############################################################
