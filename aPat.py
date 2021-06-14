import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3, time, datetime, random, os
patient_db='patient.db'
my_conn = sqlite3.connect(patient_db)
cdb = my_conn.cursor()


#defining staff all forms
def aStaff_form():
    print("Button clicked to show add Staff form")
    aPat.destroy()
    os.system('python aStaff.py')

def vStaff_form():
    print("Button clicked to show all Staff members")
    aPat.destroy()
    os.system('python vStaff.py')
    
def dStaff_form():
    print("Button clicked to go to delete Staff form")
    aPat.destroy()
    os.system('python dStaff.py')
    
def eStaff_form():
    print("Button clicked to go to edit Staff form")
    aPat.destroy()
    os.system('python eStaff.py')
    
#defining Patient forms  
def aPat_form():
    print("Button clicked to open add Patient form")
    aPat.destroy()
    os.system('python aPat.py')

def vPat_form():
    print("Button clicked to show all Patients")
    aPat.destroy()
    os.system('python vPat.py')
    
def dPat_form():
    print("Button clicked to go to delete Patient form")
    aPat.destroy()
    os.system('python dPat.py')
    
def ePat_form():
    print("Button clicked to go to edit Patient form")
    aPat.destroy()
    os.system('python ePat.py')

def ePatmeddn_form():
    print("Button clicked to go to edit Patient medical records")
    ePat.destroy()
    os.system('python ePatmeddn.py')
    
#defining Appointment forms
def aApp_form():
    print("Button clicked to show Appointment menu")
    aPat.destroy()
    os.system('python aApp.py')

def vApp_form():
    print("Button clicked to show all Appointments")
    aPat.destroy()
    os.system('python vApp.py')
    
def dApp_form():
    print("Button clicked to go to delete Appointment form")
    aPat.destroy()
    os.system('python dApp.py')
    
def eApp_form():
    print("Button clicked to go to edit Appointment form")
    aPat.destroy()
    os.system('python eApp.py')


#defining other forms
def mMenu_form():
    print("Button clicked to go to Main Menu")
    aPat.destroy()
    os.system('python mMenu.py')

def editpass_form():
    print("Button clicked to change password")
    aPat.destroy()
    os.system('python editpass.py')
    
def login_form():
    print("Button clicked to logout")
    aPat.destroy()
    os.system('python login.py')
    
gens = [
    "Male",
    "Female",
    "Other"
    ]

def clear_aPat():
    fnameEntry.delete(0, END)
    snameEntry.delete(0, END)
    dobEntry.delete(0, END)
    addressEntry.delete(0, END)
    genCombo.set('Select Gender')
    phoneEntry.delete(0, END)
    emailEntry.delete(0, END)
    
def create_table():
    cdb.execute("""CREATE TABLE IF NOT EXISTS patientDb (
                idno INTEGER PRIMARY KEY,
                firstname VARCHAR(20) NOT NULL,
                surname VARCHAR(10) NOT NULL,
                dob VARCHAR(20) NOT NULL,
                address VARCHAR(11) NOT NULL,
                gender VARCHAR(20) NOT NULL,
                phone INTEGER NOT NULL,
                email VARCHAR (20) NOT NULL)""")
    
