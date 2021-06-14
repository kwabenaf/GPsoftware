import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3, time, datetime, random, os
patient_db='patient.db'
my_conn = sqlite3.connect(patient_db)
cdb = my_conn.cursor()


#defining Patient forms  
def aPatr_form():
    print("Button clicked to open add Patient form")
    dPatr.destroy()
    os.system('python aPatr.py')

def vPatr_form():
    print("Button clicked to show all Patients")
    dPatr.destroy()
    os.system('python vPatr.py')
    
def dPatr_form():
    print("Button clicked to go to delete Patient form")
    dPatr.destroy()
    os.system('python dPatr.py')
    
def ePatr_form():
    print("Button clicked to go to edit Patient form")
    dPatr.destroy()
    os.system('python ePatr.py')
    
    
#defining Appointment forms
def aAppr_form():
    print("Button clicked to show Appointment menu")
    dPatr.destroy()
    os.system('python aAppr.py')

def vAppr_form():
    print("Button clicked to show all Appointments")
    dPatr.destroy()
    os.system('python vAppr.py')
    
def dAppr_form():
    print("Button clicked to go to delete Appointment form")
    dPatr.destroy()
    os.system('python dAppr.py')
    
def eAppr_form():
    print("Button clicked to go to edit Appointment form")
    dPatr.destroy()
    os.system('python eAppr.py')


#defining other forms
def mMenur_form():
    print("Button clicked to go to Main Menu")
    dPatr.destroy()
    os.system('python mMenur.py')

def ePassr_form():
    print("Button clicked to change password")
    dPatr.destroy()
    os.system('python ePassr.py')
    
def login_form():
    print("Button clicked to logout")
    dPatr.destroy()
    os.system('python login.py')
    

#Search patient to delete
def delete_record():
    
    recdel = recdelEntry.get()
    
    msgBox = tk.messagebox.askquestion ('Delete Patient Record','Are you sure you want to delete this patient',
                                        icon = 'warning')
    if msgBox == 'yes':   
        cdb.execute("DELETE FROM patientDb WHERE idno=?", (recdel,)) 
        print("Record " + str(recdel) + " Deleted ")
        my_conn.commit()
    else:
        tk.messagebox.showinfo('Return','Cancelled deletion')


#application dimensions
app_width = 300
app_height = 200


dPatr = tk.Tk()
dPatr.title('Delete Patients')
dPatr.configure(background='sea green')

screen_width = dPatr.winfo_screenwidth()
screen_height = dPatr.winfo_screenheight() 

#centers the app on the screen
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

dPatr.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

#submenu labels and positioning
menu = Menu(dPatr)
dPatr.config(menu=menu)

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

#title
titleLabel = tk.Label(dPatr, text="Delete Patient Records", background="sea green", fg="black", font='Helvetica 10 bold')
titleLabel.place(x=80, y=0)

#search label and entry
recdelLabel = tk.Label(dPatr, background="sea green", text="Enter Unique Patient ID:")
recdelEntry = tk.Entry(dPatr, relief="raised")
recdelLabel.place(x=15, y=60)
recdelEntry.place(x=150, y=62)
recdelbtn = tk.Button(dPatr, text="Delete", command=delete_record)
recdelbtn.place(x=120 ,y=90)

dPatr.mainloop()
