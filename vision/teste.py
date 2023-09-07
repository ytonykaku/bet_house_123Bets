import customtkinter as CTk
from tkinter import ttk
import tkinter as tk

class Profile:
    def __init__(self, username):
        self.wallet = CTk.CTkToplevel()
        self.wallet.state("zoomed")
        self.wallet.title("CRYPTOCURRENCY PORTFOLIO MANAGEMENT")
        
        #user info
        self.wlabel0 = CTk.CTkLabel(self.wallet,text=f'Olá, getName',font=('Courier',30))
        self.wlabel0.place(x=100,y=60)
        self.userd2 = CTk.CTkLabel(self.wallet,text=f"Saldo: R$getSaldo",font=('Courier',20))
        self.userd2.place(x=140,y=220)
        
        #balance info
        self.wlabel9 = CTk.CTkLabel(self.wallet,text="ACCOUNT HISTORY",font=('Courier',25))
        self.wlabel9.place(x=850,y=50)
        self.table_frame = CTk.CTkFrame(self.wallet,width=200,height=200)
        self.table_frame.place(x=850,y=100)
        self.table = ttk.Treeview(self.table_frame, columns=("col1", "col2","col3"),height=10)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Times',20))
        style.configure("Treeview", font='Courier',rowheight=30)
        self.table.column("#0", width = 0, stretch = "no")
        self.table.heading("#1", text="ACTION")
        self.table.column("#1",width=180)
        self.table.heading("#2", text="AMOUNT")
        self.table.column("#2",width=250)
        self.table.heading("#3", text="TIME")
        self.table.column("#3", width=250)
        self.table_scrollbar = tk.Scrollbar(self.table_frame, orient="vertical", command=self.table.yview)
        self.table_scrollbar.pack(side="right", fill="y")
        self.table.configure(yscrollcommand=self.table_scrollbar.set)
        self.table.pack(expand=True, fill="y")
        
        #for i in range(len(self.userb)):
        #    entry = self.userb[i]
        #    self.table.insert("","end",iid=i,values=entry[1:4])
        

        #balance
        self.Pframe0 = CTk.CTkFrame(self.wallet,width=550,height=380)
        self.Pframe0.place(x=850,y=420)
        self.wlabel3 = CTk.CTkLabel(self.Pframe0,text="FUND YOUR WALLET ",font=('Courier',30))
        self.wlabel3.place(x=20,y=30)
        #self.balance = (self.balance*10000000)//1
        self.wlabel1 = CTk.CTkLabel(self.Pframe0,text="BALANCE AVAILABLE",font=('Courier',27))
        self.wlabel1.place(x=40,y=100)
        self.wlabel2 = CTk.CTkLabel(self.Pframe0,text="R$ getsaldo",font=('Courier',20))
        self.wlabel2.place(x=60,y=160)

        self.amt = tk.StringVar()
        self.wlabel3 = CTk.CTkLabel(self.Pframe0,text="ENTER THE AMOUNT",font=('Courier',20))
        self.wlabel3.place(x=40,y=230)
        self.wentry0 = CTk.CTkEntry(self.Pframe0,textvariable = self.amt)
        self.wentry0.place(x=280,y=230)
        self.addbut = CTk.CTkButton(self.Pframe0,text="DEPOSIT MONEY",font=('Courier',20))
        self.addbut.place(x=40,y=300)
        self.withdrawbut = CTk.CTkButton(self.Pframe0,text="WITHDRAW MONEY",font=('Courier',20))
        self.withdrawbut.place(x=300,y=300)


        self.wallet.mainloop()

if __name__ == '__main__':    
    Profile("matheus")
    