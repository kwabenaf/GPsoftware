import tkinter as tk
from tkinter import *
import sqlite3, time, datetime, random, os
staff_db='staff.db'
my_conn = sqlite3.connect(staff_db)
cdb = my_conn.cursor()


#defining staff all forms
def aStaff_form():
    print("Button clicked to show add Staff form")
    vStaff.destroy()
    os.system('python aStaff.py')

def vStaff_form():
    print("Button clicked to show all Staff members")
    vStaff.destroy()
    os.system('python vStaff.py')
    
def dStaff_form():
    print("Button clicked to go to delete Staff form")
    vStaff.destroy()
    os.system('python dStaff.py')
    
def eStaff_form():
    print("Button clicked to go to edit Staff form")
    vStaff.destroy()
    os.system('python eStaff.py')
    
#defining Patient forms  
def aPat_form():
    print("Button clicked to open add Patient form")
    vStaff.destroy()
    os.system('python aPat.py')

def vPat_form():
    print("Button clicked to show all Patients")
    vStaff.destroy()
    os.system('python vPat.py')
    
def dPat_form():
    print("Button clicked to go to delete Patient form")
    vStaff.destroy()
    os.system('python dPat.py')
    
def ePat_form():
    print("Button clicked to go to edit Patient form")
    vStaff.destroy()
    os.system('python ePat.py')
    
    
#defining Appointment forms
def aApp_form():
    print("Button clicked to show Appointment menu")
    vStaff.destroy()
    os.system('python aApp.py')

def vApp_form():
    print("Button clicked to show all Appointments")
    vStaff.destroy()
    os.system('python vApp.py')
    
def dApp_form():
    print("Button clicked to go to delete Appointment form")
    vStaff.destroy()
    os.system('python dApp.py')
    
def eApp_form():
    print("Button clicked to go to edit Appointment form")
    vStaff.destroy()
    os.system('python eApp.py')
   
#defining other forms
def mMenu_form():
    print("Button clicked to go to Main Menu")
    vStaff.destroy()
    os.system('python mMenu.py')

def editpass_form():
    print("Button clicked to change password")
    vStaff.destroy()
    os.system('python editpass.py')
    
def login_form():
    print("Button clicked to logout")
    vStaff.destroy()
    os.system('python login.py')

#clear entries
def eclear():
    snameEntry.delete(0, END)

#search
def querySurname():
    
    tableLabel.place_forget()
    
    sname = snameEntry.get()
    print("Button clicked to query surname - searched for surname: " + sname) 
    
    data_set=my_conn.execute("SELECT * FROM staffDb WHERE surname=?", (sname,)) 
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


vStaff = tk.Tk()
vStaff.title('View All Staff')
vStaff.configure(background='sea green')

#centers the app on the screen
screen_width = vStaff.winfo_screenwidth()
screen_height = vStaff.winfo_screenheight() 

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

vStaff.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

data_set=my_conn.execute("SELECT * FROM staffDb")

#submenu labels and positioning
menu = Menu(vStaff)
vStaff.config(menu=menu)

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
titleLabel = tk.Label(vStaff, text="Staff Members", background="sea green", fg="black", font='Helvetica 12 bold')
titleLabel.place(x=300, y=0)

#table names
idLabel = tk.Label(vStaff, text = "ID", background="sea green", fg="black", font='Helvetica 8 bold')
idLabel.place(x=85 , y=160)

dateLabel = tk.Label(vStaff, text = "Date", background="sea green", fg="black", font='Helvetica 8 bold')
dateLabel.place(x=150 , y=160)

unameLabel = tk.Label(vStaff, text = "Username", background="sea green", fg="black", font='Helvetica 8 bold')
unameLabel.place(x=210 , y=160)

passLabel = tk.Label(vStaff, text = "Password", background="sea green", fg="black", font='Helvetica 8 bold')
passLabel.place(x=290 , y=160)

fnameLabel = tk.Label(vStaff, text = "Firstname", background="sea green", fg="black", font='Helvetica 8 bold')
fnameLabel.place(x=360 , y=160)

snameLabel = tk.Label(vStaff, text = "Surname", background="sea green", fg="black", font='Helvetica 8 bold')
snameLabel.place(x=440 , y=160)

roleLabel = tk.Label(vStaff, text = "Role", background="sea green", fg="black", font='Helvetica 8 bold')
roleLabel.place(x=530 , y=160)

ageLabel = tk.Label(vStaff, text = "Age", background="sea green", fg="black", font='Helvetica 8 bold')
ageLabel.place(x=600 , y=160)

tableLabel = tk.Label(vStaff, background="sea green", fg="black")
tableLabel.place(x=50, y=180)

stableLabel = tk.Label(vStaff, background="sea green", fg="black")
stableLabel.place(x=50, y=180)

#view all button
vallbtn = tk.Button(vStaff, text="View All", command=viewall)
vallbtn.place(x=330 ,y=30)

#search label and entry
snameLabel = tk.Label(vStaff, background="sea green", text="Search Surname:")
snameEntry = tk.Entry(vStaff, relief="raised")
snameLabel.place(x=30 ,y=60)
snameEntry.place(x=130, y=62)
snamebtn = tk.Button(vStaff, text="Search", command=querySurname)
snamebtn.place(x=100 ,y=90)

#edit button
editbtn = tk.Button(vStaff, text="Edit Staff", command=eStaff_form)
editbtn.place(x=330 ,y=60)

#Delete Staff
editbtn = tk.Button(vStaff, text="Del Staff", command=dStaff_form)
editbtn.place(x=330 ,y=90)

#display table
output_data(data_set, tableLabel)

vStaff.mainloop()
