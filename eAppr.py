import tkinter as tk
from tkinter import *
import sqlite3, time, datetime, random, os
staff_db='staff.db'
my_conn = sqlite3.connect(staff_db)
cdb = my_conn.cursor()

#defining Patient forms  
def aPatr_form():
    print("Button clicked to open add Patient form")
    eAppr.destroy()
    os.system('python aPatr.py')

def vPatr_form():
    print("Button clicked to show all Patients")
    eAppr.destroy()
    os.system('python vPatr.py')
    
def dPatr_form():
    print("Button clicked to go to delete Patient form")
    eAppr.destroy()
    os.system('python dPatr.py')
    
def ePatr_form():
    print("Button clicked to go to edit Patient form")
    eAppr.destroy()
    os.system('python ePatr.py')
    
    
#defining Appointment forms
def aAppr_form():
    print("Button clicked to show Appointment menu")
    eAppr.destroy()
    os.system('python aAppr.py')

def vAppr_form():
    print("Button clicked to show all Appointments")
    eAppr.destroy()
    os.system('python vAppr.py')
    
def dAppr_form():
    print("Button clicked to go to delete Appointment form")
    eAppr.destroy()
    os.system('python dAppr.py')
    
def eAppr_form():
    print("Button clicked to go to edit Appointment form")
    eAppr.destroy()
    os.system('python eAppr.py')


#defining other forms
def mMenur_form():
    print("Button clicked to go to Main Menu")
    eAppr.destroy()
    os.system('python mMenur.py')

def ePassr_form():
    print("Button clicked to change password")
    eAppr.destroy()
    os.system('python ePassr.py')
    
def login_form():
    print("Button clicked to logout")
    eAppr.destroy()
    os.system('python login.py')

    

app_width = 500
app_height = 600


eAppr = tk.Tk()
eAppr.title('Edit Appointment')
eAppr.configure(background='sea green')

screen_width = eAppr.winfo_screenwidth()
screen_height = eAppr.winfo_screenheight() 

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

eAppr.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

#submenu labels and positioning
menu = Menu(eAppr)
eAppr.config(menu=menu)

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

eAppr.mainloop()
