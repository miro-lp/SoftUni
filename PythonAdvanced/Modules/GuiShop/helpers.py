from SoftUni.SoftUni.PythonAdvanced.Modules.GuiShop.canvas import tk


def clean_screen():
    for el in tk.grid_slaves():
        el.destroy()
