import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3, os
staff_db ='staff.db'
my_conn = sqlite3.connect(staff_db)
cdb = my_conn.cursor()

#defining staff all forms
def aStaff_form():
    print("Button clicked to show add Staff form")
    editpass.destroy()
    os.system('python aStaff.py').pack()

def vStaff_form():
    print("Button clicked to show all Staff members")
    editpass.destroy()
    os.system('python vStaff.py').pack()
    
def dStaff_form():
    print("Button clicked to go to delete Staff form")
    editpass.destroy()
    os.system('python dStaff.py').pack()
    
def eStaff_form():
    print("Button clicked to go to edit Staff form")
    editpass.destroy()
    os.system('python eStaff.py').pack()
    
#defining Patient forms  
def aPat_form():
    print("Button clicked to open add Patient form")
    editpass.destroy()
    os.system('python aPat.py').pack()

def vPat_form():
    print("Button clicked to show all Patients")
    editpass.destroy()
    os.system('python vPat.py').pack()
    
def dPat_form():
    print("Button clicked to go to delete Patient form")
    editpass.destroy()
    os.system('python dPat.py').pack()
    
def ePat_form():
    print("Button clicked to go to edit Patient form")
    editpass.destroy()
    os.system('python ePat.py').pack()

def ePatmeddn_form():
    print("Button clicked to go to edit Patient medical records")
    editpass.destroy()
    os.system('python ePatmeddn.py').pack()
    
#defining Appointment forms
def aApp_form():
    print("Button clicked to show Appointment menu")
    editpass.destroy()
    os.system('python aApp.py').pack()

def vApp_form():
    print("Button clicked to show all Appointments")
    editpass.destroy()
    os.system('python vApp.py').pack()
    
def dApp_form():
    print("Button clicked to go to delete Appointment form")
    editpass.destroy()
    os.system('python dApp.py').pack()
    
def eApp_form():
    print("Button clicked to go to edit Appointment form")
    editpass.destroy()
    os.system('python eApp.py').pack()


#defining other forms
def mMenu_form():
    print("Button clicked to go to Main Menu")
    editpass.destroy()
    os.system('python mMenu.py').pack()

def editpass_form():
    print("Button clicked to change password")
    aStaff.destroy()
    os.system('python editpass.py').pack()
    
def login_form():
    print("Button clicked to logout")
    aStaff.destroy()
    os.system('python login.py').pack()


def updatepass():
    
    idno = idnoEntry.get() 
    
    cdb.execute("""UPDATE staffDb SET
            password = :pass,
            
            WHERE idno = :idno""",
            {'pass': changeEntry.get(),
                    
            'idno': idnorec
            })
    
    my_conn.commit()
    my_conn.close()
    
    tk.messagebox.showinfo(title = 'Updated', message = "Password has been updated")
    
    

#setting form size        
app_width = 300
app_height = 200

editpass = Tk()
editpass.title("Edit Password")
editpass.configure(background='sea green')

#centering the form
screen_width = editpass.winfo_screenwidth()
screen_height = editpass.winfo_screenheight() 

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)



editpass.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


menu = Menu(editpass)
editpass.config(menu=menu)

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

#edit password label and entry
changeLabel = tk.Label(editpass, text="Change Password", background="dark sea green", fg="black")
changeLabel.place(x=20, y=40)

changeEntry = tk.Entry(editpass, relief="groove")
changeEntry.place(x=140, y=40)

submitbtn = tk.Button(editpass, text="Confirm", command = updatepass, height = 2, width = 13).place(x=100, y=100)

editpass.mainloop()