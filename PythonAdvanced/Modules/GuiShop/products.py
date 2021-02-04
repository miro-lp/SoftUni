from tkinter import Button, Label
from SoftUni.SoftUni.PythonAdvanced.Modules.GuiShop.helpers import clean_screen
import json
from SoftUni.SoftUni.PythonAdvanced.Modules.GuiShop.canvas import tk
from PIL import Image, ImageTk
import os

base_folder = os.path.dirname(__file__)


def buy_product(button):
    _, product_id = button.cget("text").split()
    product_id = int(product_id)
    logged_user = None
    with open("db/current_user.txt", "r") as f:
        logged_user = f.read()
    with open("db/users.txt", "r+") as f:
        users = f.readlines()
        f.seek(0)
        for user in users:
            current = json.loads(user)
            if current.get("username") == logged_user:
                current["products"].append(product_id)
            f.write(json.dumps(current))
            f.write("\n")
    with open("db/products.txt", "r+") as f:
        products = f.readlines()
        f.seek(0)
        for p in products:
            product_dict = json.loads(p)
            if product_dict["id"] == product_id:
                product_dict["count"] -= 1
            f.write(json.dumps(product_dict))
            f.write("\n")
    render_products()


def render_products():
    clean_screen()
    with open("db/products.txt", "r") as p:
        products = p.readlines()
        counter = 0
        for product in products:
            current_prd = json.loads(product)
            Label(text=current_prd.get("name")).grid(row=0, column=counter)
            image = Image.open(os.path.join(os.path.join(base_folder, "images"), current_prd.get("img_path")))
            image = image.resize((160, 100))
            photo = ImageTk.PhotoImage(image)
            img_label = Label(image=photo)
            img_label.image = photo
            img_label.grid(row=2, column=counter)
            button = Button(tk, text=f"Buy {current_prd.get('id')}")
            button.configure(command=lambda b=button: buy_product(b))
            button.grid(row=4, column=counter)
            Label(text = current_prd.get("count")).grid(row=3, column = counter)
            counter += 1
