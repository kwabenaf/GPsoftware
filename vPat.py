import tkinter as tk
from tkinter import *
import sqlite3, time, datetime, random, os
patient_db='patient.db'
my_conn = sqlite3.connect(patient_db)
cdb = my_conn.cursor()


#defining staff all forms
def aStaff_form():
    print("Button clicked to show add Staff form")
    vPat.destroy()
    os.system('python aStaff.py')

def vStaff_form():
    print("Button clicked to show all Staff members")
    vPat.destroy()
    os.system('python vStaff.py')
    
def dStaff_form():
    print("Button clicked to go to delete Staff form")
    vPat.destroy()
    os.system('python dStaff.py')
    
def eStaff_form():
    print("Button clicked to go to edit Staff form")
    vPat.destroy()
    os.system('python eStaff.py')
    
#defining Patient forms  
def aPat_form():
    print("Button clicked to open add Patient form")
    vPat.destroy()
    os.system('python aPat.py')

def vPat_form():
    print("Button clicked to show all Patients")
    vPat.destroy()
    os.system('python vPat.py')
    
def dPat_form():
    print("Button clicked to go to delete Patient form")
    vPat.destroy()
    os.system('python dPat.py')
    
def ePat_form():
    print("Button clicked to go to edit Patient form")
    vPat.destroy()
    os.system('python ePat.py')

def ePatmeddn_form():
    print("Button clicked to go to edit Patient medical records")
    vPat.destroy()
    os.system('python ePatmeddn.py')
    
#defining Appointment forms
def aApp_form():
    print("Button clicked to show Appointment menu")
    vPat.destroy()
    os.system('python aApp.py')

def vApp_form():
    print("Button clicked to show all Appointments")
    vPat.destroy()
    os.system('python vApp.py')
    
def dApp_form():
    print("Button clicked to go to delete Appointment form")
    vPat.destroy()
    os.system('python dApp.py')
    
def eApp_form():
    print("Button clicked to go to edit Appointment form")
    vPat.destroy()
    os.system('python eApp.py')


#defining other forms
def mMenu_form():
    print("Button clicked to go to Main Menu")
    vPat.destroy()
    os.system('python mMenu.py')

def editpass_form():
    print("Button clicked to change password")
    vPat.destroy()
    os.system('python editpass.py')
    
def login_form():
    print("Button clicked to logout")
    vPat.destroy()
    os.system('python login.py')

 
#clear entries
def eclear():
    sNameEntry.delete(0, END)

#search
def querySurname():
    
    tableLabel.place_forget()
    
    sName = sNameEntry.get()
    print("Button clicked to query surname - searched for surname: " + sName) 
    
    data_set=my_conn.execute("SELECT * FROM patientDb WHERE surname=?", (sName,)) 
    sOutput_data(data_set,stableLabel)
    eclear()
    

def viewall():
    stableLabel.place_forget()
    tableLabel
    tableLabel.place(x=50, y=180)

def sOutput_data(data_set,stableLabel):
    i=0 # row value inside the loop 
    for person in data_set: 
        for j in range(len(person)):
            e = Entry(stableLabel, width=12, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, person[j])
            e['state'] = 'readonly'
        i=i+1
    return stableLabel


def output_data(data_set,tableLabel):
    i=0 # row value inside the loop 
    for person in data_set: 
        for j in range(len(person)):
            e = Entry(tableLabel, width=12, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, person[j])
            e['state'] = 'readonly'
        i=i+1
    return tableLabel    


    
#application dimensions   
app_width = 700
app_height = 600


vPat = tk.Tk()
vPat.title('View Patients')
vPat.configure(background='sea green')

#centers the app on the screen
screen_width = vPat.winfo_screenwidth()
screen_height = vPat.winfo_screenheight() 

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

vPat.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

data_set=my_conn.execute("SELECT * FROM patientDb")

#submenu labels and positioning
menu = Menu(vPat)
vPat.config(menu=menu)

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
titleLabel = tk.Label(vPat, text="Patient Records", background="sea green", fg="black", font='Helvetica 12 bold')
titleLabel.place(x=300, y=0)

#table names
idLabel = tk.Label(vPat, text = "ID", background="sea green", fg="black", font='Helvetica 8 bold')
idLabel.place(x=85 , y=160)

fnameLabel = tk.Label(vPat, text = "Firstname", background="sea green", fg="black", font='Helvetica 8 bold')
fnameLabel.place(x=150 , y=160)

snameLabel = tk.Label(vPat, text = "Surname", background="sea green", fg="black", font='Helvetica 8 bold')
snameLabel.place(x=210 , y=160)

dobLabel = tk.Label(vPat, text = "DoB", background="sea green", fg="black", font='Helvetica 8 bold')
dobLabel.place(x=290 , y=160)

addressLabel = tk.Label(vPat, text = "Address", background="sea green", fg="black", font='Helvetica 8 bold')
addressLabel.place(x=360 , y=160)

genLabel = tk.Label(vPat, text = "Gender", background="sea green", fg="black", font='Helvetica 8 bold')
genLabel.place(x=440 , y=160)

phoneLabel = tk.Label(vPat, text = "Phone no.", background="sea green", fg="black", font='Helvetica 8 bold')
phoneLabel.place(x=530 , y=160)

emailLabel = tk.Label(vPat, text = "Email", background="sea green", fg="black", font='Helvetica 8 bold')
emailLabel.place(x=600 , y=160)

tableLabel = tk.Label(vPat, background="sea green", fg="black")
tableLabel.place(x=50, y=180)

stableLabel = tk.Label(vPat, background="sea green", fg="black")
stableLabel.place(x=50, y=180)

#view all button
vallbtn = tk.Button(vPat, text="View All", command=viewall)
vallbtn.place(x=330 ,y=30)

#search label and entry
sNameLabel = tk.Label(vPat, background="sea green", text="Search Surname:")
sNameEntry = tk.Entry(vPat, relief="raised")
sNameLabel.place(x=30 ,y=60)
sNameEntry.place(x=130, y=62)
sNamebtn = tk.Button(vPat, text="Search", command=querySurname)
sNamebtn.place(x=100 ,y=90)

#edit button
editbtn = tk.Button(vPat, text="Edit Patient", command=ePat_form)
editbtn.place(x=330 ,y=60)

#Delete Patient
editbtn = tk.Button(vPat, text="Del Patient", command=dPat_form)
editbtn.place(x=330 ,y=90)

#display table
output_data(data_set, tableLabel)

vPat.mainloop()