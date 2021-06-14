import tkinter as tk
from tkinter import *
import sqlite3, time, datetime, random, os
patient_db='patient.db'
my_conn = sqlite3.connect(patient_db)
cdb = my_conn.cursor()


#defining Patient forms  
def aPatr_form():
    print("Button clicked to open add Patient form")
    vPatr.destroy()
    os.system('python aPatr.py')

def vPatr_form():
    print("Button clicked to show all Patients")
    vPatr.destroy()
    os.system('python vPatr.py')
    
def dPatr_form():
    print("Button clicked to go to delete Patient form")
    vPatr.destroy()
    os.system('python dPatr.py')
    
def ePatr_form():
    print("Button clicked to go to edit Patient form")
    vPatr.destroy()
    os.system('python ePatr.py')
    
    
#defining Appointment forms
def aAppr_form():
    print("Button clicked to show Appointment menu")
    vPatr.destroy()
    os.system('python aAppr.py')

def vAppr_form():
    print("Button clicked to show all Appointments")
    vPatr.destroy()
    os.system('python vAppr.py')
    
def dAppr_form():
    print("Button clicked to go to delete Appointment form")
    vPatr.destroy()
    os.system('python dAppr.py')
    
def eAppr_form():
    print("Button clicked to go to edit Appointment form")
    vPatr.destroy()
    os.system('python eAppr.py')


#defining other forms
def mMenur_form():
    print("Button clicked to go to Main Menu")
    vPatr.destroy()
    os.system('python mMenur.py')

def ePassr_form():
    print("Button clicked to change password")
    vPatr.destroy()
    os.system('python ePassr.py')
    
def login_form():
    print("Button clicked to logout")
    vPatr.destroy()
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


vPatr = tk.Tk()
vPatr.title('View Patients')
vPatr.configure(background='sea green')

#centers the app on the screen
screen_width = vPatr.winfo_screenwidth()
screen_height = vPatr.winfo_screenheight() 

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

vPatr.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

data_set=my_conn.execute("SELECT * FROM patientDb")

#submenu labels and positioning
menu = Menu(vPatr)
vPatr.config(menu=menu)

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
titleLabel = tk.Label(vPatr, text="Patient Records", background="sea green", fg="black", font='Helvetica 12 bold')
titleLabel.place(x=300, y=0)

#table names
idLabel = tk.Label(vPatr, text = "ID", background="sea green", fg="black", font='Helvetica 8 bold')
idLabel.place(x=85 , y=160)

fnameLabel = tk.Label(vPatr, text = "Firstname", background="sea green", fg="black", font='Helvetica 8 bold')
fnameLabel.place(x=150 , y=160)

snameLabel = tk.Label(vPatr, text = "Surname", background="sea green", fg="black", font='Helvetica 8 bold')
snameLabel.place(x=210 , y=160)

dobLabel = tk.Label(vPatr, text = "DoB", background="sea green", fg="black", font='Helvetica 8 bold')
dobLabel.place(x=290 , y=160)

addressLabel = tk.Label(vPatr, text = "Address", background="sea green", fg="black", font='Helvetica 8 bold')
addressLabel.place(x=360 , y=160)

genLabel = tk.Label(vPatr, text = "Gender", background="sea green", fg="black", font='Helvetica 8 bold')
genLabel.place(x=440 , y=160)

phoneLabel = tk.Label(vPatr, text = "Phone no.", background="sea green", fg="black", font='Helvetica 8 bold')
phoneLabel.place(x=530 , y=160)

emailLabel = tk.Label(vPatr, text = "Email", background="sea green", fg="black", font='Helvetica 8 bold')
emailLabel.place(x=600 , y=160)

tableLabel = tk.Label(vPatr, background="sea green", fg="black")
tableLabel.place(x=50, y=180)

stableLabel = tk.Label(vPatr, background="sea green", fg="black")
stableLabel.place(x=50, y=180)

#view all button
vallbtn = tk.Button(vPatr, text="View All", command=viewall)
vallbtn.place(x=330 ,y=30)

#search label and entry
sNameLabel = tk.Label(vPatr, background="sea green", text="Search Surname:")
sNameEntry = tk.Entry(vPatr, relief="raised")
sNameLabel.place(x=30 ,y=60)
sNameEntry.place(x=130, y=62)
sNamebtn = tk.Button(vPatr, text="Search", command=querySurname)
sNamebtn.place(x=100 ,y=90)

#edit button
editbtn = tk.Button(vPatr, text="Edit Patient", command=ePatr_form)
editbtn.place(x=330 ,y=60)

#Delete Patient
editbtn = tk.Button(vPatr, text="Del Patient", command=dPatr_form)
editbtn.place(x=330 ,y=90)

#display table
output_data(data_set, tableLabel)

vPatr.mainloop()
