import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3, time, datetime, random, os
patient_db='patient.db'
my_conn = sqlite3.connect(patient_db)
cdb = my_conn.cursor()


#defining Patient forms  
def vPatdn_form():
    print("Button clicked to show all Patients")
    ePatmeddn.destroy()
    os.system('python vPatdn.py')
    
def ePatmeddn_form():
    print("Button clicked to go to edit Patient form")
    ePatmeddn.destroy()
    os.system('python ePatmeddn.py')

def sPatdn_form():
    print("Button clicked to go to search Patient form")
    ePatmeddn.destroy()
    os.system('python sPatdn.py')
       
    
#defining Appointment forms
def aAppdn_form():
    print("Button clicked to show Appointment menu")
    ePatmeddn.destroy()
    os.system('python aAppdn.py')

def vAppdn_form():
    print("Button clicked to show all Appointments")
    ePatmeddn.destroy()
    os.system('python vAppdn.py')
    
def dAppdn_form():
    print("Button clicked to go to delete Appointment form")
    ePatmeddn.destroy()
    os.system('python dAppdn.py')
    
def eAppdn_form():
    print("Button clicked to go to edit Appointment form")
    ePatmeddn.destroy()
    os.system('python eAppdn.py')


#defining other forms
def mMenudn_form():
    print("Button clicked to go to Main Menu")
    ePatmeddn.destroy()
    os.system('python mMenudn.py')

def ePassdn_form():
    print("Button clicked to change password")
    ePatmeddn.destroy()
    os.system('python ePassdn.py')
    
def login_form():
    print("Button clicked to logout")
    ePatmeddn.destroy()
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


ePatmeddn = tk.Tk()
ePatmeddn.title('Edit Patient Medical Records')
ePatmeddn.configure(background='sea green')

#centers the app on the screen
screen_width = ePatmeddn.winfo_screenwidth()
screen_height = ePatmeddn.winfo_screenheight() 

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

ePatmeddn.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

#submenu labels and positioning
menu = Menu(ePatmeddn)
ePatmeddn.config(menu=menu)

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

tableLabel = tk.Label()

#form labels and buttons
titleLabel = tk.Label(ePatmeddn, text="Editing Patient Records", background="sea green", fg="black")
titleLabel.grid(row=0, column=4, padx=10, pady=10)


#search label and entry
idnoLabel = tk.Label(ePatmeddn, background="sea green", text="Search ID:")
idnoEntry = tk.Entry(ePatmeddn, relief="raised")
idnoLabel.grid(row=2, column=3, padx=10, pady=10)
idnoEntry.grid(row=2, column=4)
searchbtn = tk.Button(ePatmeddn, text="Search", command=searchid)
searchbtn.grid(row=3, column=3, columnspan=2)

#entries and labels to display information
idLabel = tk.Label(ePatmeddn, text="ID:", background="dark sea green", fg="black")
idEntry = tk.Entry(ePatmeddn, relief="groove", background="medium sea green")
idLabel.grid(row=4, column=3, padx=70, pady=30)
idEntry.grid(row=4, column=4)


fnameLabel = tk.Label(ePatmeddn, text="Firstname:", background="dark sea green", fg="black")
fnameEntry = tk.Entry(ePatmeddn, relief="groove", background="medium sea green")
fnameLabel.grid(row=5, column=3, padx=70, pady=10)
fnameEntry.grid(row=5, column=4)

snameLabel = tk.Label(ePatmeddn, text="Surname:", background="dark sea green", fg="black")
snameEntry = tk.Entry(ePatmeddn, relief="groove", background="medium sea green")
snameLabel.grid(row=6, column=3, padx=70, pady=10)
snameEntry.grid(row=6, column=4)

dobLabel = tk.Label(ePatmeddn, text="DoB:", background="dark sea green", fg="black")
dobEntry = tk.Entry(ePatmeddn, relief="groove", background="medium sea green")
dobLabel.grid(row=7, column=3, padx=70, pady=10)
dobEntry.grid(row=7, column=4)

addressLabel = tk.Label(ePatmeddn, text="Address:", background="dark sea green", fg="black")
addressEntry = tk.Entry(ePatmeddn, relief="groove", background="medium sea green")
addressLabel.grid(row=8, column=3, padx=70, pady=10)
addressEntry.grid(row=8, column=4)

genLabel = tk.Label(ePatmeddn, text="Gender:", background="dark sea green", fg="black")
genEntry = tk.Entry(ePatmeddn, relief="groove", background="medium sea green")
genLabel.grid(row=9, column=3, padx=70, pady=10)
genEntry.grid(row=9, column=4)

phoneLabel = tk.Label(ePatmeddn, text="Phone no.:", background="dark sea green", fg="black")
phoneEntry = tk.Entry(ePatmeddn, relief="groove", background="medium sea green")
phoneLabel.grid(row=10, column=3, padx=70, pady=10)
phoneEntry.grid(row=10, column=4)

emailLabel = tk.Label(ePatmeddn, text="Email:", background="dark sea green", fg="black")
emailEntry = tk.Entry(ePatmeddn, relief="groove", background="medium sea green")
emailLabel.grid(row=11, column=3, padx=70, pady=10)
emailEntry.grid(row=11, column=4)

btnedit = tk.Button(ePatmeddn, text="Edit", fg="black", font='Helvetica 10 bold', command = updaterec)
btnedit.grid(columnspan=5)

ePatmeddn.mainloop()
