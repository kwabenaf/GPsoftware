import os
import tkinter as tk
from tkinter import *
    
#defining Patient forms  
def aPatr_form():
    print("Button clicked to open add Patient form")
    mMenur.destroy()
    os.system('python aPatr.py')

def vPatr_form():
    print("Button clicked to show all Patients")
    mMenur.destroy()
    os.system('python vPatr.py')
    
def dPatr_form():
    print("Button clicked to go to delete Patient form")
    mMenur.destroy()
    os.system('python dPatr.py')
    
def ePatr_form():
    print("Button clicked to go to edit Patient form")
    mMenur.destroy()
    os.system('python ePatr.py')
    
    
#defining Appointment forms
def aAppr_form():
    print("Button clicked to show Appointment menu")
    mMenur.destroy()
    os.system('python aAppr.py')

def vAppr_form():
    print("Button clicked to show all Appointments")
    mMenur.destroy()
    os.system('python vAppr.py')
    
def dAppr_form():
    print("Button clicked to go to delete Appointment form")
    mMenur.destroy()
    os.system('python dAppr.py')
    
def eAppr_form():
    print("Button clicked to go to edit Appointment form")
    mMenur.destroy()
    os.system('python eAppr.py')


#defining other forms
def mMenur_form():
    print("Button clicked to go to Main Menu")
    mMenur.destroy()
    os.system('python mMenur.py')

def ePassr_form():
    print("Button clicked to change password")
    mMenur.destroy()
    os.system('python ePassr.py')
    
def login_form():
    print("Button clicked to logout")
    mMenur.destroy()
    os.system('python login.py')



#application dimensions
app_width = 300
app_height = 200



mMenur = tk.Tk()
mMenur.title('Main Menu')
mMenur.configure(background='sea green')

#centers the app on the screen
screen_width = mMenur.winfo_screenwidth()
screen_height = mMenur.winfo_screenheight() 

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

mMenur.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

#submenu labels and positioning
menu = Menu(mMenur)
mMenur.config(menu=menu)

homeSubmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Home", menu=homeSubmenu)
homeSubmenu.add_command(label="Menu", command = mMenur_form)
homeSubmenu.add_separator()
homeSubmenu.add_command(label="Edit Password", command = ePassr_form)
homeSubmenu.add_separator()
homeSubmenu.add_command(label="Log Out", command = login_form)
homeSubmenu.add_command(label="Exit", command = exit)

patientSubmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Patient", menu=patientSubmenu)
patientSubmenu.add_command(label="View Patients", command = vPatr_form)
patientSubmenu.add_command(label="Add Patient", command = aPatr_form)
patientSubmenu.add_command(label="Edit Patient", command = ePatr_form)
patientSubmenu.add_command(label="Delete Patient", command = dPatr_form)

appSubmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Appointment", menu=appSubmenu)
appSubmenu.add_command(label="View Appointments", command = vAppr_form)
appSubmenu.add_command(label="Book Appointment", command = aAppr_form)
appSubmenu.add_command(label="Cancel Appointment", command = dAppr_form)
appSubmenu.add_command(label="Edit Appointment", command = eAppr_form)

#labels and buttons
welcomeLabel = tk.Label(mMenur, text="Welcome Receptionist", background="sea green", fg="black")
welcomeLabel.grid(row=0, column=2, columnspan=2)
welcomeLabel.place(x=110 ,y=0 )

btnPatientmenu = tk.Button(mMenur, text="Patients", font="8", command = vPatr_form)
btnPatientmenu.place(x=40 ,y=30 )

btnAppmenu = tk.Button(mMenur, text="Appointments", font="8", command = vAppr_form)
btnAppmenu.place(x=180 ,y=30 )

btnLogin = tk.Button(mMenur, text="Log Out", font="8", command = login_form)
btnLogin.place(x=40 ,y=80 )


mMenur.mainloop()


