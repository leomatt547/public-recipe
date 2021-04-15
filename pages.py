import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from PIL import ImageTk, Image
import login
import pandas as pd

class homePage :
    def __init__(self, root):
        self.root = root
        #setting title
        root.title("undefined")
        #setting window size
        width=951
        height=703
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background = "white")

        menuBar = tk.Frame(master = root, height = 50, width = 951, bg = "pink")
        menuBar.pack()

        labelTitle=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        labelTitle["font"] = ft
        labelTitle["fg"] = "#333333"
        labelTitle["justify"] = "center"
        labelTitle["text"] = "Public Recipe"
        labelTitle["bg"] = "pink"
        labelTitle.config(font="Courier")
        labelTitle.place(x=378,y=10,width=205,height=30)

        labelSignUp=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        labelSignUp["font"] = ft
        labelSignUp["fg"] = "#333333"
        labelSignUp["justify"] = "center"
        labelSignUp["text"] = "Sign Up"
        labelSignUp["bg"] = "pink"
        labelSignUp.place(x=760,y=10,width=70,height=25)
        labelSignUp.bind("<Button-1>", self.gotoRegister)

        labelLogin=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        labelLogin["font"] = ft
        labelLogin["fg"] = "#333333"
        labelLogin["justify"] = "center"
        labelLogin["text"] = "Login"
        labelLogin["bg"] = "pink"
        labelLogin.place(x=840,y=10,width=70,height=25)
        labelLogin.bind("<Button-1>", self.gotoLogin)

        canvas = tk.Canvas(root, width = 300, height = 300, highlightthickness = 0)
        canvas.pack()
        canvas["bg"] = "white"
        img = ImageTk.PhotoImage(file = "./img/logo.jpg")
        canvas.create_image(60, 2, anchor = tk.NW, image = img)
        tk.mainloop()

    def gotoLogin(self, event) :
        self.root.destroy()
        self.root = tk.Tk()
        self.app = Login(self.root)
        self.root.mainloop()

    def gotoRegister(self, event) :
        print("goto register")

class Login:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=951
        height=703
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background = "white")

        menuBar = tk.Frame(master = root, height = 50, width = 951, bg = "pink")
        menuBar.pack()

        labelTitle=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        labelTitle["font"] = ft
        labelTitle["fg"] = "#333333"
        labelTitle["justify"] = "center"
        labelTitle["text"] = "Public Recipe"
        labelTitle["bg"] = "pink"
        labelTitle.config(font="Courier")
        labelTitle.place(x=378,y=10,width=205,height=30)

        entryUsername=tk.Entry(root)
        entryUsername["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entryUsername["font"] = ft
        entryUsername["fg"] = "#333333"
        entryUsername["justify"] = "center"
        entryUsername["text"] = ""
        entryUsername["justify"] = "left"
        entryUsername.place(x=350,y=380,width=259,height=30)

        labelUsername=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        labelUsername["font"] = ft
        labelUsername["fg"] = "#333333"
        labelUsername["justify"] = "left"
        labelUsername["text"] = "Username :"
        labelUsername["bg"] = "white"
        labelUsername.place(x=350,y=350,width=68,height=30)

        labelPassword=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        labelPassword["font"] = ft
        labelPassword["fg"] = "#333333"
        labelPassword["justify"] = "left"
        labelPassword["text"] = "Password :"
        labelPassword["bg"] = "white"
        labelPassword.place(x=350,y=420,width=80,height=30)

        entryPassword=tk.Entry(root)
        entryPassword["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entryPassword["font"] = ft
        entryPassword["fg"] = "#333333"
        entryPassword["justify"] = "center"
        entryPassword["text"] = "tes"
        entryPassword["justify"] = "left"
        entryPassword.place(x=350,y=450,width=260,height=30)

        loginButton=tk.Button(root)
        loginButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        loginButton["font"] = ft
        loginButton["fg"] = "#000000"
        loginButton["justify"] = "center"
        loginButton["text"] = "Login"
        loginButton.place(x=450,y=510,width=70,height=25)
        loginButton["command"] = lambda : self.loginButton_command(entryUsername.get(), entryPassword.get(), comboBox.get())

        canvas = tk.Canvas(root, width = 300, height = 300, highlightthickness = 0)
        canvas.pack()
        canvas["bg"] = "white"
        img = ImageTk.PhotoImage(file = "./img/logo.jpg")
        canvas.create_image(60, 2, anchor = tk.NW, image = img)

        comboBox = ttk.Combobox(root, values = ["Shopper", "Pembeli"])
        comboBox.place(x = 410, y = 610)

        tk.mainloop()

    def loginButton_command(self, username, password, status):
        if status == "Pembeli" :
            registered = login.loginPembeli(username, password)
            if registered :
                print("Berhasil masuk")
            else :
                print("User tidak ditemukan")
        elif status == "Shopper" :
            registered = login.loginShopper(username, password)
            if registered :
                print("Berhasil masuk")
            else :
                print("User tidak ditemukan")

if __name__ == "__main__":
    root = tk.Tk()
    app = homePage(root)
    root.mainloop()





# from tkinter import *

# window = Tk()

# window.wm_attributes('-transparentcolor', 'black')

# homePage = Frame(master = window, height = 550, width = 2000)

# menuBar = Frame(master = homePage, height = 80, width = 2000, bg = "pink")
# labelTitle = Label(text = "Public Recipe", master = menuBar, justify = CENTER, bg = "pink")
# labelTitle.config(font=("Courier", 44))
# labelTitle.pack()
# menuBar.pack(fill = X, side = TOP, expand = False)

# frame = Frame(master = homePage, height = 2000, width = 2000, bg = "yellow")
# frame.pack(fill = BOTH, side = TOP, expand = False)

# homePage.pack(fill = BOTH, side = TOP, expand = True)

# window.mainloop()






# root = Tk()

# root.title("Public Recipe")
# menuBar = Frame(master = root, relief = RAISED, borderwidth = 1, bg = "pink", height = 20)

# menuBar.columnconfigure([0,1,2,3,4,5,6], minsize = 100, weight = 1)
# menuBar.rowconfigure(0, minsize = 20, weight = 1)

# labelTitle = Label(text = "Public Recipe", master = menuBar, justify = CENTER)
# labelTitle.grid(row = 0, column = 3, sticky = "ne")

# labelSignUp = Button(text = "Sign Up", master = menuBar, justify = RIGHT)
# labelSignUp.grid(row = 0, column = 6, sticky = "nw")

# labelLogin = Button(text = "Login", master = menuBar, justify = RIGHT)
# labelLogin.grid(row = 0, column = 6, sticky = "ne")

# menuBar.pack(fill = BOTH, expand = True)
# root.wm_attributes('-transparentcolor', 'black')

# root.mainloop()