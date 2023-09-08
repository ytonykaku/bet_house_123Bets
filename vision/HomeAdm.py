import customtkinter
from CTkMessagebox import CTkMessagebox
import Fontes.Fonts as Fonts
import Validation as v

class HomeUser:
    def __init__(self, user):

        homepage = customtkinter.CTk()
        customtkinter.set_appearance_mode("dark")  
        customtkinter.set_default_color_theme("green") 

        homepage.geometry("800x800")
        homepage.title('Bem vindo, getName()')
        
        abas = customtkinter.CTkTabview(homepage, height = 750, width = 750)
        abas.pack()
        abas.add("Gerenciar lutas")
        abas.add("Gerenciar usuários")
        abas.add("Gerenciar lutadores")

        self.lutas = customtkinter.CTkLabel(master = abas.tab("Gerenciar lutas"), text = f'EM BREVE...', font=(Fonts.title_font(), 25))
        self.lutadores = customtkinter.CTkLabel(master = abas.tab("Gerenciar lutadores"), text = f'EM BREVE...', font=(Fonts.title_font(), 25))
        self.lutas.place(x = 60, y = 30)
        self.lutadores.place(x = 60, y = 30)
        
        self.cpf = customtkinter.CTkEntry(master = abas.tab("Gerenciar usuários"), height = 30, width = 300, placeholder_text = 'CPF')
        self.cpf.place(x = 220, y = 275)

        button1 = customtkinter.CTkButton(master = abas.tab("Gerenciar usuários"), height = 30, width = 300, text = "Elevar permissão", command = self.elevarPermissao, corner_radius = 6, font = Fonts.button_med_font())
        button1.place(x = 220, y = 320)

        button2 = customtkinter.CTkButton(master = abas.tab("Gerenciar usuários"), height = 30, width = 300, text = "Rebaixar permissão", command = self.rebaixarPermissao, corner_radius = 6, font = Fonts.button_med_font())
        button2.place(x = 220, y = 360)

        homepage.mainloop()
    
    def elevarPermissao(self):
        try:
            v.validarCpf(self.cpf.get())
        except ValueError as e:
            CTkMessagebox(title = "Error", message = e, icon = "cancel")


    def rebaixarPermissao(self):
        try:
            v.validarCpf(self.cpf.get())
        except ValueError as e:
            CTkMessagebox(title = "Error", message = e, icon = "cancel")
            
    
if __name__ == '__main__':    
    HomeUser("matheus")