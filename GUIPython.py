import tkMessageBox
import ttk
from Tkinter import *
from PIL import Image, ImageTk
import time
import sys


# Main part of the program that has the background and window sizes
root = Tk()


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom



root.title("This is a RansomWare Attack")
root.configure(background="black")
root.overrideredirect(True)
tempkey = "JacobIsAGreatCoder"

def submit_function():
    count = 0
    while count < 1:
            tkMessageBox.showinfo("CHECKING KEY...", "FILES NOW DECRYPTED. THANK YOU!!!")
            count += 1
    exit()
root.overrideredirect(True)
tempkey = "Q1W2E3R4T5Y6U7I8O9P0123"

def submit_function():
    count = 0
    while count < 1:
            tkMessageBox.showinfo("CHECKING KEY...", "FILES NOW DECRYPTED. THANK YOU!!!")
            count += 1
    exit()

def Messages():
    global entering
    string = entering.get()
    if string == tempkey:

        print string
        tkMessageBox.showinfo("Checker", "YOUR FILES ARE NOW SAFE. THANK YOU!!!")
        exit()
    else:
        tkMessageBox.showerror("ERROR", "Your Key Entered Is Not Correct!! REMOVING TIME!!")


def submit_denied():
    tkMessageBox.showinfo("ACCESS DENIED", "KEY NOT VALID. TRY AGAIN!!!!")

def countdown_timer(self):
    counter = 25
 #   while counter > 0:

def ListRandomNumbers():
    scrolling = Scrollbar(root).place(x=100, y=70, height=350)
    ListBoxText = Listbox(root, height=2, width=15, bg="RED")
    ListBoxText.place(x=1, y=70)
    ListBoxText.insert(0, "000110101101010")
    ListBoxText.insert(0, "001010101001010")
    ListBoxText.insert(0, "110100101010010")
    #ListBoxText.insert(0, "42  70")
    #ListBoxText.place(x=3, y=70)
    #for random_numbers in [ListBoxText]:
        #ListBoxText.insert(END, random_numbers)


#This is the main banner at the top of the page
FirstHeading = Label(root, relief="raised", text="THIS IS A RANSOMWARE ATTACK ", font=("helvetica", 40, "bold"), bg="PURPLE",
                     fg="RED").pack()
#This is the text and submit box for the program
entering = Entry(root, width=80, relief="sunken")
entering.place(x=250, y=500, height=28)
entering.focus_set()

#SUBMIT button that is listening to a users actions
button1 = Button(root, text="SUBMIT", fg="BLUE", relief="raised", command=Messages,
            bg="RED").place(x=750, y=500)

#COUNTDOWNTIMER
timer = Label(root, font=("ARIAL", 40, "bold"), bg="RED", width=14).place(x=250, y=448, height=45)

#This is where the layers are for the designed image
ListRandomNumbers()

#CODE to display the description
DescriptionImage = Image.open("Capture.GIF")
tkimage = ImageTk.PhotoImage(DescriptionImage)
LabelIt = Label(root, image=tkimage, relief="sunken").pack()

#Bitcoin Image
BitcoinImage = Image.open("bitcoin.png")
BC = ImageTk.PhotoImage(BitcoinImage)
LabelIt2 = Label(root, image=BC, height=100)
LabelIt2.place(x=200, y=535)

#These are to display the check button boxes
Chooser = Checkbutton(root, bg="BLUE", text="DECRYPT YOUR FILES").place(x=25, y=500)
Chooser2 = Checkbutton(root, bg="BLUE", text="AVOID BRICKING SYSTEM").place(x=25, y=520)
Chooser3 = Checkbutton(root, bg="BLUE", text="PAY ME").place(x=25, y=540)
#update_time()

app=FullScreenApp(root)
root.mainloop()
