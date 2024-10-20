import string
import random
from tkinter import *
from tkinter import messagebox

def generate_password():
    try:
        plen = int(entry.get())
        if plen < 1:
            raise ValueError("Password length must be greater than 0.")
        
    except ValueError:
        messagebox.showerror("Invalid Input","Please enter a valid number for password length.")
        return

    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    s =[]
        
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    if plen > len(s):
        messagebox.showerror("Invalid Input","Password length exceed available character pool.")
        return    

    random_password = "".join(random.sample(s,plen))
    password_label.config(text=f"Your Password is : {random_password}")

root = Tk()
root.title("Passwod Generator")
root.geometry("600x400")
root.config(bg="#E8E8E8")

font_style = ("Helvetica Neue",18,"bold")
button_font = ("Helvetica Neue",16)

label = Label(root,text="Enter password length : ",font=font_style,bg="#E8E8E8",fg="black")
label.pack(pady=10)

entry = Entry(root,font=font_style,bg="white",fg="black",borderwidth=1 ,relief="solid")
entry.pack(pady=10)

generate_button = Button(root,text="Generate Password",command=generate_password,font=button_font,bg="#0078E7",fg="white",activebackground="#005BB5",activeforeground="white",borderwidth=0)
generate_button.pack(pady=20)

password_label = Label(root, text="", font=font_style, bg="#E8E8E8", fg="black")
password_label.pack(pady=20)


root.mainloop()


    
