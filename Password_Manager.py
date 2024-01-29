#Password manager

import customtkinter as ctk
import CTkMessagebox,CTkTable
import tkinter as tk
import mysql.connector

mydb = mysql.connector.connect(host = 'localhost',user='root',password="Apc@2007#CS")
mycursor = mydb.cursor()
mycursor.execute("USE password_manager")

#TABLE CONTENTS
mycursor.execute("Select * from manager")
value = list(mycursor.fetchall())

root = ctk.CTk()
root._set_appearance_mode("dark")
root.title("Password Manager")
root.state('zoomed')
ctk.set_default_color_theme("green")

def on_f11(event):
    if root.attributes('-fullscreen'):
        root.attributes('-fullscreen',False)
    else:
        root.attributes('-fullscreen',True)

root.bind('<F11>',on_f11)

def login():
    uid = "kami"
    pas = "1234"
    global frame

    def validate_login():
        if username_entry.get() == uid and pass_entry.get() == pas:
            frame.destroy()
            home_page() 
            return CTkMessagebox.CTkMessagebox(title="Password Manager",message="Successfully logged in",icon="check", option_1="Thanks")
            
            
        else:
            return CTkMessagebox.CTkMessagebox(title="Password Manager Error", message="Incorrect Username or password", icon="cancel")

    frame = ctk.CTkFrame(root,width=400,
                        height=600,  
                        corner_radius=0,
                        border_color="black")
    frame.pack(padx=500, pady=175)
    frame.pack_propagate(False)

    label = ctk.CTkLabel(
        master = frame,
        text='Login',
        font=('Khula Light', 36)
        )
    label.pack(pady=20)

    username_label = ctk.CTkLabel(
        master = frame,
        text='Username:',
        font=('Khula Light', 27))
    username_label.pack(padx=42,anchor=tk.W)

    username_entry = ctk.CTkEntry(
        master = frame,
        placeholder_text="User ID",
        width=250,
        height=50
    )
    username_entry.pack(padx=42,anchor=tk.W)

    
    
    pass_label = ctk.CTkLabel(
        master = frame,
        text='Password:',
        font=('Khula Light', 27))
    pass_label.place(relx=0.1,rely=0.45)

    pass_entry = ctk.CTkEntry(
        master = frame,
        placeholder_text="Password",
        width=250,
        height=50,
        corner_radius=10,
        show = '*'
    )
    pass_entry.place(relx=0.1,rely=0.54)

    login_button = ctk.CTkButton(
        master = frame,
        text="Login",
        fg_color=("green"),
        command=validate_login,
        font=("Khula Light",28),)
    login_button.place(relx=0.5,rely=0.8,anchor=tk.CENTER)
    pass_entry.bind('<Return>', lambda event=None: validate_login())

def add_password():
        global value,acc_entry,web_entry,pass2_entry,add_password_frame
        home_frame.destroy()
        add_password_frame = ctk.CTkFrame(
            master=root,
            width=400,
            height=600,
            corner_radius=0
            )
        add_password_frame.pack(padx=500, pady=175)
        add_password_frame.pack_propagate(False)

        add_password_label = ctk.CTkLabel(
            master = add_password_frame,
            text='Add New Password',
            font=('Khula Light', 36)
        )
        add_password_label.pack(pady=20)

        acc_entry = ctk.CTkEntry(
            master = add_password_frame,
            placeholder_text="Enter account name",
            width=250,
            height=50
        )
        acc_entry.pack(padx=42,anchor=tk.W)

        web_entry = ctk.CTkEntry(
            master=add_password_frame,
            placeholder_text="Website/App Name",
            width=250,
            height=50,
            corner_radius=10
        )
        web_entry.place(relx=0.1,rely=0.375)

        pass2_entry = ctk.CTkEntry(
            master = add_password_frame,
            placeholder_text="Password",
            width=250,
            height=50,
            corner_radius=10,
            show = '*'
        )
        pass2_entry.place(relx=0.1,rely=0.54)

        add_button = ctk.CTkButton(
            master = add_password_frame,
            text="Add",
            fg_color=("green"),
            command=append_pass,
            font=("Khula Light",28),)
        add_button.place(relx=0.5,rely=0.8,anchor=tk.CENTER)
        pass2_entry.bind('<Return>', lambda event=None: append_pass())
        
def append_pass():

    global value,web_entry,acc_entry,pass2_entry,add_password_frame

    
    print(value)

    web = web_entry.get()
    User = acc_entry.get()
    pswd = pass2_entry.get()
            
    #SQL PART

    mycursor.execute("USE password_manager")
    sql = "INSERT INTO manager (Website, Username, Password) VALUES (%s,%s,%s)"
    val = (web,User,pswd)
    mycursor.execute(sql,val)
    mydb.commit()

    value.append([web,User,pswd])
    tk.messagebox.showinfo("Password Manager", "Password sucessfully added")

    print(value)
    add_password_frame.destroy()
    home_page()
    

def home_page():
    global value,home_frame
    
    home_frame = tk.Frame(
        root,
        width=1920,
        height=1080,
        background="#121212")

    

    n = len(value)
    if n<8:
         n=7
    
    table = CTkTable.CTkTable(
        master=home_frame,
        row=n,
        column=3,
        values=value,
        font=("Khula Light",27),
        header_color=("#0047ab"),
        hover=True,
        height=900,
        width=1080,
        colors=['#121212','#121212'],
        border_color="White"
    )
    table.pack(padx = 20, pady = 70)

    
    addnew = ctk.CTkButton(
        master=home_frame,
        text="Add Password",
        fg_color=("green"),
        corner_radius=20,
        command=add_password,
        font=("Khula Light",28)
    )
    addnew.place(relx=0.45,rely=0.92)
    home_frame.pack()

login()
root.mainloop() 