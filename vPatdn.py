import tkinter as tk
from tkinter import *
import sqlite3, time, datetime, random, os
patient_db='patient.db'
my_conn = sqlite3.connect(patient_db)
cdb = my_conn.cursor()


#defining Patient forms  
def vPatdn_form():
    print("Button clicked to show all Patients")
    vPatdn.destroy()
    os.system('python vPatdn.py')
    
def ePatmeddn_form():
    print("Button clicked to go to edit Patient form")
    vPatdn.destroy()
    os.system('python ePatmeddn.py')

    
#defining Appointment forms
def aAppdn_form():
    print("Button clicked to show Appointment menu")
    vPatdn.destroy()
    os.system('python aAppdn.py')

def vAppdn_form():
    print("Button clicked to show all Appointments")
    vPatdn.destroy()
    os.system('python vAppdn.py')
    
def dAppdn_form():
    print("Button clicked to go to delete Appointment form")
    vPatdn.destroy()
    os.system('python dAppdn.py')
    
def eAppdn_form():
    print("Button clicked to go to edit Appointment form")
    vPatdn.destroy()
    os.system('python eAppdn.py')


#defining other forms
def mMenudn_form():
    print("Button clicked to go to Main Menu")
    vPatdn.destroy()
    os.system('python mMenudn.py')

def ePassdn_form():
    print("Button clicked to change password")
    vPatdn.destroy()
    os.system('python ePassdn.py')
    
def login_form():
    print("Button clicked to logout")
    vPatdn.destroy()
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


vPatdn = tk.Tk()
vPatdn.title('View Patients')
vPatdn.configure(background='sea green')

#centers the app on the screen
screen_width = vPatdn.winfo_screenwidth()
screen_height = vPatdn.winfo_screenheight() 

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

vPatdn.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

data_set=my_conn.execute("SELECT * FROM patientDb")

#submenu labels and positioning
menu = Menu(vPatdn)
vPatdn.config(menu=menu)

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

appSubmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Appointment", menu=appSubmenu)
appSubmenu.add_command(label="View Appointments", command = vAppdn_form)
appSubmenu.add_command(label="Book Appointment", command = aAppdn_form)
appSubmenu.add_command(label="Cancel Appointment", command = dAppdn_form)
appSubmenu.add_command(label="Edit Appointment", command = eAppdn_form)

#title
titleLabel = tk.Label(vPatdn, text="Patient Records", background="sea green", fg="black", font='Helvetica 12 bold')
titleLabel.place(x=300, y=0)

#table names
idLabel = tk.Label(vPatdn, text = "ID", background="sea green", fg="black", font='Helvetica 8 bold')
idLabel.place(x=85 , y=160)

fnameLabel = tk.Label(vPatdn, text = "Firstname", background="sea green", fg="black", font='Helvetica 8 bold')
fnameLabel.place(x=150 , y=160)

snameLabel = tk.Label(vPatdn, text = "Surname", background="sea green", fg="black", font='Helvetica 8 bold')
snameLabel.place(x=210 , y=160)

dobLabel = tk.Label(vPatdn, text = "DoB", background="sea green", fg="black", font='Helvetica 8 bold')
dobLabel.place(x=290 , y=160)

addressLabel = tk.Label(vPatdn, text = "Address", background="sea green", fg="black", font='Helvetica 8 bold')
addressLabel.place(x=360 , y=160)

genLabel = tk.Label(vPatdn, text = "Gender", background="sea green", fg="black", font='Helvetica 8 bold')
genLabel.place(x=440 , y=160)

phoneLabel = tk.Label(vPatdn, text = "Phone no.", background="sea green", fg="black", font='Helvetica 8 bold')
phoneLabel.place(x=530 , y=160)

emailLabel = tk.Label(vPatdn, text = "Email", background="sea green", fg="black", font='Helvetica 8 bold')
emailLabel.place(x=600 , y=160)

tableLabel = tk.Label(vPatdn, background="sea green", fg="black")
tableLabel.place(x=50, y=180)

stableLabel = tk.Label(vPatdn, background="sea green", fg="black")
stableLabel.place(x=50, y=180)

#view all button
vallbtn = tk.Button(vPatdn, text="View All", command=viewall)
vallbtn.place(x=330 ,y=30)

#search label and entry
sNameLabel = tk.Label(vPatdn, background="sea green", text="Search Surname:")
sNameEntry = tk.Entry(vPatdn, relief="raised")
sNameLabel.place(x=30 ,y=60)
sNameEntry.place(x=130, y=62)
sNamebtn = tk.Button(vPatdn, text="Search", command=querySurname)
sNamebtn.place(x=100 ,y=90)

#edit button
editbtn = tk.Button(vPat, text="Edit Patient", command=ePatmeddn_form)
editbtn.place(x=330 ,y=60)

#display table
output_data(data_set, tableLabel)


vPatdn.mainloop()
