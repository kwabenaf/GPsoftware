import tkinter as tk
from tkinter import *
import sqlite3, time, datetime, random, os
staff_db='staff.db'
my_conn = sqlite3.connect(staff_db)
cdb = my_conn.cursor()

#defining Patient forms  
def vPatdn_form():
    print("Button clicked to show all Patients")
    dAppdn.destroy()
    os.system('python vPatdn.py')
    
def ePatmeddn_form():
    print("Button clicked to go to edit Patient form")
    dAppdn.destroy()
    os.system('python ePatmeddn.py')

def sPatdn_form():
    print("Button clicked to go to search Patient form")
    dAppdn.destroy()
    os.system('python sPatdn.py')
       
    
#defining Appointment forms
def aAppdn_form():
    print("Button clicked to show Appointment menu")
    dAppdn.destroy()
    os.system('python aAppdn.py')

def vAppdn_form():
    print("Button clicked to show all Appointments")
    dAppdn.destroy()
    os.system('python vAppdn.py')
    
def dAppdn_form():
    print("Button clicked to go to delete Appointment form")
    dAppdn.destroy()
    os.system('python dAppdn.py')
    
def eAppdn_form():
    print("Button clicked to go to edit Appointment form")
    dAppdn.destroy()
    os.system('python eAppdn.py')


#defining other forms
def mMenudn_form():
    print("Button clicked to go to Main Menu")
    dAppdn.destroy()
    os.system('python mMenudn.py')

def ePassdn_form():
    print("Button clicked to change password")
    dAppdn.destroy()
    os.system('python ePassdn.py')
    
def login_form():
    print("Button clicked to logout")
    dAppdn.destroy()
    os.system('python login.py')

    
app_width = 500
app_height = 600


dAppdn = tk.Tk()
dAppdn.title('Cancel Appointment')
dAppdn.configure(background='sea green')

screen_width = dAppdn.winfo_screenwidth()
screen_height = dAppdn.winfo_screenheight() 

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

dAppdn.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

#submenu labels and positioning
menu = Menu(dAppdn)
dAppdn.config(menu=menu)

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



dAppdn.mainloop()
