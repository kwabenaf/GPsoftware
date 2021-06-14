import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3, time, datetime, random, os
patient_db='patient.db'
my_conn = sqlite3.connect(patient_db)
cdb = my_conn.cursor()


#defining staff all forms
def aStaff_form():
    print("Button clicked to show add Staff form")
    dPat.destroy()
    os.system('python aStaff.py')

def vStaff_form():
    print("Button clicked to show all Staff members")
    dPat.destroy()
    os.system('python vStaff.py')
    
def dStaff_form():
    print("Button clicked to go to delete Staff form")
    dPat.destroy()
    os.system('python dStaff.py')
    
def eStaff_form():
    print("Button clicked to go to edit Staff form")
    dPat.destroy()
    os.system('python eStaff.py')
    
#defining Patient forms  
def aPat_form():
    print("Button clicked to open add Patient form")
    dPat.destroy()
    os.system('python aPat.py')

def vPat_form():
    print("Button clicked to show all Patients")
    dPat.destroy()
    os.system('python vPat.py')
    
def dPat_form():
    print("Button clicked to go to delete Patient form")
    dPat.destroy()
    os.system('python dPat.py')
    
def ePat_form():
    print("Button clicked to go to edit Patient form")
    dPat.destroy()
    os.system('python ePat.py')

def ePatmeddn_form():
    print("Button clicked to go to edit Patient medical records")
    ePat.destroy()
    os.system('python ePatmeddn.py')
    
#defining Appointment forms
def aApp_form():
    print("Button clicked to show Appointment menu")
    dPat.destroy()
    os.system('python aApp.py')

def vApp_form():
    print("Button clicked to show all Appointments")
    dPat.destroy()
    os.system('python vApp.py')
    
def dApp_form():
    print("Button clicked to go to delete Appointment form")
    dPat.destroy()
    os.system('python dApp.py')
    
def eApp_form():
    print("Button clicked to go to edit Appointment form")
    dPat.destroy()
    os.system('python eApp.py')


#defining other forms
def mMenu_form():
    print("Button clicked to go to Main Menu")
    dPat.destroy()
    os.system('python mMenu.py')

def editpass_form():
    print("Button clicked to change password")
    dPat.destroy()
    os.system('python editpass.py')
    
def login_form():
    print("Button clicked to logout")
    dPat.destroy()
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


dPat = tk.Tk()
dPat.title('Delete Patients')
dPat.configure(background='sea green')

#centers the app on the screen
screen_width = dPat.winfo_screenwidth()
screen_height = dPat.winfo_screenheight() 

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

dPat.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

#submenu labels and positioning
menu = Menu(dPat)
dPat.config(menu=menu)

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

#title
titleLabel = tk.Label(dPat, text="Delete Patient Records", background="sea green", fg="black", font='Helvetica 10 bold')
titleLabel.place(x=80, y=0)

#search label and entry
recdelLabel = tk.Label(dPat, background="sea green", text="Enter Unique Patient ID:")
recdelEntry = tk.Entry(dPat, relief="raised")
recdelLabel.place(x=15, y=60)
recdelEntry.place(x=150, y=62)
recdelbtn = tk.Button(dPat, text="Delete", command=delete_record)
recdelbtn.place(x=120 ,y=90)

dPat.mainloop()