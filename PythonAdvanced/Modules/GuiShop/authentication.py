import json
from tkinter import Button, Entry, Label
from SoftUni.SoftUni.PythonAdvanced.Modules.GuiShop.canvas import tk
from SoftUni.SoftUni.PythonAdvanced.Modules.GuiShop.helpers import clean_screen
from SoftUni.SoftUni.PythonAdvanced.Modules.GuiShop.products import render_products


def register(**user):
    user.update({"products": []})
    with open("db/users.txt", "a") as f:
        f.write(json.dumps(user))
        f.write("\n")
    with open("db/user_credentials.txt", "a") as f:
        f.write(f"{user.get('username')}, {user.get('password')}")
        f.write("\n")
    render_login()


def login(username, password):
    with open("db/user_credentials.txt", "r") as f:
        lines = f.readlines()
        for l in lines:
            user, pswrd = l[:-1].split(", ")
            if user == username and pswrd == password:
                with open("db/current_user.txt", "w") as f:
                    f.write(user)
                render_products()
                return
        render_login(errors=True)


def render_register():
    clean_screen()
    Label(text="username").grid(row=0, column=0)
    user_name = Entry(tk, text="username")
    user_name.grid(row=0, column=1)
    Label(text="password").grid(row=1, column=0)
    password = Entry(tk, show="*")
    password.grid(row=1, column=1)
    Label(text="first name").grid(row=2, column=0)
    first_name = Entry(tk)
    first_name.grid(row=2, column=1)
    Label(text="last name").grid(row=3, column=0)
    last_name = Entry(tk)
    last_name.grid(row=3, column=1)
    Button(tk, text="Register",
           command=lambda: register(
               username=user_name.get(),
               password=password.get(),
               first_name=first_name.get(),
               last_name=last_name.get())
           ).grid(row=4, column=1)


def render_login(errors=None):
    clean_screen()
    Label(text="username").grid(row=0, column=0)
    user_name = Entry(tk)
    user_name.grid(row=0, column=1)
    Label(text="password").grid(row=1, column=0)
    password = Entry(tk)
    password.grid(row=1, column=1)
    Button(tk, text="Enter", command=lambda: login(user_name.get(), password.get())).grid(row=2, column=1)
    if errors:
        Label(text="Invalid username or password").grid(row=4, column=0)


def render_main_enter_screen():
    login_btn = Button(tk, text="Login", bg="green", fg="white", command=render_login)
    login_btn.grid(row=0, column=0, padx=200, pady=100)
    Button(tk, text="Register", bg="yellow", command=render_register).grid(row=0, column=1)
