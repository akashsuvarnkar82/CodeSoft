from tkinter import *

root = Tk()
root.geometry("320x400") 
root.title("Calculator BY Akash")

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Error"
        scvalue.set(value)
        screen.update()
            
    elif text == "C":
        scvalue.set("") 
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 20 bold", bd=5, relief=SUNKEN)
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

# First row of buttons (1, 2, 3, +)
f = Frame(root, bg="grey")
b = Button(f, text="1", padx=20, pady=20, font="lucida 15 bold")
b.grid(row=1, column=0)
b.bind("<Button-1>", click)

b = Button(f, text="2", padx=20, pady=20, font="lucida 15 bold")
b.grid(row=1, column=1)
b.bind("<Button-1>", click)

b = Button(f, text="3", padx=20, pady=20, font="lucida 15 bold")
b.grid(row=1, column=2)
b.bind("<Button-1>", click)

b = Button(f, text="+", padx=18, pady=20, font="lucida 15 bold")
b.grid(row=1, column=3)
b.bind("<Button-1>", click)
f.pack()

# Second row of buttons (4, 5, 6, -)
f = Frame(root, bg="grey")
b = Button(f, text="4", padx=20, pady=20, font="lucida 15 bold")
b.grid(row=2, column=0)
b.bind("<Button-1>", click)

b = Button(f, text="5", padx=20, pady=20, font="lucida 15 bold")
b.grid(row=2, column=1)
b.bind("<Button-1>", click)

b = Button(f, text="6", padx=20, pady=20, font="lucida 15 bold")
b.grid(row=2, column=2)
b.bind("<Button-1>", click)

b = Button(f, text="-", padx=20, pady=20, font="lucida 15 bold")
b.grid(row=2, column=3)
b.bind("<Button-1>", click)
f.pack()

# Third row of buttons (7, 8, 9, *)
f = Frame(root, bg="grey")
b = Button(f, text="7", padx=21, pady=20, font="lucida 15 bold")
b.grid(row=3, column=0)
b.bind("<Button-1>", click)

b = Button(f, text="8", padx=20, pady=20, font="lucida 15 bold")
b.grid(row=3, column=1)
b.bind("<Button-1>", click)

b = Button(f, text="9", padx=20, pady=20, font="lucida 15 bold")
b.grid(row=3, column=2)
b.bind("<Button-1>", click)

b = Button(f, text="*", padx=19, pady=20, font="lucida 15 bold")
b.grid(row=3, column=3)
b.bind("<Button-1>", click)
f.pack()

# Fourth row of buttons (Clear, 0, =, /)
f = Frame(root, bg="grey")
b = Button(f, text="C", padx=20, pady=20, font="lucida 15 bold")
b.grid(row=4, column=0)
b.bind("<Button-1>", click)

b = Button(f, text="0", padx=20, pady=20, font="lucida 15 bold")
b.grid(row=4, column=1)
b.bind("<Button-1>", click)

b = Button(f, text="=", padx=19, pady=20, font="lucida 15 bold")
b.grid(row=4, column=2)
b.bind("<Button-1>", click)

b = Button(f, text="/", padx=20, pady=20, font="lucida 15 bold")
b.grid(row=4, column=3)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()

