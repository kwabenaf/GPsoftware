import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3, time, datetime, random, os
patient_db='patient.db'
my_conn = sqlite3.connect(patient_db)
cdb = my_conn.cursor()


#defining Patient forms  
def aPatr_form():
    print("Button clicked to open add Patient form")
    aPatr.destroy()
    os.system('python aPatr.py')

def vPatr_form():
    print("Button clicked to show all Patients")
    aPatr.destroy()
    os.system('python vPatr.py')
    
def dPatr_form():
    print("Button clicked to go to delete Patient form")
    aPatr.destroy()
    os.system('python dPatr.py')
    
def ePatr_form():
    print("Button clicked to go to edit Patient form")
    aPatr.destroy()
    os.system('python ePatr.py')
    
    
#defining Appointment forms
def aAppr_form():
    print("Button clicked to show Appointment menu")
    aPatr.destroy()
    os.system('python aAppr.py')

def vAppr_form():
    print("Button clicked to show all Appointments")
    aPatr.destroy()
    os.system('python vAppr.py')
    
def dAppr_form():
    print("Button clicked to go to delete Appointment form")
    aPatr.destroy()
    os.system('python dAppr.py')
    
def eAppr_form():
    print("Button clicked to go to edit Appointment form")
    aPatr.destroy()
    os.system('python eAppr.py')


#defining other forms
def mMenur_form():
    print("Button clicked to go to Main Menu")
    aPatr.destroy()
    os.system('python mMenur.py')

def ePassr_form():
    print("Button clicked to change password")
    aPatr.destroy()
    os.system('python ePassr.py')
    
def login_form():
    print("Button clicked to logout")
    aPatr.destroy()
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


aPatr = tk.Tk()   
aPatr.title('Add Patients')
aPatr.configure(background='sea green')

#centers the app on the screen
screen_width = aPatr.winfo_screenwidth()
screen_height = aPatr.winfo_screenheight() 

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

aPatr.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

#submenu labels and positioning
menu = Menu(aPatr)
aPatr.config(menu=menu)

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
titleLabel = tk.Label(aPatr, text="Adding A New Patient Record", background="sea green", fg="black", font="7")
titleLabel.grid(row=0, column=3, columnspan=2, padx=10, pady=10)

fnameLabel = tk.Label(aPatr, text="Firstname:", background="dark sea green", fg="black")
fnameEntry = tk.Entry(aPatr, relief="groove", background="medium sea green")
fnameLabel.grid(row=3, column=3, padx=70, pady=10)
fnameEntry.grid(row=3, column=4)

snameLabel = tk.Label(aPatr, text="Surname:", background="dark sea green", fg="black")
snameEntry = tk.Entry(aPatr, relief="groove", background="medium sea green")
snameLabel.grid(row=4, column=3, padx=70, pady=10)
snameEntry.grid(row=4, column=4)

dobLabel = tk.Label(aPatr, text="DoB:", background="dark sea green", fg="black")
dobEntry = tk.Entry(aPatr, relief="groove", background="medium sea green")
dobLabel.grid(row=5, column=3, padx=70, pady=10)
dobEntry.grid(row=5, column=4)

addressLabel = tk.Label(aPatr, text="Address:", background="dark sea green", fg="black")
addressEntry = tk.Entry(aPatr, relief="groove", background="medium sea green")
addressLabel.grid(row=6, column=3, padx=70, pady=10)
addressEntry.grid(row=6, column=4)

genLabel = tk.Label(aPatr, text="Gender:", background="dark sea green", fg="black")
genCombo = ttk.Combobox(aPatr, value = gens, width=17)
genCombo.set('Select Role')
genCombo.bind("<<ComboboxSelected>>")
genCombo['state'] = 'readonly'
genCombo.grid(row=7, column=4)
genLabel.grid(row=7, column=3, padx=30, pady=10)

phoneLabel = tk.Label(aPatr, text="Phone no:", background="dark sea green", fg="black")
phoneEntry = tk.Entry(aPatr, relief="groove", background="medium sea green")
phoneLabel.grid(row=8, column=3, padx=70, pady=10)
phoneEntry.grid(row=8, column=4)

emailLabel = tk.Label(aPatr, text="Email:", background="dark sea green", fg="black")
emailEntry = tk.Entry(aPatr, relief="groove", background="medium sea green")
emailLabel.grid(row=9, column=3, padx=70, pady=10)
emailEntry.grid(row=9, column=4)

btnAdd = tk.Button(aPatr, text="Add Patient", command=putRecord, background="dark green", fg="black", font="8")
btnAdd.grid(columnspan=5)

aPatr.mainloop()
