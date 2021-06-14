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
    ePat.destroy()
    os.system('python aStaff.py')

def vStaff_form():
    print("Button clicked to show all Staff members")
    ePat.destroy()
    os.system('python vStaff.py')
    
def dStaff_form():
    print("Button clicked to go to delete Staff form")
    ePat.destroy()
    os.system('python dStaff.py')
    
def eStaff_form():
    print("Button clicked to go to edit Staff form")
    ePat.destroy()
    os.system('python eStaff.py')
    
#defining Patient forms  
def aPat_form():
    print("Button clicked to open add Patient form")
    ePat.destroy()
    os.system('python aPat.py')

def vPat_form():
    print("Button clicked to show all Patients")
    ePat.destroy()
    os.system('python vPat.py')
    
def dPat_form():
    print("Button clicked to go to delete Patient form")
    ePat.destroy()
    os.system('python dPat.py')
    
def ePat_form():
    print("Button clicked to go to edit Patient form")
    ePat.destroy()
    os.system('python ePat.py')

def ePatmeddn_form():
    print("Button clicked to go to edit Patient medical records")
    ePat.destroy()
    os.system('python ePatmeddn.py')
       
    
#defining Appointment forms
def aApp_form():
    print("Button clicked to show Appointment menu")
    ePat.destroy()
    os.system('python aApp.py')

def vApp_form():
    print("Button clicked to show all Appointments")
    ePat.destroy()
    os.system('python vApp.py')
    
def dApp_form():
    print("Button clicked to go to delete Appointment form")
    ePat.destroy()
    os.system('python dApp.py')
    
def eApp_form():
    print("Button clicked to go to edit Appointment form")
    ePat.destroy()
    os.system('python eApp.py')


#defining other forms
def mMenu_form():
    print("Button clicked to go to Main Menu")
    ePat.destroy()
    os.system('python mMenu.py')

def editpass_form():
    print("Button clicked to change password")
    ePat.destroy()
    os.system('python editpass.py')
    
def login_form():
    print("Button clicked to logout")
    ePat.destroy()
    os.system('python login.py')

    
#clear entries
def eclear():
    fnameEntry.delete(0, END)
    snameEntry.delete(0, END)
    dobEntry.delete(0, END)
    addressEntry.delete(0, END)
    genEntry.delete(0, END)
    phoneEntry.delete(0, END)
    emailEntry.delete(0, END)
  

#searching a record to display    
def searchid():
    
    eclear()
    
    idno = idnoEntry.get()
    
    data_set=my_conn.execute("SELECT * FROM patientDb WHERE idno=?", (idno,)) 
    output_data(data_set, tableLabel)
    
  
#display data from database
def output_data(data_set,tableLabel):
    i=0 # row value inside the loop 
    for person in data_set: 
        for j in range(len(person)):
            e = Entry(tableLabel, width=12, fg='blue') 
            e.grid(row=i, column=j) 
            e.insert(END, person[j])
        i=i+1
        idEntry.insert(0, person[0])
        fnameEntry.insert(0, person[1])
        snameEntry.insert(0, person[2])
        dobEntry.insert(0, person[3])
        addressEntry.insert(0, person[4])
        genEntry.insert(0, person[5])
        phoneEntry.insert(0, person[6])
        emailEntry.insert(0, person[7])
    
    return tableLabel

def updaterec():
    
    idnorec = idnoEntry.get() 
    
    cdb.execute("""UPDATE patientDb SET
            firstname = :fname,
            surname = :sname,
            dob = :dob,
            address = :address,
            gender = :gen,
            phone = :phone,
            email = :email
            
            WHERE idno = :idno""",
            {'fname': fnameEntry.get(),
             'sname': snameEntry.get(),
             'dob': dobEntry.get(),
             'address': addressEntry.get(),
             'gen': genEntry.get(),
             'phone': phoneEntry.get(),
             'email': emailEntry.get(),
                    
            'idno': idnorec
            })
    
    my_conn.commit()
    my_conn.close()
    
    tk.messagebox.showinfo(title = 'Updated', message = "Record has been updated")
    eclear()
    
#application dimensions
app_width = 500
app_height = 600


ePat = tk.Tk()
ePat.title('Edit Patient Details')
ePat.configure(background='sea green')

#centers the app on the screen
screen_width = ePat.winfo_screenwidth()
screen_height = ePat.winfo_screenheight() 

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

ePat.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

#submenu labels and positioning
menu = Menu(ePat)
ePat.config(menu=menu)

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

tableLabel = tk.Label()

#form labels and buttons
titleLabel = tk.Label(ePat, text="Editing Patient Records", background="sea green", fg="black")
titleLabel.grid(row=0, column=4, padx=10, pady=10)


#search label and entry
idnoLabel = tk.Label(ePat, background="sea green", text="Search ID:")
idnoEntry = tk.Entry(ePat, relief="raised")
idnoLabel.grid(row=2, column=3, padx=10, pady=10)
idnoEntry.grid(row=2, column=4)
searchbtn = tk.Button(ePat, text="Search", command=searchid)
searchbtn.grid(row=3, column=3, columnspan=2)

#entries and labels to display information
idLabel = tk.Label(ePat, text="ID:", background="dark sea green", fg="black")
idEntry = tk.Entry(ePat, relief="groove", background="medium sea green")
idLabel.grid(row=4, column=3, padx=70, pady=30)
idEntry.grid(row=4, column=4)


fnameLabel = tk.Label(ePat, text="Firstname:", background="dark sea green", fg="black")
fnameEntry = tk.Entry(ePat, relief="groove", background="medium sea green")
fnameLabel.grid(row=5, column=3, padx=70, pady=10)
fnameEntry.grid(row=5, column=4)

snameLabel = tk.Label(ePat, text="Surname:", background="dark sea green", fg="black")
snameEntry = tk.Entry(ePat, relief="groove", background="medium sea green")
snameLabel.grid(row=6, column=3, padx=70, pady=10)
snameEntry.grid(row=6, column=4)

dobLabel = tk.Label(ePat, text="DoB:", background="dark sea green", fg="black")
dobEntry = tk.Entry(ePat, relief="groove", background="medium sea green")
dobLabel.grid(row=7, column=3, padx=70, pady=10)
dobEntry.grid(row=7, column=4)

addressLabel = tk.Label(ePat, text="Address:", background="dark sea green", fg="black")
addressEntry = tk.Entry(ePat, relief="groove", background="medium sea green")
addressLabel.grid(row=8, column=3, padx=70, pady=10)
addressEntry.grid(row=8, column=4)

genLabel = tk.Label(ePat, text="Gender:", background="dark sea green", fg="black")
genEntry = tk.Entry(ePat, relief="groove", background="medium sea green")
genLabel.grid(row=9, column=3, padx=70, pady=10)
genEntry.grid(row=9, column=4)

phoneLabel = tk.Label(ePat, text="Phone no.:", background="dark sea green", fg="black")
phoneEntry = tk.Entry(ePat, relief="groove", background="medium sea green")
phoneLabel.grid(row=10, column=3, padx=70, pady=10)
phoneEntry.grid(row=10, column=4)

emailLabel = tk.Label(ePat, text="Email:", background="dark sea green", fg="black")
emailEntry = tk.Entry(ePat, relief="groove", background="medium sea green")
emailLabel.grid(row=11, column=3, padx=70, pady=10)
emailEntry.grid(row=11, column=4)

btnedit = tk.Button(ePat, text="Edit", fg="black", font='Helvetica 10 bold', command = updaterec)
btnedit.grid(columnspan=5)

ePat.mainloop()