def putRecord():

    with my_conn:
        
        firstname = fnameEntry.get().title().rstrip()
        surname = snameEntry.get().title().rstrip()
        dob = dobEntry.get().rstrip()
        address = addressEntry.get().rstrip()
        gender = genCombo.get().rstrip()
        phone = phoneEntry.get().rstrip()
        email = emailEntry.get().rstrip()
        
        #check entry is valid
        try:
            if firstname.isalpha() and surname.isalpha() and phone.isnumeric() and firstname.isalpha():
                            
                    
                cdb.execute('''INSERT INTO patientDb (
                                                    firstname,
                                                    surname,
                                                    dob,
                                                    address,
                                                    gender,
                                                    phone,
                                                    email) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                          (firstname, surname, dob, address, gender, phone, email))
                my_conn.commit()
                
                
                print("Added to DB")

                print("Firstname: " + firstname)
                print("Surname: " + surname)
                print("DoB: " + dob)
                print("Address: " + address)
                print("Gender: " + gender)
                print("Phone: " + phone)
                print("Email: " + email)
                clear_aPat()

            else:
                tk.messagebox.showerror(title = 'Invaild', message = "Invaild data, please try again")
        except ValueError:
           pass

#creates the table    
create_table()

#application dimensions
app_width = 500
app_height = 600


aPat = tk.Tk()   
aPat.title('Add Patients')
aPat.configure(background='sea green')

#centers the app on the screen
screen_width = aPat.winfo_screenwidth()
screen_height = aPat.winfo_screenheight() 

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

aPat.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

#submenu labels and positioning
menu = Menu(aPat)
aPat.config(menu=menu)

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

#changing the combo box colours and style
combostyle = ttk.Style()

combostyle.theme_create('combostyle', parent='alt',
                         settings = {'TCombobox':
                                     {'configure':
                                      {'selectbackground': 'blue',
                                       'fieldbackground': 'medium sea green',
                                       'background': 'dark green'
                                       }}}
                        )

combostyle.theme_use('combostyle') 

#labels and entries
titleLabel = tk.Label(aPat, text="Adding A New Patient Record", background="sea green", fg="black", font="7")
titleLabel.grid(row=0, column=3, columnspan=2, padx=10, pady=10)

fnameLabel = tk.Label(aPat, text="Firstname:", background="dark sea green", fg="black")
fnameEntry = tk.Entry(aPat, relief="groove", background="medium sea green")
fnameLabel.grid(row=3, column=3, padx=70, pady=10)
fnameEntry.grid(row=3, column=4)

snameLabel = tk.Label(aPat, text="Surname:", background="dark sea green", fg="black")
snameEntry = tk.Entry(aPat, relief="groove", background="medium sea green")
snameLabel.grid(row=4, column=3, padx=70, pady=10)
snameEntry.grid(row=4, column=4)

dobLabel = tk.Label(aPat, text="DoB:", background="dark sea green", fg="black")
dobEntry = tk.Entry(aPat, relief="groove", background="medium sea green")
dobLabel.grid(row=5, column=3, padx=70, pady=10)
dobEntry.grid(row=5, column=4)

addressLabel = tk.Label(aPat, text="Address:", background="dark sea green", fg="black")
addressEntry = tk.Entry(aPat, relief="groove", background="medium sea green")
addressLabel.grid(row=6, column=3, padx=70, pady=10)
addressEntry.grid(row=6, column=4)

genLabel = tk.Label(aPat, text="Gender:", background="dark sea green", fg="black")
genCombo = ttk.Combobox(aPat, value = gens, width=17)
genCombo.set('Select Role')
genCombo.bind("<<ComboboxSelected>>")
genCombo['state'] = 'readonly'
genCombo.grid(row=7, column=4)
genLabel.grid(row=7, column=3, padx=30, pady=10)

phoneLabel = tk.Label(aPat, text="Phone no:", background="dark sea green", fg="black")
phoneEntry = tk.Entry(aPat, relief="groove", background="medium sea green")
phoneLabel.grid(row=8, column=3, padx=70, pady=10)
phoneEntry.grid(row=8, column=4)

emailLabel = tk.Label(aPat, text="Email:", background="dark sea green", fg="black")
emailEntry = tk.Entry(aPat, relief="groove", background="medium sea green")
emailLabel.grid(row=9, column=3, padx=70, pady=10)
emailEntry.grid(row=9, column=4)

btnAdd = tk.Button(aPat, text="Add Patient", command=putRecord, background="dark green", fg="black", font="8")
btnAdd.grid(columnspan=5)


aPat.mainloop()