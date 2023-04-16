from tkinter import *
from tkinter import messagebox
from tkinter import ttk


root = Tk()
root.title('Login')

style = ttk.Style()
# # Theme
style.theme_use("clam")
style.configure('TButton', font=('Sans', 10))


root_width = 280
root_height = 120

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width / 2) - (root_width / 2)
y = (screen_height / 2) - (root_height / 2)

root.geometry(f'{root_width}x{root_height}+{int(x)}+{int(y)}')


root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=5)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=5)

a_en = Label(root, text="User", font='sans 12')
a_en.grid(column=0, row=0, pady=(10, 0))
b_en = Label(root, text="Password", font='sans 12')
b_en.grid(column=0, row=1)

a_en_entrys = ttk.Entry(root, textvariable=StringVar(), font='sans 12', width=20)
a_en_entrys.grid(column=1, row=0, pady=(10, 0))
b_en_entrys = ttk.Entry(root, show='*', textvariable=StringVar(), font='sans 12', width=20)
b_en_entrys.grid(column=1, row=1)


# import shoftware
def open_app():
    pass

def open_app_2():
    pass

# close app
def close():
    root.destroy()

# check loginand login if True
def connect():
    if a_en_entrys.get() == 'user' and b_en_entrys.get() == 'psw':
        open_app()

    elif a_en_entrys.get() == 'user2' and b_en_entrys.get() == 'psw2':
        open_app_2()

    else:
        messagebox.showerror('Login', 'Try again...!!!')

# check loginand login if True, bind to ENTER button
def connect_2(e):
    if a_en_entrys.get() == 'user' and b_en_entrys.get() == 'psw':
        open_app() and root.destroy()

    elif a_en_entrys.get() == 'user2' and b_en_entrys.get() == 'psw2':
        open_app_2() and root.destroy()

    else:
        messagebox.showerror('Login', 'Try again...!!!')

# close app, BIND to ESC button
def close_2(e):
    root.destroy()


login_button = ttk.Button(root, text="OK", command=connect, width=6)
login_button.grid(column=1, row=2, padx=(5, 0))
cancel_button = ttk.Button(root, text="Cancel", command=close, width=6)
cancel_button.grid(column=1, row=2, padx=(125, 0))

root.bind('<Return>', connect_2)
root.bind('<Escape>', close_2)

mainloop()
