import tkinter as tk
from generator import *

'''This is the version 0.5 of password generator app.
In this version a simple GUI has been created for the purpose of the program.
The user now interacts with the GUI instead the command window.
By Antonis Raftopoulos at 03.04.2020'''

#----CREATING THE MAIN ELEMENTS---
# create the main window
mw=tk.Tk()
mw.title("Password Generator v0.5") #main window title
mw.geometry("500x200") #main window size
#mainwindow.resizable(0,0) #no resizing window

# create the main frame of the window
mainframe=tk.Frame(mw)
mainframe.pack()

# creating the main frame label fields
tk.Label(mainframe,text="Service Name: ",anchor="e").grid(row=0,column=0)
tk.Label(mainframe,text="Service Website: ", anchor="e").grid(row=1,column=0)
tk.Label(mainframe,text="Your User Name: ", anchor="e").grid(row=2,column=0)
tk.Label(mainframe,text="Pasword Length (number of characters >=8): ", anchor="e").grid(row=3,column=0)

# creating the entry fields
a=tk.StringVar(mainframe, value="abc") #need to have an initial number of letters because it is not workingotherwise
servicenameEntry=tk.Entry(mainframe,textvariable=a)
b=tk.StringVar(mainframe, value="abc")#need to have an initial number of letters because it is not workingotherwise
sitenameEntry=tk.Entry(mainframe,textvariable=b)
c=tk.StringVar(mainframe, value="abc")#need to have an initial number of letters because it is not workingotherwise
usernameEntry=tk.Entry(mainframe,textvariable=c)
p=tk.IntVar(mainframe, value=8) #need this to get the password length as integer and not string
passlenEntry=tk.Entry(mainframe,textvariable=p)

servicenameEntry.grid(row=0, column=1)
sitenameEntry.grid(row=1,column=1)
usernameEntry.grid(row=2,column=1)
passlenEntry.grid(row=3, column=1)

#creating the last field for password before the generate button
#so we can use the function in the button
pswtext=tk.Label(mainframe,text="N/A")
pswtext.grid(row=6, column=1)

#------------------------------------------


#----Functions to Use----

#creating an instanse of the generator class to get the program started
#we will update the instanse when we fill the field of the password length and press the generate button
new_passwprd=Generator(int(passlenEntry.get()))
#this is the function to use to update the password by pressing the generate button
def passwordDisplay():
    from tkinter import messagebox
    try:
        if int(passlenEntry.get())<8:
            messagebox.showerror("Error", "Password should have at least 8 characters")
        else:
            passlen=int(passlenEntry.get())
            new_passwprd=Generator(passlen)
            pswtext["text"]=new_passwprd.pswrd()
    except:
        messagebox.showerror("Error", "Sorry, only numbers allowed (greater or equal to 8)")

#we use the get() in order to pass the fields texts as arguments to the method
def writetofile():
    from tkinter import messagebox
    new_passwprd.filewrite(servicenameEntry.get(),sitenameEntry.get(),usernameEntry.get(),pswtext["text"])
    messagebox.showinfo("Password Generated", "Password generated and  saved at Password.csv file")

def clear_text():
    servicenameEntry.delete(0,"end")
    sitenameEntry.delete(0,"end")
    usernameEntry.delete(0,"end")
    passlenEntry.delete(0,"end")
    pswtext["text"]="N/A"

#------------------------------------

#---Creating the buttons---
saveBTN=tk.Button(mainframe, text="SAVE",command=lambda:[writetofile(),clear_text()])
#using lambda here to use command with 2 functions
saveBTN.grid(row=4, column=0)

generateBTN=tk.Button(mainframe, text="Generate Password", command=passwordDisplay)
generateBTN.grid(row=4,column=1)

#displaying the password
tk.Label(mainframe,text=" ", anchor="e").grid(row=5,column=0) #leaving blank row
tk.Label(mainframe,text="Your Password is: ", anchor="e").grid(row=6,column=0)



mw.mainloop()
