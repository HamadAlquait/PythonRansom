from Tkinter import *

# Main part of the program that has the background and window sizes
root = Tk()
root.geometry("900x600")
root.title("This is a RansomWare Attack")
root.configure(background="black")




#This is the main banner at the top of the page
FirstHeading = Label(root, relief="raised", text="THIS IS A RANSOMWARE ATTACK ", font=("helvetica", 40, "bold"), bg="PURPLE",
                     fg="RED").pack()
#This is the text and submit box for the program
entering = Entry(root, width=80, relief="sunken").place(x=250, y=500, height=28)

#SUBMIT button that is listening to a users actions
button1 = Button(root, text="SUBMIT", fg="BLUE", relief="raised", bg="RED").place(x=750, y=500)


SideLabel = Label(root, text="HAHA").place(x=3, y=70, height=200)
MainLabel = Label(root, text="WHAT HAPPENED TO YOUR FILES", relief="sunken", width=90).place(x=250, y=80, height=320)

Timer_Countdown = Label(root, text="PLACEHOLDER TIMER", font=("times", 30, "bold"), fg="GREEN", bg="WHITE", width=20).place(x=200, y=420)
Chooser = Checkbutton(root, bg="BLUE", text="DECRYPT YOUR FILES").place(x=25, y=500);
Chooser2 = Checkbutton(root, bg="BLUE", text="AVOID BRICKING SYSTEM").place(x=25, y=520);
#update_time()




root.mainloop()
