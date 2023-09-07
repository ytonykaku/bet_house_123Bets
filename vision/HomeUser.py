import customtkinter
from tkinter import ttk
import tkinter as tk
import Fontes.Fonts as Fonts
from PIL import Image
from CTkMessagebox import CTkMessagebox


class Home:
    def __init__(self, user):
        imageUser = customtkinter.CTkImage(Image.open("Imagens/user.png"), size = (28,28))
        imageSaldo = customtkinter.CTkImage(Image.open("Imagens/saldo.png"), size = (28,28))
        imageHistorico = customtkinter.CTkImage(Image.open("Imagens/historico.png"), size = (28,28))

        homepage = customtkinter.CTk()
        customtkinter.set_appearance_mode("dark")  
        customtkinter.set_default_color_theme("green") 

        homepage.geometry("800x800")
        homepage.title('Bem vindo, getName()')
        
        abas = customtkinter.CTkTabview(homepage, height = 750, width = 750)
        abas.pack()
        abas.add("Lutas")
        abas.add("Carteira")
        abas.add("Apostas")
        
        self.lutas = customtkinter.CTkLabel(master = abas.tab("Lutas"), text = f'EM BREVE...', font=(Fonts.title_font(), 25))
        self.apostas = customtkinter.CTkLabel(master = abas.tab("Apostas"), text = f'EM BREVE...', font=(Fonts.title_font(), 25))
        self.lutas.place(x = 60, y = 30)
        self.apostas.place(x = 60, y = 30)
        
        self.userName = customtkinter.CTkLabel(master = abas.tab("Carteira"), text = f'Olá, Matheus', font=(Fonts.title_font(), 25))
        self.userName.place(x = 60, y = 30)
        self.userImage = customtkinter.CTkLabel(master = abas.tab("Carteira"), text = "", image = imageUser)
        self.userImage.place(x = 20, y = 30)
        
        self.userSaldo= customtkinter.CTkLabel(master = abas.tab("Carteira"), text = f'Saldo: R$65,60', font = (Fonts.heading_font(), 25))
        self.userSaldo.place(x = 500, y = 30)
        self.saldoImage = customtkinter.CTkLabel(master = abas.tab("Carteira"), text = "", image = imageSaldo)
        self.saldoImage.place(x = 465, y = 30)
        
        self.historico = customtkinter.CTkLabel(master = abas.tab("Carteira"), text = "Histórico de transações:", font = (Fonts.heading_font(), 25))
        self.historico.place(x = 60, y = 90)
        self.saldoImage = customtkinter.CTkLabel(master = abas.tab("Carteira"), text = "", image = imageHistorico)
        self.saldoImage.place(x = 20, y = 90)
        
        self.table_frame = customtkinter.CTkFrame(master = abas.tab("Carteira"), width = 600, height = 600)
        self.table_frame.place(x = 30, y = 140)
        self.table = ttk.Treeview(self.table_frame, columns = ("col1", "col2","col3"), height = 15)
        style = ttk.Style()
        style.configure("Treeview", font = Fonts.body_med_font(), rowheight = 20, background="#2a2d2e", foreground="white", bordercolor="#343638", borderwidth = 0)
        style.map('Treeview', background=[('selected', '#22559b')])

        
        self.table.column("#0", width = 0, stretch = "no")
        self.table.heading("#1", text = "Operação")
        self.table.column("#1",width = 210, anchor="center")
        self.table.heading("#2", text = "Valor")
        self.table.column("#2",width = 210, anchor="center")
        self.table.heading("#3", text = "Data")
        self.table.column("#3", width = 210, anchor="center")

        self.table_scrollbar = tk.Scrollbar(self.table_frame, orient = "vertical", command = self.table.yview)
        self.table_scrollbar.pack(side = "right", fill = "y")
        self.table.configure(yscrollcommand = self.table_scrollbar.set)
        self.table.pack(expand = True, fill = "y")

        itens = [("deposito", "R$50,00", "07/09/2023"),
                  ("saque", "R$10,00", "07/09/2023"),
                  ("deposito", "R$30,00", "07/09/2023"),
                  ("saque", "R$20,00", "07/09/2023"),
                  ("deposito", "R$50,00", "07/09/2023"),
                  ("saque", "R$10,00", "07/09/2023"),
                  ("deposito", "R$15,00", "07/09/2023"),
                  ("saque", "R$20,00", "07/09/2023"),
                  ("deposito", "R$50,00", "07/09/2023"),
                  ("saque", "R$50,00", "07/09/2023"),
                  ("deposito", "R$15,00", "07/09/2023"),
                  ("deposito", "R$50,00", "07/09/2023"),
                  ("saque", "R$10,00", "07/09/2023"),
                  ("deposito", "R$30,00", "07/09/2023"),
                  ("deposito", "R$50,00", "07/09/2023"),
                  ("saque", "R$10,00", "07/09/2023"),
                  ("deposito", "R$30,00", "07/09/2023")
                ]
        
        for i in range(len(itens)):
            entry = itens[i]
            self.table.insert("", "end", iid = i, values=entry[0:3])

        self.value = customtkinter.CTkEntry(master = abas.tab("Carteira"), height = 30, width = 300, placeholder_text = 'R$ Valor')
        self.value.place(x = 220, y = 510)

        buttonLogin = customtkinter.CTkButton(master = abas.tab("Carteira"), height = 30, width = 300, text = "Saque", command = self.saquePress, corner_radius = 6, font = Fonts.button_med_font())
        buttonLogin.place(x = 220, y = 560)

        buttonCadastrato = customtkinter.CTkButton(master = abas.tab("Carteira"), height = 30, width = 300, text = "Depósito", command = self.depositoPress, corner_radius = 6, font = Fonts.button_med_font())
        buttonCadastrato.place(x = 220, y = 600)

        homepage.mainloop()
    
    def depositoPress(self):
        #adicionar saldo na conta
        CTkMessagebox(message = "Depósito feito com sucesso!", icon = "check", option_1 = "OK")
        print(self.value.get())
    
    def saquePress(self):
        #verificar se tem saldo na conta
        #se houver saldo retirar e dar mensagem ok caso contrario dar mensagem de erro
        #CTkMessagebox(title = "Error", message = "Saldo insuficiente!", icon = "cancel")
        CTkMessagebox(message = "Saque feito com sucesso!", icon = "check", option_1 = "OK")
        print(self.value.get())

if __name__ == '__main__':    
    Home("matheus")
    