import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import datetime as dt
import csv

class riwayat:    
    def __init__(self, usernameInput):
        self.username = usernameInput


    def windowShow(self):  
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

        with open('.\\csv\\Riwayat.csv') as csv_Riwayat:
            riwayatTotal = list(csv.reader(csv_Riwayat, delimiter=';'))
            csv_Riwayat.close()

        print(riwayatTotal)
        root = tk.Tk()
        root.title("Riwayat Pemesanan")

        headerbg = tk.Frame(root,bg="#FFA6A6")
        headerbg.place(relheight=0.15, relwidth=1)

        containerbg = tk.Frame(root, bg="#e75480")
        containerbg.place(relheight=0.85, relwidth=1, rely=0.15)

        canvas = tk.Canvas(root, height=600, width=1100)
        canvas.pack()

        header = tk.Frame(canvas,bg="#FFA6A6")
        header.place(relheight=0.15, relwidth=1)

        title = tk.Label(header, text="Riwayat Pesanan "+now, fg="white", bg="#FFA6A6", font="Garamond 32 bold")
        title.place(rely=0.5,relx=0.5,anchor="center")

        container = tk.Frame(canvas, bg="#e75480")
        container.place(relheight=0.85, relwidth=1, rely=0.15)

        tableContainer = tk.Frame(container, bg="#e75480")
        tableContainer.place(rely=0.05,relx=0.5,anchor="n")

        total_rows = len(riwayatTotal)
        total_columns = len(riwayatTotal[0])

        for i in range(total_rows):
            for j in range(total_columns):
                if (j!=2 and (riwayatTotal[i][2] == self.username or i == 0) and (now == riwayatTotal[i][1] or i == 0)):
                    table = tk.Entry(tableContainer, fg='maroon', bg="#FFA6A6", font=('Arial',9))
                    table.grid(row=i, column=j, pady=0.5,padx=0.5)
                    table.insert(tk.END, riwayatTotal[i][j])

        root.mainloop()

class shopperpage:
    def __init__(self, username):
        self.username = username
        self.currOrder = []

    def buttonPick(self):
        print("Hi")

    def showRiwayat(self):
        print("riwayat")
        riwayatUser = riwayat(self.username)
        riwayatUser.windowShow()

    def ambilPesanan(self,text,buttonAmbilPesanan,buttonClearPesanan):
        with open(".\\csv\\Pesanan.csv", "r") as csv_Pesanan:
            dataPesananBaru = list(csv.reader(csv_Pesanan, delimiter=';'))
            takenOrder = dataPesananBaru[1]
            dataPesananBaru.remove(dataPesananBaru[1])
        with open(".\\csv\\Pesanan.csv", "w",newline='') as csv_Pesanan:
            csv.writer(csv_Pesanan,delimiter=';').writerows(dataPesananBaru)
            csv_Pesanan.close()
        print("taken order")
        print(takenOrder)
        self.currOrder = takenOrder
        self.writeToPage(text,buttonAmbilPesanan,buttonClearPesanan)
        
    def writeToPage(self,text,buttonAmbilPesanan,buttonClearPesanan):
        text.configure(state="normal")
        text.delete(1.0,tk.END)
        text.insert(tk.END, "Nama Pembeli\t\t: "+str(self.currOrder[0])+"\n")
        text.insert(tk.END, "Alamat Pembeli\t\t: "+str(self.currOrder[1])+"\n")
        text.insert(tk.END, "No. Telp Pembeli\t\t: "+str(self.currOrder[2])+"\n")
        text.insert(tk.END, "Nama Toko\t\t: "+str(self.currOrder[3])+"\n")
        text.insert(tk.END, "Alamat Toko\t\t: "+str(self.currOrder[4])+"\n")
        text.insert(tk.END, "Bahan\t\t: "+str(self.currOrder[5])+"\n")
        text.configure(state="disabled")
        buttonAmbilPesanan.configure(state="disabled", fg="white", bg="red")
        buttonClearPesanan.configure(state="normal",fg="black",bg="white")

    def clearPesanan(self,text,buttonAmbilPesanan,buttonClearPesanan):
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
        print(now)

        text.configure(state="normal")
        text.delete(1.0,tk.END)
        text.insert(tk.END, "Tidak ada pesanan aktif.")
        text.configure(state="disabled")
        buttonClearPesanan.configure(state="disabled", fg="white", bg="red")
        buttonAmbilPesanan.configure(state="normal",fg="black",bg="white")
        with open(".\\csv\\Riwayat.csv", "r") as csv_Riwayat:
            dataPesananBaru = list(csv.reader(csv_Riwayat, delimiter=';'))
            dataPesananBaru.append([len(dataPesananBaru),now,self.username,self.currOrder[0],self.currOrder[1],self.currOrder[2],self.currOrder[3],self.currOrder[4],self.currOrder[5]])
        with open(".\\csv\\Riwayat.csv", "w",newline='') as csv_Riwayat:
            csv.writer(csv_Riwayat,delimiter=';').writerows(dataPesananBaru)
            csv_Riwayat.close()
        self.currOrder = []


    def windowShow(self):
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

        root = tk.Tk()
        root.title("Order")

        headerbg = tk.Frame(root,bg="#FFA6A6")
        headerbg.place(relheight=0.15, relwidth=1)

        containerbg = tk.Frame(root, bg="#e75480")
        containerbg.place(relheight=0.85, relwidth=1, rely=0.15)

        canvas = tk.Canvas(root, height=400, width=400)
        canvas.pack()

        header = tk.Frame(canvas,bg="#FFA6A6")
        header.place(relheight=0.15, relwidth=1)

        title = tk.Label(header, text="Public Recipe's Shopper", fg="white", bg="#FFA6A6", font=("Garamond 32 bold",12))
        title.place(rely=0.5,relx=0.5,anchor="center")
        
        container = tk.Frame(canvas, bg="#e75480")
        container.place(relheight=0.85, relwidth=1, rely=0.15)

        labelYourCurrentOrder = tk.Label(container, text="Your current order:", fg="white", bg="#e75480", font=("Garamond 32 bold",12))
        labelYourCurrentOrder.place(rely=0.05, relx=0.05, anchor="nw")

        order = tk.Text(container,state="normal", fg="white", bg="#e75480",font=("Monospace",10))
        order.place(rely=0.15, relx=0.05, width=360, height=150, anchor="nw")
        order.insert(tk.END,"Tidak ada pesanan aktif.")
        order.configure(state="disabled")

        buttonRiwayat = tk.Button(container, text="Riwayat Hari Ini", font=("Garamond 32 bold",12), command=self.showRiwayat)
        buttonRiwayat.place(rely=0.65, relx=0.05, anchor="nw")

        buttonAmbilPesanan = tk.Button(container, text="Ambil Pesanan", font=("Garamond 32 bold",12), command=lambda : self.ambilPesanan(order,buttonAmbilPesanan,buttonClearPesanan))
        buttonAmbilPesanan.place(rely=0.65, relx=0.95, anchor="ne")

        buttonClearPesanan = tk.Button(container, text="Clear Pesanan",state="disabled", fg="white", bg="red", font=("Garamond 32 bold",12), command=lambda : self.clearPesanan(order,buttonAmbilPesanan,buttonClearPesanan))
        buttonClearPesanan.place(rely=0.80, relx=0.95, anchor="ne")

        root.mainloop()

    

# riwayatShopper = riwayat("jeff123")
# riwayatShopper.windowShow()

shopperJeff = shopperpage("jeff123")
shopperJeff.windowShow()