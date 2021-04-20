import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import datetime as dt
import re
import mysql.connector
import math
import login
from PIL import ImageTk, Image
import csv
import pandas

my_connect = mysql.connector.connect(host ="sql6.freesqldatabase.com",
                                    user = "sql6405141",
                                    password = "BkxHy17U62",
                                    db ="sql6405141")
my_conn = my_connect.cursor()

def exact(query):
    my_conn.execute("SELECT * FROM resep WHERE MATCH (nama,bahan,instruksi) AGAINST ('"+query+"' IN BOOLEAN MODE)")
    resep = []
    count = 0
    for query in my_conn:
        temp = []
        for j in range(len(query)):
            temp.append(query[j])
        resep.append(query)
        count=count+1
    return count,resep
    
class Resep:
    def _on_mousewheel(self, event):
        self.my_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def order_pesanan(self, username, password, bahan):
        # Current date
        todaydate = dt.datetime.now()
        date = str(todaydate.day)
        month = str(todaydate.month)
        year = str(todaydate.year)
        now = ""
        if (len(month)==1):
            now = date+"/0"+month+"/"+year
        elif (len(month)==1):
            now = date+"/"+month+"/"+year

        data = login.loginPembeli(username,password).values.tolist()
        #print(data.values.tolist())
        with open("..\\data\\Pesanan.csv", "r") as csv_Pesanan:
            dataPesananBaru = list(csv.reader(csv_Pesanan, delimiter=';'))
            dataPesananBaru.append([data[0][0], data[0][3], data[0][1], "NoName", "NoName", bahan])
        with open("..\\data\\Pesanan.csv", "w",newline='') as csv_Pesanan:
            csv.writer(csv_Pesanan,delimiter=';').writerows(dataPesananBaru)
            csv_Pesanan.close()

    def buttonContact_command(self):
        self.root.destroy()
        self.root = tk.Tk()
        self.app = Contact(self.root)
        self.root.mainloop()
    
    def recipeButton_command(self,username, password):
        self.root.destroy()
        self.root = tk.Tk()
        self.app = resep.Resep(self.root, username, password)
        self.root.mainloop()

    def __init__(self, root, username, password, namaresep):
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

        labelPembeli=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        labelPembeli["font"] = ft
        labelPembeli["fg"] = "#333333"
        labelPembeli["justify"] = "right"
        labelPembeli["text"] = "Hello, " + str(username)
        labelPembeli["bg"] = "pink"
        labelPembeli.place(x=840,y=10,width=100,height=25)
        main_frame = Frame(root)
        main_frame.pack(fill=BOTH , expand=1)

        my_conn.execute("SELECT * FROM resep WHERE MATCH (nama) AGAINST ('"+namaresep+"' IN BOOLEAN MODE)")
        count=0
        resep = []
        for query in my_conn:
            temp = []
            for j in range(len(query)):
                #if (j != 0):
                    #query[j] = query[j].replace('\n','')
                temp.append(query[j])
            resep.append(query)
            count=count+1
        jumlah = count #jumlah data
        self.my_canvas = Canvas(main_frame,scrollregion=(0,0,500,math.ceil(jumlah/2)*350))
        self.my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
        
        my_scrollbar = Scrollbar(main_frame, orient=VERTICAL)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        my_scrollbar.config(command=self.my_canvas.yview)
        self.my_canvas.config(yscrollcommand=my_scrollbar.set)
        self.my_canvas.bind("<MouseWheel>", self._on_mousewheel)

        self.my_canvas.config(width=300,height=600)
        self.my_canvas.config(yscrollcommand=my_scrollbar.set)
        self.my_canvas.pack(side=LEFT,expand=True,fill=BOTH)

        self.img_ref = []
        #SIDEBAR
        if (jumlah > 2):
            self.sidebar = Canvas(self.my_canvas, width=118, height=(math.ceil(jumlah/2)*560), bg = "pink")
        else:
            self.sidebar = Canvas(self.my_canvas, width=118, height=703, bg = "pink")
        self.my_canvas.create_window(0, 0, anchor=NW, window=self.sidebar)
        buttonRecipeList = Button(self.sidebar, text = "Recipe List", anchor = N, activeforeground = "Black")
        buttonRecipeList.configure(width = 120, height = 2,activebackground = "Pink", relief = FLAT)
        buttonRecipeList_window = self.sidebar.create_window(40, 0, anchor=N, window=buttonRecipeList)
        buttonRecipeList["command"] = lambda : self.recipeButton_command(username, password)
        buttonContact = Button(self.sidebar, text = "Contact Us", anchor = N, activeforeground = "Black")
        buttonContact.configure(width = 120, height = 2,activebackground = "Pink", relief = FLAT)
        buttonContact_window = self.sidebar.create_window(40, 40, anchor=N, window=buttonContact)
        buttonContact["command"] = lambda : self.buttonContact_command()
        aboutContact = Button(self.sidebar, text = "About Us", anchor = N, activeforeground = "Black")
        aboutContact.configure(width = 120, height = 2,activebackground = "Pink", relief = FLAT)
        aboutContact_window = self.sidebar.create_window(40, 80, anchor=N, window=aboutContact)
        self.sidebar.bind("<MouseWheel>", self._on_mousewheel)
        
        innercanvas = []
        button = []
        button_window = []
        image = []
        img = []
        
        harga = 20000
        ongkos = 5000

        for i in range(jumlah):
            innercanvas.append(Canvas(self.my_canvas, width = 400, height=220, bg = "pink"))
            self.my_canvas.create_window(120+(i%2)*400, (i//2)*220, anchor=NW, window=innercanvas[i])
            innercanvas[i].create_text(10, 125, anchor=NW, text=resep[i][1], font=("Times New Roman", 12, "bold"))
            innercanvas[i].create_text(10, 145, anchor=NW, text=("Harga : "+ str(harga)), font=("Times New Roman", 12, "bold"))
            #Harga
            innercanvas[i].create_text(10, 160, anchor=NW, text="Harga Total : " + str(harga+ongkos), font=("Times New Roman", 12, "bold"))
            #Harga Total (+ Ongkir)
            if (resep[i][4]):
                image.append(Image.open(str(resep[i][4])))
                image[i] = image[i].resize((200, 120), Image.ANTIALIAS)
                img.append(ImageTk.PhotoImage(image[i]))
                self.img_ref.append(img[i])
                innercanvas[i].create_image(10, 2, anchor = tk.NW, image = self.img_ref[i])
            bahan = resep[i][2]
            button.append(Button(innercanvas[i], text = "Pesan", anchor = N, command = lambda bahan=bahan : self.order_pesanan(username,password,bahan)))
            button[i].configure(width = 8, activebackground = "#33B5E5", relief = FLAT)
            button_window.append(innercanvas[i].create_window(360, 180, anchor=N, window=button[i]))
            innercanvas[i].bind("<MouseWheel>", self._on_mousewheel)
            if (i % 2 == 0):
                harga = harga + 5000
                ongkos = ongkos + 1000
            else:
                harga = harga + 3000
                ongkos = ongkos + 2000

        tk.mainloop()

class Contact:
    def _on_mousewheel(self, event):
        self.my_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def buttonContact_command(self, username, password):
        self.root.destroy()
        self.root = tk.Tk()
        self.app = Contact(self.root, username, password)
        self.root.mainloop()

    def recipeButton_command(self, username, password):
        self.root.destroy()
        self.root = tk.Tk()
        self.app = resep.Resep(self.root, username, password)
        self.root.mainloop()
        
    def __init__(self, root, username, password):
        self.root = root
        #setting title
        root.title("Contact Us")
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

        main_frame = Frame(root)
        main_frame.pack(fill=BOTH , expand=1)

        self.my_canvas = Canvas(main_frame,scrollregion=(0,0,500,700))
        self.my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
        
        my_scrollbar = Scrollbar(main_frame, orient=VERTICAL)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        my_scrollbar.config(command=self.my_canvas.yview)
        self.my_canvas.config(yscrollcommand=my_scrollbar.set)
        self.my_canvas.bind("<MouseWheel>", self._on_mousewheel)

        self.my_canvas.config(width=300,height=600)
        self.my_canvas.config(yscrollcommand=my_scrollbar.set)
        self.my_canvas.pack(side=LEFT,expand=True,fill=BOTH)

        self.img_ref = []
        #SIDEBAR
        self.sidebar = Canvas(self.my_canvas, width=118, height=703, bg = "pink")
        self.my_canvas.create_window(0, 0, anchor=NW, window=self.sidebar)
        buttonRecipeList = Button(self.sidebar, text = "Recipe List", anchor = N, activeforeground = "Black")
        buttonRecipeList.configure(width = 120, height = 2,activebackground = "Pink", relief = FLAT)
        buttonRecipeList_window = self.sidebar.create_window(40, 0, anchor=N, window=buttonRecipeList)
        buttonRecipeList["command"] = lambda : self.recipeButton_command(username, password)
        buttonContact = Button(self.sidebar, text = "Contact Us", anchor = N, activeforeground = "Black")
        buttonContact.configure(width = 120, height = 2,activebackground = "Pink", relief = FLAT)
        buttonContact_window = self.sidebar.create_window(40, 40, anchor=N, window=buttonContact)
        buttonContact["command"] = lambda : self.buttonContact_command(username, password)
        aboutContact = Button(self.sidebar, text = "About Us", anchor = N, activeforeground = "Black")
        aboutContact.configure(width = 120, height = 2,activebackground = "Pink", relief = FLAT)
        aboutContact_window = self.sidebar.create_window(40, 80, anchor=N, window=aboutContact)
        self.sidebar.bind("<MouseWheel>", self._on_mousewheel)
