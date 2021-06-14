import tkinter as tk
from tkinter import *
import sqlite3, time, datetime, random, os
staff_db='staff.db'
my_conn = sqlite3.connect(staff_db)
cdb = my_conn.cursor()

#defining staff all forms
def aStaff_form():
    print("Button clicked to show add Staff form")
    eApp.destroy()
    os.system('python aStaff.py')

def vStaff_form():
    print("Button clicked to show all Staff members")
    eApp.destroy()
    os.system('python vStaff.py')
    
def dStaff_form():
    print("Button clicked to go to delete Staff form")
    eApp.destroy()
    os.system('python dStaff.py')
    
def eStaff_form():
    print("Button clicked to go to edit Staff form")
    eApp.destroy()
    os.system('python eStaff.py')
    
#defining Patient forms  
def aPat_form():
    print("Button clicked to open add Patient form")
    eApp.destroy()
    os.system('python aPat.py')

def vPat_form():
    print("Button clicked to show all Patients")
    eApp.destroy()
    os.system('python vPat.py')
    
def dPat_form():
    print("Button clicked to go to delete Patient form")
    eApp.destroy()
    os.system('python dPat.py')
    
def ePat_form():
    print("Button clicked to go to edit Patient form")
    eApp.destroy()
    os.system('python ePat.py')

def ePatmeddn_form():
    print("Button clicked to go to edit Patient medical records")
    eApp.destroy()
    os.system('python ePatmeddn.py')
    
#defining Appointment forms
def aApp_form():
    print("Button clicked to show Appointment menu")
    eApp.destroy()
    os.system('python aApp.py')

def vApp_form():
    print("Button clicked to show all Appointments")
    eApp.destroy()
    os.system('python vApp.py')
    
def dApp_form():
    print("Button clicked to go to delete Appointment form")
    eApp.destroy()
    os.system('python dApp.py')
    
def eApp_form():
    print("Button clicked to go to edit Appointment form")
    eApp.destroy()
    os.system('python eApp.py')


#defining other forms
def mMenu_form():
    print("Button clicked to go to Main Menu")
    eApp.destroy()
    os.system('python mMenu.py')

def editpass_form():
    print("Button clicked to change password")
    eApp.destroy()
    os.system('python editpass.py')
    
def login_form():
    print("Button clicked to logout")
    eApp.destroy()
    os.system('python login.py')

    

app_width = 500
app_height = 600


eApp = tk.Tk()
eApp.title('Edit Appointment')
eApp.configure(background='sea green')

screen_width = eApp.winfo_screenwidth()
screen_height = eApp.winfo_screenheight() 

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

eApp.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

#submenu labels and positioning
menu = Menu(eApp)
eApp.config(menu=menu)

homeSubmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Home", menu=homeSubmenu)
homeSubmenu.add_command(label="Menu", command = mMenu_form)
homeSubmenu.add_separator()
homeSubmenu.add_command(label="Edit Password", command = editpass_form)
homeSubmenu.add_separator()
homeSubmenu.add_command(label="Log Out", command = login_form)
homeSubmenu.add_command(label="Exit", command = exit)

patientSubmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Patient", menu=patientSubmenu)
patientSubmenu.add_command(label="View Patients", command = vPat_form)
patientSubmenu.add_command(label="Add Patient", command = aPat_form)
patientSubmenu.add_command(label="Edit Patient", command = ePat_form)
patientSubmenu.add_command(label="Delete Patient", command = dPat_form)


appSubmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Appointment", menu=appSubmenu)
appSubmenu.add_command(label="View Appointments", command = vApp_form)
appSubmenu.add_command(label="Book Appointment", command = aApp_form)
appSubmenu.add_command(label="Cancel Appointment", command = dApp_form)
appSubmenu.add_command(label="Edit Appointment", command = eApp_form)


staffSubmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Staff", menu=staffSubmenu)
staffSubmenu.add_command(label="View Staff", command = vStaff_form)
staffSubmenu.add_command(label="Add Staff", command = aStaff_form)
staffSubmenu.add_command(label="Edit Staff", command = eStaff_form)
staffSubmenu.add_command(label="Delete Staff", command = dStaff_form)



eApp.mainloop()