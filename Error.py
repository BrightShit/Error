#My coding skills got you climbing hills
from tkinter import *
import customtkinter
import os
import random
import pyperclip as pc
from tkinter import messagebox as mb
from cryptography.fernet import Fernet
global encrypted
customtkinter.set_appearance_mode("Light")
window=customtkinter.CTk()
# Making all the widgets for thte password saver
window.title("Password saver for me")
window.geometry("750x420")
# Logic (The hard part)
#----------------------------------------------------
def main_func():
    #Add Passwords Function
    def add():
        for i in window.winfo_children():
            i.destroy()
        password=customtkinter.CTkEntry(window,
                                    width=230
                                        ,border_width=0.5
                                            ,placeholder_text="Password"
                                                ,placeholder_text_color="Silver")
        user=customtkinter.CTkEntry(window,
                                        width=230,
                                            border_width=0.5
                                                ,placeholder_text="User"
                                                    ,placeholder_text_color="Silver")
        platform_=customtkinter.CTkEntry(window,
                                        width=490,
                                            border_width=0.5
                                                ,placeholder_text="Platform"
                                                    ,placeholder_text_color="Silver")
        password.place(x=450,y=35) #I wasn't able to calculate this by myself
        user.place(x=192,y=35)
        platform_.place(x=192,y=70)
        main_func()
        def logic():
            #Opens the file and writes the user information inside it
            #Guardian
            if platform_.get() == "" or user.get() == "" or password.get() == "":
                mb.showerror("WRONG INPUT","Please Make sure to enter all the fields \nIf you don't have a username/password Enter \'None\'")
                return
            file = open("pass.txt","a")
            write_platform_=file.write("Platform: "+platform_.get()+" | ")
            write_email=file.write("Username/Email: "+user.get()+" | ")
            write_password=file.write("Password: "+password.get()+"\n")
            file.close()
            key = Fernet.generate_key()

            with open("MyKey.key","wb") as mykey:

                mykey.write(key)
            ############################################ddddddddddddddddddddddddddddddddddddddddddd
            with open("MyKey.key","rb") as mykey:

                key = mykey.read()

            f = Fernet(key)
            with open("pass.txt","rb") as original_file:

                original = original_file.read()

            encrypted = f.encrypt(original)
            #########################################3
            with open("enc_passwords.txt","wb") as encrypted_file:

                encrypted_file.write(encrypted)

            f = Fernet(key)

            with open("enc_passwords.txt","rb") as encrypted_file:

                encrypted=encrypted_file.read()

            decrypted=f.decrypt(encrypted)
            file=open("pass.txt","wb")
            file.write(encrypted)
            
            
                #Clear Fields
        def clear_field():
            for i in window.winfo_children():
                i.destroy()
                
            add()
        def generate_password():
            for i in range(12):
                a = random.choice("Q!w!E!r!T!y!U!i!O!p!A!s!D!fGhJkLzXcVbNm1234567890")
                password.insert(i,a)
            pc.copy(password.get())
        save=customtkinter.CTkButton(window,text="Save",
                                    command=logic
                                        ,fg_color='red',
                                                hover_color="white"
                                                        ,width=490).place(x=192,y=105)
        first_generate_button=customtkinter.CTkButton(window
                                                        ,width=490
                                                            ,text="Generate Random Password"
                                                                ,fg_color="red"
                                                                    ,hover_color="white"
                                                                        ,command=generate_password).place(x=192,y=105+35)
        clear_fields=customtkinter.CTkButton(window
                                                ,width=490
                                                    ,text="Clear Fields"
                                                        ,fg_color="Red"
                                                            ,hover_color="white"
                                                                ,command=clear_field).place(x=192,y=105+70)
    #--------------------------------------------------------------------------------

    def generate():
            for i in window.winfo_children():
                i.destroy()
            main_func()
            password_label2=customtkinter.CTkLabel(window,
                                                        text="New Password")
            password_label2.place(x=191,y=65)  
            rand_password=customtkinter.CTkEntry(window,
                                                    border_width=0.5)
            rand_password.place(x=192,y=150-65)
            for i in range(12):
                a = random.choice("QwErTyUiOpAsDfGhJkLzXcVbNm1234567890")
                rand_password.insert(i,a)
                pc.copy(rand_password.get())

    #---------------------------------------------------------------

    #----------------------------------------------------------------
    #----------------------------------------------------------------------
    #Not finished Need to add encryption
    def add_passport():
        for i in window.winfo_children():
            i.destroy()
        name=customtkinter.CTkEntry(window
                                    ,placeholder_text="Enter Surname"
                                        ,placeholder_text_color="Silver")
        passport_no=customtkinter.CTkEntry(window
                                        ,placeholder_text="Enter Given name",
                                            placeholder_text_color="Silver")
        nation=customtkinter.CTkEntry(window
                                    ,placeholder_text="Nationality"
                                        ,placeholder_text_color="Silver")
        date_of_birth=customtkinter.CTkEntry(window
                                            ,placeholder_text="Date of birth"
                                                ,placeholder_text_color="Silver")
        date_of_issue=customtkinter.CTkEntry(window
                                            ,placeholder_text="Date of issue"
                                                ,placeholder_text_color="Silver")
        authority=customtkinter.CTkEntry(window
                                        ,placeholder_text="Authority"
                                                ,placeholder_text_color="Silver")
        name.place(x=200,y=35)
        passport_no.place(x=370,y=35)
        nation.place(x=540,y=35)
        date_of_birth.place(x=200,y=70)
        date_of_issue.place(x=370,y=70)
        authority.place(x=540,y=70)
        # The space between x + 170 and y supposed to be + 35
        main_func()
        # platform_: Iphone | Username/Email: Nitay | Password: pro
    #All the Buttons
    #Saved button
    def saved():

        file1 = open("pass.txt","rb")
        new_window=customtkinter.CTk()
        saved_passwords=customtkinter.CTkLabel(new_window,text=decrypted)
        saved_passwords.pack()
        new_window.mainloop()
        return
    
    saved=customtkinter.CTkButton(window,command=saved
                                ,fg_color="red",
                                    hover_color="white",
                                        text="Saved Passwords").place(x=1,y=0)
    # Generate password button
    #------------------------------------------------------------------------
    generate_button=customtkinter.CTkButton(window,text="Generate Password",
                                            command=generate,height=28,
                                                fg_color="red",
                                                    hover_color="white").place(x=1,y=35)
    #------------------------------------------------------------------------
    #Save button
    #-------------------------------------------------
    add_password=customtkinter.CTkButton(window
                                        ,text="Add Password"
                                            ,fg_color="red"
                                                ,hover_color="white"
                                                    ,command=add).place(x=1,y=70)
    #-------------------------------------------------
    #Add Password Button
    add_passports=customtkinter.CTkButton(window,text="Add Passport"
                                        ,fg_color="red"
                                            ,hover_color="white"
                                                ,command=add_passport).place(x=1,y=105)
    #Main Loop
main_func()
window.mainloop()
