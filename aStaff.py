import tkinter as tk
from tkinter import *
from tkinter import ttk
import sqlite3, time, datetime, os, random
from random import *
staff_db='staff.db'
my_conn = sqlite3.connect(staff_db)
cdb = my_conn.cursor()


#defining staff all forms
def aStaff_form():
    print("Button clicked to show add Staff form")
    aStaff.destroy()
    os.system('python aStaff.py')

def vStaff_form():
    print("Button clicked to show all Staff members")
    aStaff.destroy()
    os.system('python vStaff.py')
    
def dStaff_form():
    print("Button clicked to go to delete Staff form")
    aStaff.destroy()
    os.system('python dStaff.py')
    
def eStaff_form():
    print("Button clicked to go to edit Staff form")
    aStaff.destroy()
    os.system('python eStaff.py')
    
#defining Patient forms  
def aPat_form():
    print("Button clicked to open add Patient form")
    aStaff.destroy()
    os.system('python aPat.py')

def vPat_form():
    print("Button clicked to show all Patients")
    aStaff.destroy()
    os.system('python vPat.py')
    
def dPat_form():
    print("Button clicked to go to delete Patient form")
    aStaff.destroy()
    os.system('python dPat.py')
    
def ePat_form():
    print("Button clicked to go to edit Patient form")
    aStaff.destroy()
    os.system('python ePat.py')
    
    
#defining Appointment forms
def aApp_form():
    print("Button clicked to show Appointment menu")
    aStaff.destroy()
    os.system('python aApp.py')

def vApp_form():
    print("Button clicked to show all Appointments")
    aStaff.destroy()
    os.system('python vApp.py')
    
def dApp_form():
    print("Button clicked to go to delete Appointment form")
    aStaff.destroy()
    os.system('python dApp.py')
    
def eApp_form():
    print("Button clicked to go to edit Appointment form")
    aStaff.destroy()
    os.system('python eApp.py')
   
#defining other forms
def editpass_form():
    print("Button clicked to change password")
    aStaff.destroy()
    os.system('python editpass.py')
    
def login_form():
    print("Button clicked to logout")
    aStaff.destroy()
    os.system('python login.py')


#clear all the form texts
def clear_aStaff():
    fnameEntry.delete(0, END)
    snameEntry.delete(0, END)
    roleCombo.set('Select Role')
    ageEntry.delete(0, END)


def create_table():
    cdb.execute("""CREATE TABLE IF NOT EXISTS staffDb (
                idno INTEGER PRIMARY KEY,
                datestamp VARCHAR(10) NOT NULL,
                username VARCHAR(10) NOT NULL,
                password VARCHAR(20) NOT NULL,
                firstname VARCHAR(20) NOT NULL,
                surname VARCHAR(20) NOT NULL,
                role VARCHAR(20) NOT NULL,
                age INTEGER NOT NULL)""")



roles = [
    "Practice Manager",
    "Assistant Practice Manager",
    "Doctor",
    "Nurse",
    "Receptionist"
    ]

#creating a list of numbers for userID 
rand_listPM = list(range(10, 20))

rand_listDnN = list(range(20, 60))

rand_listRecep = list(range(60, 100))


def putRecord():

    with my_conn:
        currtime = time.time()
        date = datetime.datetime.fromtimestamp(currtime).strftime('%x')
        password = "Password123"
        firstname = fnameEntry.get().title().rstrip()
        surname = snameEntry.get().title().rstrip()
        role = roleCombo.get()
        age = ageEntry.get()
        
        #check entry is valid
        try:
            if firstname.isalpha() and surname.isalpha() and age.isnumeric():
                
               #the user will be giving a random number from a range depending on the role selected       
                if role == roles[0]:
                    username = "PM" + firstname.lower()[0] + surname.lower()[0] + str(choice(rand_listPM))
                elif role == roles[1]:
                    username = "PM" + firstname.lower()[0] + surname.lower()[0] + str(choice(rand_listPM))
                elif role == roles[2]:
                    username = "D" + firstname.lower()[0] + surname.lower()[0] + str(choice(rand_listDnN))
                elif role == roles[3]:
                    username = "N" + firstname.lower()[0] + surname.lower()[0] + str(choice(rand_listDnN))
                else:
                    username = "R" + firstname.lower()[0] + surname.lower()[0] + str(choice(rand_listRecep))
                            
                    
                cdb.execute('''INSERT INTO staffDb (
                                                    datestamp,
                                                    username,
                                                    password,
                                                    firstname,
                                                    surname,
                                                    role,
                                                    age) VALUES (?, ?, ?, ?, ?, ?, ?)''',
                          (date, username, password, firstname, surname, role, age))
                my_conn.commit()
                
                tk.messagebox.showinfo(title = 'Info', message = "Your username is: " + ((username) + " and password: " + (password)))
                
                print("Added to DB")

                print("The following has been added to the DB " + staff_db +"\n")
                print("Username: " + username)
                print("Password: " + password)
                print("FirstName: " + firstname)
                print("Surname: " + surname)
                print("Role: " + role)
                print("Age: " + age)
                clear_aStaff()

            else:
                tk.messagebox.showerror(title = 'Invaild', message = "Invaild data, please try again")
        except ValueError:
           pass
            
        
    
#creates the table    
create_table()

#application dimensions
app_width = 500
app_height = 600


aStaff = tk.Tk()
aStaff.title('Add Staff')
aStaff.configure(background='sea green')

#centers the app on the screen
screen_width = aStaff.winfo_screenwidth()
screen_height = aStaff.winfo_screenheight() 

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

aStaff.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

#submenu labels and positioning
menu = Menu(aStaff)
aStaff.config(menu=menu)

homeSubmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Home", menu=homeSubmenu)
homeSubmenu.add_command(label="Menu")
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

#form labels and buttons
titleLabel = tk.Label(aStaff, text="Creating New Staff Member", background="sea green", fg="black")
titleLabel.place(x=130, y=0)

fnameLabel = tk.Label(aStaff, text="Enter firstname:", background="dark sea green", fg="black")
fnameEntry = tk.Entry(aStaff, relief="groove", background="medium sea green")
fnameLabel.grid(row=2, column=3, padx=60, pady=30)
fnameEntry.grid(row=2, column=4)

snameLabel = tk.Label(aStaff, text="Enter surname:", background="dark sea green", fg="black")
snameEntry = tk.Entry(aStaff, relief="groove", background="medium sea green")
snameLabel.grid(row=4, column=3, padx=30, pady=30)
snameEntry.grid(row=4, column=4)

roleLabel = tk.Label(aStaff, text="Enter role:", background="dark sea green", fg="black")
roleCombo = ttk.Combobox(aStaff, value = roles, width=17)
roleCombo.set('Select Role')
roleCombo.bind("<<ComboboxSelected>>")
roleCombo['state'] = 'readonly'
roleCombo.grid(row=6, column=4)
roleLabel.grid(row=6, column=3, padx=30, pady=30)


ageLabel = tk.Label(aStaff, text="Enter age:", background="dark sea green", fg="black")
ageEntry = tk.Entry(aStaff, relief="groove", background="medium sea green")
ageLabel.grid(row=8, column=3, padx=30, pady=30)
ageEntry.grid(row=8, column=4)

btnSubmit = tk.Button(aStaff, text="Create", command = putRecord, background="dark green", fg="black")
btnSubmit.grid(columnspan=5)



aStaff.mainloop()