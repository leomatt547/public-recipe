import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
import re
import mysql.connector
import math
from PIL import ImageTk, Image
import pembeli
import pandas as pd

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

    def buttonContact_command(self, username, password):
        self.root.destroy()
        self.root = tk.Tk()
        self.app = Contact(self.root, username, password)
        self.root.mainloop()
    
    def pindahkepembeli(self, username, password, namaresep):
        self.root.destroy()
        self.root = tk.Tk()
        self.app = pembeli.Resep(self.root, username, password, namaresep)
        self.root.mainloop()

    def cariButton_command(self, query, username, password):
        count,resep = exact(query)
        if (count > 0): #jumlah data
            self.root.destroy()
            self.root = tk.Tk()
            self.app = Search(self.root, query, username, password)
            self.root.mainloop()
        else:
            labelgaada=tk.Label(self.sidebar)
            ft = tkFont.Font(family='Times',size=10)
            labelgaada["font"] = ft
            labelgaada["fg"] = "Red"
            labelgaada["justify"] = "left"
            labelgaada["text"] = "Resep gaada!"
            labelgaada["bg"] = "Pink"
            labelgaada.place(x=4,y=200,width=120,height=20)
    
    def recipeButton_command(self, username, password):
        self.root.destroy()
        self.root = tk.Tk()
        self.app = Resep(self.root, username, password)
        self.root.mainloop()

    def __init__(self, root, username, password):
        self.root = root
        #setting title
        root.title("Resep")
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
        #labelPembeli.bind("<Button-1>", self.gotoLogin)

        main_frame = Frame(root)
        main_frame.pack(fill=BOTH , expand=1)

        my_conn.execute("SELECT * FROM resep limit 0,10")
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
        self.my_canvas = Canvas(main_frame,scrollregion=(0,0,500,math.ceil(jumlah/2)*560))
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
        buttonContact["command"] = lambda : self.buttonContact_command(username, password)
        aboutContact = Button(self.sidebar, text = "About Us", anchor = N, activeforeground = "Black")
        aboutContact.configure(width = 120, height = 2,activebackground = "Pink", relief = FLAT)
        aboutContact_window = self.sidebar.create_window(40, 80, anchor=N, window=aboutContact)
        self.sidebar.bind("<MouseWheel>", self._on_mousewheel)
        
        #Kotak Pencarian
        entryCari=tk.Entry(self.sidebar)
        entryCari["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entryCari["font"] = ft
        entryCari["fg"] = "#333333"
        entryCari["justify"] = "center"
        entryCari["text"] = ""
        entryCari["justify"] = "left"
        entryCari.place(x=4,y=150,width=110,height=20)

        labelCari=tk.Label(self.sidebar)
        ft = tkFont.Font(family='Times',size=10)
        labelCari["font"] = ft
        labelCari["fg"] = "Black"
        labelCari["justify"] = "left"
        labelCari["text"] = "Cari Resep:"
        labelCari["bg"] = "Pink"
        labelCari.place(x=4,y=130,width=110,height=20)

        cariButton=tk.Button(self.sidebar)
        cariButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        cariButton["font"] = ft
        cariButton["fg"] = "#000000"
        cariButton["justify"] = "center"
        cariButton["text"] = "Cari"
        cariButton.place(x=12,y=175,width=90,height=25)
        cariButton["command"] = lambda : self.cariButton_command(entryCari.get(), username, password)

        innercanvas = []
        button = []
        button_window = []
        image = []
        img = []
        
        for i in range(jumlah):
            innercanvas.append(Canvas(self.my_canvas, width = 400, height=560, bg = "pink"))
            self.my_canvas.create_window(120+(i%2)*400, (i//2)*560, anchor=NW, window=innercanvas[i])
            innercanvas[i].create_text(10, 125, anchor=NW, text=resep[i][1], font=("Times New Roman", 12, "bold"))
            innercanvas[i].create_text(10, 145, anchor=NW, text="Bahan", font=("Times New Roman", 9, "bold"))
            innercanvas[i].create_text(10, 160, anchor=NW, text=resep[i][2].replace('\n',''))
            innercanvas[i].create_text(10, 330, anchor=NW, text="Instruksi", font=("Times New Roman", 9, "bold"))
            innercanvas[i].create_text(10, 350, anchor=NW, text=resep[i][3].replace('\n',''))
            if (resep[i][4]):
                image.append(Image.open(str(resep[i][4])))
                image[i] = image[i].resize((200, 120), Image.ANTIALIAS)
                img.append(ImageTk.PhotoImage(image[i]))
                self.img_ref.append(img[i])
                innercanvas[i].create_image(10, 2, anchor = tk.NW, image = self.img_ref[i])
            namaresep = resep[i][1]
            button.append(Button(innercanvas[i], text = "Pesan", anchor = N, command = lambda namaresep=namaresep : self.pindahkepembeli(username, password, namaresep)))
            button[i].configure(width = 8, activebackground = "#33B5E5", relief = FLAT)
            button_window.append(innercanvas[i].create_window(360, 525, anchor=N, window=button[i]))
            innercanvas[i].bind("<MouseWheel>", self._on_mousewheel)

        tk.mainloop()

class Search:
    def _on_mousewheel(self, event):
        self.my_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def pindahkepembeli(self, username, password, namaresep):
        self.root.destroy()
        self.root = tk.Tk()
        self.app = pembeli.Resep(self.root, username, password, namaresep)
        self.root.mainloop()

    def recipeButton_command(self, username, password):
        self.root.destroy()
        self.root = tk.Tk()
        self.app = Resep(self.root, username, password)
        self.root.mainloop()

    def buttonContact_command(self, username, password):
        self.root.destroy()
        self.root = tk.Tk()
        self.app = Contact(self.root, username, password)
        self.root.mainloop()

    def cariButton_command(self, query, username, password):
        count,resep = exact(query)
        if (count > 0): #jumlah data
            self.root.destroy()
            self.root = tk.Tk()
            self.app = Search(self.root, query, username, password)
            self.root.mainloop()
        else:
            labelgaada=tk.Label(self.sidebar)
            ft = tkFont.Font(family='Times',size=10)
            labelgaada["font"] = ft
            labelgaada["fg"] = "Red"
            labelgaada["justify"] = "left"
            labelgaada["text"] = "Resep gaada!"
            labelgaada["bg"] = "Pink"
            labelgaada.place(x=4,y=200,width=120,height=20)
            
    def __init__(self, root, query, username, password):
        self.root = root
        #setting title
        root.title("Search")
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

        jumlah,resep = exact(query)
        self.my_canvas = Canvas(main_frame,scrollregion=(0,0,500,math.ceil(jumlah/2)*560))
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
        buttonContact["command"] = lambda : self.buttonContact_command(username, password)
        buttonContact.configure(width = 120, height = 2,activebackground = "Pink", relief = FLAT)
        buttonContact_window = self.sidebar.create_window(40, 40, anchor=N, window=buttonContact)
        aboutContact = Button(self.sidebar, text = "About Us", anchor = N, activeforeground = "Black")
        aboutContact.configure(width = 120, height = 2,activebackground = "Pink", relief = FLAT)
        aboutContact_window = self.sidebar.create_window(40, 80, anchor=N, window=aboutContact)
        self.sidebar.bind("<MouseWheel>", self._on_mousewheel)
        
        #Kotak Pencarian
        entryCari=tk.Entry(self.sidebar)
        entryCari["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        entryCari["font"] = ft
        entryCari["fg"] = "#333333"
        entryCari["justify"] = "center"
        entryCari["text"] = ""
        entryCari["justify"] = "left"
        entryCari.place(x=4,y=150,width=110,height=20)

        labelCari=tk.Label(self.sidebar)
        ft = tkFont.Font(family='Times',size=10)
        labelCari["font"] = ft
        labelCari["fg"] = "Black"
        labelCari["justify"] = "left"
        labelCari["text"] = "Cari Resep:"
        labelCari["bg"] = "Pink"
        labelCari.place(x=4,y=130,width=110,height=20)

        cariButton=tk.Button(self.sidebar)
        cariButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        cariButton["font"] = ft
        cariButton["fg"] = "#000000"
        cariButton["justify"] = "center"
        cariButton["text"] = "Cari"
        cariButton.place(x=12,y=175,width=90,height=25)
        cariButton["command"] = lambda : self.cariButton_command(entryCari.get(), username, password)

        labelhasil=tk.Label(self.sidebar)
        ft = tkFont.Font(family='Times',size=10)
        labelhasil["font"] = ft
        labelhasil["fg"] = "Green"
        labelhasil["justify"] = "left"
        labelhasil["text"] = "Hasil Pencarian \nuntuk\n" + query
        labelhasil["bg"] = "Pink"
        labelhasil.place(x=4,y=200,width=120,height=80)

        innercanvas = []
        button = []
        button_window = []
        image = []
        img = []
        
        for i in range(jumlah):
            innercanvas.append(Canvas(self.my_canvas, width = 400, height=560, bg = "pink"))
            self.my_canvas.create_window(120+(i%2)*400, (i//2)*560, anchor=NW, window=innercanvas[i])
            innercanvas[i].create_text(10, 125, anchor=NW, text=resep[i][1], font=("Times New Roman", 12, "bold"))
            innercanvas[i].create_text(10, 145, anchor=NW, text="Bahan", font=("Times New Roman", 9, "bold"))
            innercanvas[i].create_text(10, 160, anchor=NW, text=resep[i][2].replace('\n',''))
            innercanvas[i].create_text(10, 330, anchor=NW, text="Instruksi", font=("Times New Roman", 9, "bold"))
            innercanvas[i].create_text(10, 350, anchor=NW, text=resep[i][3].replace('\n',''))
            if (resep[i][4]):
                image.append(Image.open(str(resep[i][4])))
                image[i] = image[i].resize((200, 120), Image.ANTIALIAS)
                img.append(ImageTk.PhotoImage(image[i]))
                self.img_ref.append(img[i])
                innercanvas[i].create_image(10, 2, anchor = tk.NW, image = self.img_ref[i])
            namaresep = resep[i][1]
            button.append(Button(innercanvas[i], text = "Pesan", anchor = N, command = lambda namaresep=namaresep : self.pindahkepembeli(username, password, namaresep)))
            button[i].configure(width = 8, activebackground = "#33B5E5", relief = FLAT)
            button_window.append(innercanvas[i].create_window(360, 525, anchor=N, window=button[i]))
            innercanvas[i].bind("<MouseWheel>", self._on_mousewheel)

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
        self.app = Resep(self.root, username, password)
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

        dframe = pd.read_csv("../data/shopper.csv")
        df1 = dframe[['nama_shopper', 'no_telp_shopper']]
        resep = df1.values.tolist()

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

        jumlah = len(df1) #jumlah data
        self.my_canvas = Canvas(main_frame,scrollregion=(0,0,500,math.ceil(jumlah/2)*201))
        self.my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
        
        my_scrollbar = Scrollbar(main_frame, orient=VERTICAL)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        my_scrollbar.config(command=self.my_canvas.yview)
        self.my_canvas.config(yscrollcommand=my_scrollbar.set)
        self.my_canvas.bind("<MouseWheel>", self._on_mousewheel)

        self.my_canvas.config(width=300,height=600)
        self.my_canvas.config(yscrollcommand=my_scrollbar.set)
        self.my_canvas.pack(side=LEFT,expand=True,fill=BOTH)
        
        labelPembeli=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        labelPembeli["font"] = ft
        labelPembeli["fg"] = "#333333"
        labelPembeli["justify"] = "right"
        labelPembeli["text"] = "Hello, " + str(username)
        labelPembeli["bg"] = "pink"
        labelPembeli.place(x=840,y=10,width=100,height=25)

        #SIDEBAR
        if (jumlah > 6):
            self.sidebar = Canvas(self.my_canvas, width=118, height=(math.ceil(jumlah/2)*200), bg = "pink")
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
        buttonContact["command"] = lambda : self.buttonContact_command(username, password)
        aboutContact = Button(self.sidebar, text = "About Us", anchor = N, activeforeground = "Black")
        aboutContact.configure(width = 120, height = 2,activebackground = "Pink", relief = FLAT)
        aboutContact_window = self.sidebar.create_window(40, 80, anchor=N, window=aboutContact)
        self.sidebar.bind("<MouseWheel>", self._on_mousewheel)

        innercanvas = []
        button = []
        button_window = []

        for i in range(jumlah):
            innercanvas.append(Canvas(self.my_canvas, width = 400, height=100, bg = "pink"))
            self.my_canvas.create_window(120+(i%2)*400, (i//2)*100, anchor=NW, window=innercanvas[i])
            innercanvas[i].create_text(10, 5, anchor=NW, text="Nama Shopper", font=("Times New Roman", 9, "bold"))
            innercanvas[i].create_text(10, 20, anchor=NW, text=resep[i][0], font=("Times New Roman", 12, "bold"))
            innercanvas[i].create_text(10, 60, anchor=NW, text="Nomor Telepon", font=("Times New Roman", 9, "bold"))
            innercanvas[i].create_text(10, 80, anchor=NW, text=resep[i][1].replace('\n',''))
            innercanvas[i].bind("<MouseWheel>", self._on_mousewheel)

        tk.mainloop()