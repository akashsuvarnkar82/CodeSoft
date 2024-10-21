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

    s = []
        
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    if plen > len(s):
        messagebox.showerror("Invalid Input","Password length exceeds available character pool.")
        return    

    random_password = "".join(random.sample(s, plen))
    
    password_textbox.delete(1.0, END)
    password_textbox.insert(END, random_password)
    
    copy_button.config(state=NORMAL)
    
    global generated_password
    generated_password = random_password

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(generated_password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

root = Tk()
root.title("Password Generator")
root.geometry("400x300")
root.config(bg="#E8E8E8")

font_style = ("Helvetica Neue", 16, "bold")
button_font = ("Helvetica Neue", 14)

# Entry for password length
entry = Entry(root, font=font_style, bg="white", fg="black", borderwidth=1, relief="solid")
entry.pack(pady=20)

# Button to generate password
generate_button = Button(root, text="Generate Password", command=generate_password, font=button_font, bg="#0078E7", fg="white", activebackground="#005BB5", activeforeground="white", borderwidth=0)
generate_button.pack(pady=10)

password_frame = Frame(root, bg="#E8E8E8")
password_frame.pack(pady=10)

password_label = Label(password_frame, text="Your Password:", font=("Helvetica Neue", 14), bg="#E8E8E8", fg="black")
password_label.pack(anchor=CENTER, pady=5)

password_textbox = Text(password_frame, height=1, width=30, font=("Helvetica Neue", 14), borderwidth=1, relief="solid", wrap=NONE)
password_textbox.pack(anchor=CENTER, pady=5)

# Copy Button (initially disabled) placed inside the same frame and centered
copy_button = Button(password_frame, text="Copy", command=copy_to_clipboard, font=("Helvetica Neue", 10), bg="#E8E8E8", fg="blue", state=DISABLED)
copy_button.pack(anchor=CENTER, pady=5)

root.mainloop()
