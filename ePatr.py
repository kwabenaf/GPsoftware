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
    ePatr.destroy()
    os.system('python aPatr.py')

def vPatr_form():
    print("Button clicked to show all Patients")
    ePatr.destroy()
    os.system('python vPatr.py')
    
def dPatr_form():
    print("Button clicked to go to delete Patient form")
    ePatr.destroy()
    os.system('python dPatr.py')
    
def ePatr_form():
    print("Button clicked to go to edit Patient form")
    ePatr.destroy()
    os.system('python ePatr.py')
    
    
#defining Appointment forms
def aAppr_form():
    print("Button clicked to show Appointment menu")
    ePatr.destroy()
    os.system('python aAppr.py')

def vAppr_form():
    print("Button clicked to show all Appointments")
    ePatr.destroy()
    os.system('python vAppr.py')
    
def dAppr_form():
    print("Button clicked to go to delete Appointment form")
    ePatr.destroy()
    os.system('python dAppr.py')
    
def eAppr_form():
    print("Button clicked to go to edit Appointment form")
    ePatr.destroy()
    os.system('python eAppr.py')


#defining other forms
def mMenur_form():
    print("Button clicked to go to Main Menu")
    ePatr.destroy()
    os.system('python mMenur.py')

def ePassr_form():
    print("Button clicked to change password")
    ePatr.destroy()
    os.system('python ePassr.py')
    
def login_form():
    print("Button clicked to logout")
    ePatr.destroy()
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


ePatr = tk.Tk()
ePatr.title('Edit Patient Details')
ePatr.configure(background='sea green')

#centers the app on the screen
screen_width = ePatr.winfo_screenwidth()
screen_height = ePatr.winfo_screenheight() 

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

ePatr.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

#submenu labels and positioning
menu = Menu(ePatr)
ePatr.config(menu=menu)

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

tableLabel = tk.Label()

#form labels and buttons
titleLabel = tk.Label(ePatr, text="Editing Patient Records", background="sea green", fg="black")
titleLabel.grid(row=0, column=4, padx=10, pady=10)


#search label and entry
idnoLabel = tk.Label(ePatr, background="sea green", text="Search ID:")
idnoEntry = tk.Entry(ePatr, relief="raised")
idnoLabel.grid(row=2, column=3, padx=10, pady=10)
idnoEntry.grid(row=2, column=4)
searchbtn = tk.Button(ePatr, text="Search", command=searchid)
searchbtn.grid(row=3, column=3, columnspan=2)

#entries and labels to display information
idLabel = tk.Label(ePatr, text="ID:", background="dark sea green", fg="black")
idEntry = tk.Entry(ePatr, relief="groove", background="medium sea green")
idLabel.grid(row=4, column=3, padx=70, pady=30)
idEntry.grid(row=4, column=4)


fnameLabel = tk.Label(ePatr, text="Firstname:", background="dark sea green", fg="black")
fnameEntry = tk.Entry(ePatr, relief="groove", background="medium sea green")
fnameLabel.grid(row=5, column=3, padx=70, pady=10)
fnameEntry.grid(row=5, column=4)

snameLabel = tk.Label(ePatr, text="Surname:", background="dark sea green", fg="black")
snameEntry = tk.Entry(ePatr, relief="groove", background="medium sea green")
snameLabel.grid(row=6, column=3, padx=70, pady=10)
snameEntry.grid(row=6, column=4)

dobLabel = tk.Label(ePatr, text="DoB:", background="dark sea green", fg="black")
dobEntry = tk.Entry(ePatr, relief="groove", background="medium sea green")
dobLabel.grid(row=7, column=3, padx=70, pady=10)
dobEntry.grid(row=7, column=4)

addressLabel = tk.Label(ePatr, text="Address:", background="dark sea green", fg="black")
addressEntry = tk.Entry(ePatr, relief="groove", background="medium sea green")
addressLabel.grid(row=8, column=3, padx=70, pady=10)
addressEntry.grid(row=8, column=4)

genLabel = tk.Label(ePatr, text="Gender:", background="dark sea green", fg="black")
genEntry = tk.Entry(ePatr, relief="groove", background="medium sea green")
genLabel.grid(row=9, column=3, padx=70, pady=10)
genEntry.grid(row=9, column=4)

phoneLabel = tk.Label(ePatr, text="Phone no.:", background="dark sea green", fg="black")
phoneEntry = tk.Entry(ePatr, relief="groove", background="medium sea green")
phoneLabel.grid(row=10, column=3, padx=70, pady=10)
phoneEntry.grid(row=10, column=4)

emailLabel = tk.Label(ePatr, text="Email:", background="dark sea green", fg="black")
emailEntry = tk.Entry(ePatr, relief="groove", background="medium sea green")
emailLabel.grid(row=11, column=3, padx=70, pady=10)
emailEntry.grid(row=11, column=4)

btnedit = tk.Button(ePatr, text="Edit", fg="black", font='Helvetica 10 bold', command = updaterec)
btnedit.grid(columnspan=5)

ePatr.mainloop()
