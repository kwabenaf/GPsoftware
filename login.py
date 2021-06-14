import tkinter as tk
from tkinter import *
import sqlite3, os
staff_db ='staff.db'
my_conn = sqlite3.connect(staff_db)
cdb = my_conn.cursor()

rand_listPM = list(range(10, 20))

rand_listDnN = list(range(20, 60))

rand_listRecep = list(range(60, 100))


def login():

    uname = unameEntry.get()
    
    
    if uname.startswith("PM"):
        print("PM")
        
        while True:
            uname
            password = passEntry.get()
            
            find_user = ("SELECT * FROM staffDb WHERE username = ? AND password = ?")
            cdb.execute(find_user, [(uname), (password)])
            result = cdb.fetchall()
            
            if result:
                for i in result:
                    login_form.destroy()
                    os.system('python mMenu.py')
                    break
            else:
                tk.messagebox.showerror(title = 'Error', message = "Username or password was incorrect")
                break
            
    elif uname.startswith("D") or uname.startswith("N"):
        print("User has a Doctor or Nurse account")
        
        while True:
            uname = unameEntry.get()
            password = passEntry.get()
            
            find_user = ("SELECT * FROM staffDb WHERE username = ? AND password = ?")
            cdb.execute(find_user, [(uname), (password)])
            result = cdb.fetchall()
            
            if result:
                for i in result:
                    login_form.destroy()
                    os.system('python mMenudn.py')
                    break
            else:
                tk.messagebox.showerror(title = 'Error', message = "Username or password was incorrect")
                break
    
    elif uname.startswith("R"):
        print("User has a Receptionist account")
        
        while True:
            uname = unameEntry.get()
            password = passEntry.get()
            
            find_user = ("SELECT * FROM staffDb WHERE username = ? AND password = ?")
            cdb.execute(find_user, [(uname), (password)])
            result = cdb.fetchall()
            
            if result:
                for i in result:
                    login_form.destroy()
                    os.system('python mMenur.py')
                    break
            else:
                tk.messagebox.showerror(title = 'Error', message = "Username or password was incorrect")
                break    
        
    else:
        tk.messagebox.showerror(title = 'Error', message = "ERROR")
        print("probabaly didnt work")
    
    
#setting form size        
app_width = 300
app_height = 200


login_form = Tk()
login_form.title("Login")
login_form.configure(background='sea green')

#centering the form
screen_width = login_form.winfo_screenwidth()
screen_height = login_form.winfo_screenheight() 

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

login_form.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


Label(login_form, text="Username", background="dark sea green", fg="black").place(x=30, y=20)
Label(login_form, text="Password", background="dark sea green", fg="black").place(x=30, y=50)

unameEntry = tk.Entry(login_form, relief="groove", background="medium sea green")
unameEntry.place(x=120, y=20)

passEntry = tk.Entry(login_form, relief="groove", background="medium sea green")
passEntry.place(x=120, y=50)
passEntry.config(show="*")

Button(login_form, text="Login", command = login, height = 3, width = 13).place(x=100, y=100)

login_form.mainloop()