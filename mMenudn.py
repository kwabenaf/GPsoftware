import os
import tkinter as tk
from tkinter import *
    
#defining Patient forms  
def vPatdn_form():
    print("Button clicked to show all Patients")
    mMenudn.destroy()
    os.system('python vPatdn.py')
    
def ePatmeddn_form():
    print("Button clicked to go to edit Patient form")
    mMenudn.destroy()
    os.system('python ePatmeddn.py')

def sPatdn_form():
    print("Button clicked to go to search Patient form")
    mMenudn.destroy()
    os.system('python sPatdn.py')
       
    
#defining Appointment forms
def aAppdn_form():
    print("Button clicked to show Appointment menu")
    mMenudn.destroy()
    os.system('python aAppdn.py')

def vAppdn_form():
    print("Button clicked to show all Appointments")
    mMenudn.destroy()
    os.system('python vAppdn.py')
    
def dAppdn_form():
    print("Button clicked to go to delete Appointment form")
    mMenudn.destroy()
    os.system('python dAppdn.py')
    
def eAppdn_form():
    print("Button clicked to go to edit Appointment form")
    mMenudn.destroy()
    os.system('python eAppdn.py')


#defining other forms
def mMenudn_form():
    print("Button clicked to go to Main Menu")
    mMenudn.destroy()
    os.system('python mMenudn.py')

def ePassdn_form():
    print("Button clicked to change password")
    mMenudn.destroy()
    os.system('python ePassdn.py')
    
def login_form():
    print("Button clicked to logout")
    mMenudn.destroy()
    os.system('python login.py')



#application dimensions
app_width = 300
app_height = 200


mMenudn = tk.Tk()
mMenudn.title('Main Menu')
mMenudn.configure(background='sea green')

#centers the app on the screen
screen_width = mMenudn.winfo_screenwidth()
screen_height = mMenudn.winfo_screenheight() 

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

mMenudn.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


#submenu labels and positioning
menu = Menu(mMenudn)
mMenudn.config(menu=menu)

homeSubmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Home", menu=homeSubmenu)
homeSubmenu.add_command(label="Menu", command = mMenudn_form)
homeSubmenu.add_separator()
homeSubmenu.add_command(label="Edit Password", command = ePassdn_form)
homeSubmenu.add_separator()
homeSubmenu.add_command(label="Log Out", command = login_form)
homeSubmenu.add_command(label="Exit", command = exit)

patientSubmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Patient", menu=patientSubmenu)
patientSubmenu.add_command(label="View Patients", command = vPatdn_form)
patientSubmenu.add_command(label="Edit Patient", command = ePatmeddn_form)
patientSubmenu.add_command(label="Search Patient", command = sPatdn_form)

appSubmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Appointment", menu=appSubmenu)
appSubmenu.add_command(label="View Appointments", command = vAppdn_form)
appSubmenu.add_command(label="Book Appointment", command = aAppdn_form)
appSubmenu.add_command(label="Cancel Appointment", command = dAppdn_form)
appSubmenu.add_command(label="Edit Appointment", command = eAppdn_form)

#labels and buttons
welcomeLabel = tk.Label(mMenudn, text="Welcome Doctor/Nurse", background="sea green", fg="black")
welcomeLabel.grid(row=0, column=2, columnspan=2)
welcomeLabel.place(x=110 ,y=0 )

btnPatientmenu = tk.Button(mMenudn, text="Patients", font="8", command = vPatdn_form)
btnPatientmenu.place(x=40 ,y=30 )

btnAppmenu = tk.Button(mMenudn, text="Appointments", font="8", command = vAppdn_form)
btnAppmenu.place(x=180 ,y=30 )

btnLogin = tk.Button(mMenudn, text="Log Out", font="8", command = login_form)
btnLogin.place(x=40 ,y=80 )


mMenudn.mainloop()


