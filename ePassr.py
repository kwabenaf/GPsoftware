import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3, os
staff_db ='staff.db'
my_conn = sqlite3.connect(staff_db)
cdb = my_conn.cursor()

#defining Patient forms  
def aPatr_form():
    print("Button clicked to open add Patient form")
    ePassr.destroy()
    os.system('python aPatr.py').pack()

def vPatr_form():
    print("Button clicked to show all Patients")
    ePassr.destroy()
    os.system('python vPatr.py').pack()
    
def dPatr_form():
    print("Button clicked to go to delete Patient form")
    ePassr.destroy()
    os.system('python dPatr.py').pack()
    
def ePatr_form():
    print("Button clicked to go to edit Patient form")
    ePassr.destroy()
    os.system('python ePatr.py').pack()
    
    
#defining Appointment forms
def aAppr_form():
    print("Button clicked to show Appointment menu")
    ePassr.destroy()
    os.system('python aAppr.py').pack()

def vAppr_form():
    print("Button clicked to show all Appointments")
    ePassr.destroy()
    os.system('python vAppr.py').pack()
    
def dAppr_form():
    print("Button clicked to go to delete Appointment form")
    ePassr.destroy()
    os.system('python dAppr.py').pack()
    
def eAppr_form():
    print("Button clicked to go to edit Appointment form")
    ePassr.destroy()
    os.system('python eAppr.py').pack()


#defining other forms
def mMenur_form():
    print("Button clicked to go to Main Menu")
    ePassr.destroy()
    os.system('python mMenur.py').pack()

def ePassr_form():
    print("Button clicked to change password")
    ePassr.destroy()
    os.system('python ePassr.py').pack()
    
def login_form():
    print("Button clicked to logout")
    ePassr.destroy()
    os.system('python login.py').pack()

#setting form size        
app_width = 300
app_height = 200

ePassr = Tk()
ePassr.title("Edit Password")
ePassr.configure(background='sea green')

#centering the form
screen_width = ePassr.winfo_screenwidth()
screen_height = ePassr.winfo_screenheight() 

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)



ePassr.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

#submenu labels and positioning
menu = Menu(ePassr)
ePassr.config(menu=menu)

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


#edit password label and entry
changeLabel = tk.Label(ePassr, text="Change Password", background="dark sea green", fg="black")
changeLabel.place(x=20, y=40)

changeEntry = tk.Entry(ePassr, relief="groove")
changeEntry.place(x=140, y=40)

submitbtn = tk.Button(ePassr, text="Confirm", height = 2, width = 13).place(x=100, y=100)

ePassr.mainloop()
