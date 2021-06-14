import tkinter as tk
from tkinter import *
import sqlite3, time, datetime, random, os
staff_db='staff.db'
my_conn = sqlite3.connect(staff_db)
cdb = my_conn.cursor()




#defining staff all forms
def aStaff_form():
    print("Button clicked to show add Staff form")
    eStaff.destroy()
    os.system('python aStaff.py')

def vStaff_form():
    print("Button clicked to show all Staff members")
    eStaff.destroy()
    os.system('python vStaff.py')
    
def dStaff_form():
    print("Button clicked to go to delete Staff form")
    eStaff.destroy()
    os.system('python dStaff.py')
    
def eStaff_form():
    print("Button clicked to go to edit Staff form")
    eStaff.destroy()
    os.system('python eStaff.py')
    
#defining Patient forms  
def aPat_form():
    print("Button clicked to open add Patient form")
    eStaff.destroy()
    os.system('python aPat.py')

def vPat_form():
    print("Button clicked to show all Patients")
    eStaff.destroy()
    os.system('python vPat.py')
    
def dPat_form():
    print("Button clicked to go to delete Patient form")
    eStaff.destroy()
    os.system('python dPat.py')
    
def ePat_form():
    print("Button clicked to go to edit Patient form")
    eStaff.destroy()
    os.system('python ePat.py')

def ePatmeddn_form():
    print("Button clicked to go to edit Patient medical records")
    ePat.destroy()
    os.system('python ePatmeddn.py')
    
#defining Appointment forms
def aApp_form():
    print("Button clicked to show Appointment menu")
    eStaff.destroy()
    os.system('python aApp.py')

def vApp_form():
    print("Button clicked to show all Appointments")
    eStaff.destroy()
    os.system('python vApp.py')
    
def dApp_form():
    print("Button clicked to go to delete Appointment form")
    eStaff.destroy()
    os.system('python dApp.py')
    
def eApp_form():
    print("Button clicked to go to edit Appointment form")
    eStaff.destroy()
    os.system('python eApp.py')


#defining other forms
def mMenu_form():
    print("Button clicked to go to Main Menu")
    eStaff.destroy()
    os.system('python mMenu.py')

def editpass_form():
    print("Button clicked to change password")
    eStaff.destroy()
    os.system('python editpass.py')
    
def login_form():
    print("Button clicked to logout")
    eStaff.destroy()
    os.system('python login.py')
    
#clear entries
def eclear():
    idEntry.delete(0, END)
    unameEntry.delete(0, END)
    passEntry.delete(0, END)
    fnameEntry.delete(0, END)
    snameEntry.delete(0, END)
    roleEntry.delete(0, END)
    ageEntry.delete(0, END)
  

#searching a record to display    
def searchid():
    
    eclear()
    
    idno = idnoEntry.get()
    
    data_set=my_conn.execute("SELECT * FROM staffDb WHERE idno=?", (idno,)) 
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
        unameEntry.insert(0, person[2])
        passEntry.insert(0, person[3])
        fnameEntry.insert(0, person[4])
        snameEntry.insert(0, person[5])
        roleEntry.insert(0, person[6])
        ageEntry.insert(0, person[7])
    
    return tableLabel

def updaterec():
    
    idnorec = idnoEntry.get() 
    
    cdb.execute("""UPDATE staffDb SET
            username = :uname,
            password = :pass,
            firstname = :fname,
            surname = :sname,
            role = :role,
            age = :age
            
            WHERE idno = :idno""",
            {'uname': unameEntry.get(),
             'pass': passEntry.get(),
             'fname': fnameEntry.get(),
             'sname': snameEntry.get(),
             'role': roleEntry.get(),
             'age': ageEntry.get(),
                    
            'idno': idnorec
            })
    
    my_conn.commit()
    my_conn.close()
    
    tk.messagebox.showinfo(title = 'Updated', message = "Record has been updated")
    eclear()

#application dimensions
app_width = 500
app_height = 600


eStaff = tk.Tk()
eStaff.title('Edit Staff')
eStaff.configure(background='sea green')

#centers the app on the screen
screen_width = eStaff.winfo_screenwidth()
screen_height = eStaff.winfo_screenheight() 

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

eStaff.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

#submenu labels and positioning
menu = Menu(eStaff)
eStaff.config(menu=menu)

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
titleLabel = tk.Label(eStaff, text="Editing Staff Member", background="sea green", fg="black")
titleLabel.grid(row=0, column=4, padx=10, pady=10)


#search label and entry
idnoLabel = tk.Label(eStaff, background="sea green", text="Search ID:")
idnoEntry = tk.Entry(eStaff, relief="raised")
idnoLabel.grid(row=2, column=3, padx=10, pady=10)
idnoEntry.grid(row=2, column=4)
searchbtn = tk.Button(eStaff, text="Search", command=searchid)
searchbtn.grid(row=3, column=3, columnspan=2)

#entries and labels to display information
idLabel = tk.Label(eStaff, text="ID:", background="dark sea green", fg="black")
idEntry = tk.Entry(eStaff, relief="groove", background="medium sea green")
idLabel.grid(row=4, column=3, padx=70, pady=30)
idEntry.grid(row=4, column=4)


unameLabel = tk.Label(eStaff, text="Username:", background="dark sea green", fg="black")
unameEntry = tk.Entry(eStaff, relief="groove", background="medium sea green")
unameLabel.grid(row=5, column=3, padx=70, pady=20)
unameEntry.grid(row=5, column=4)

passLabel = tk.Label(eStaff, text="Password:", background="dark sea green", fg="black")
passEntry = tk.Entry(eStaff, relief="groove", background="medium sea green")
passLabel.grid(row=6, column=3, padx=70, pady=20)
passEntry.grid(row=6, column=4)

fnameLabel = tk.Label(eStaff, text="Firstname:", background="dark sea green", fg="black")
fnameEntry = tk.Entry(eStaff, relief="groove", background="medium sea green")
fnameLabel.grid(row=5, column=3, padx=70, pady=20)
fnameEntry.grid(row=5, column=4)

snameLabel = tk.Label(eStaff, text="Surname:", background="dark sea green", fg="black")
snameEntry = tk.Entry(eStaff, relief="groove", background="medium sea green")
snameLabel.grid(row=7, column=3, padx=70, pady=20)
snameEntry.grid(row=7, column=4)

roleLabel = tk.Label(eStaff, text="Role:", background="dark sea green", fg="black")
roleEntry = tk.Entry(eStaff, relief="groove", background="medium sea green")
roleLabel.grid(row=8, column=3, padx=70, pady=20)
roleEntry.grid(row=8, column=4)

ageLabel = tk.Label(eStaff, text="Age:", background="dark sea green", fg="black")
ageEntry = tk.Entry(eStaff, relief="groove", background="medium sea green")
ageLabel.grid(row=9, column=3, padx=70, pady=20)
ageEntry.grid(row=9, column=4)

btnedit = tk.Button(eStaff, text="Edit", fg="black", font='Helvetica 10 bold', command = updaterec)
btnedit.grid(columnspan=5)

eStaff.mainloop()