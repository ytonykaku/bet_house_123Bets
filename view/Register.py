import customtkinter
from CTkMessagebox import CTkMessagebox
import Fontes.Fonts as Fonts
import Validation as v

class Register:
    def __init__(self):
        
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")

        self.register = customtkinter.CTk()
        self.register.geometry("800x550")
        self.register.title('Cadastro')
        
        frame = customtkinter.CTkFrame(master = self.register)
        frame.pack(pady = 30, padx = 120, fill = "both", expand = True)

        label = customtkinter.CTkLabel(master = frame, width = 120, height = 32, text = "123Bet - Cadastro", font = ('Roboto', 24))
        label.pack(pady = 12, padx = 10)

        self.nomeEntry = customtkinter.CTkEntry(master = frame, width = 240, height = 32, placeholder_text = "Nome completo")
        self.nomeEntry.pack(pady = 12, padx = 10)

        self.cpfEntry = customtkinter.CTkEntry(master=frame, width = 240, height = 32, placeholder_text = "CPF")
        self.cpfEntry .pack(pady = 12, padx = 10)

        self.usernameEntry = customtkinter.CTkEntry(master=frame, width = 240, height = 32, placeholder_text = "Username")
        self.usernameEntry.pack(pady = 12, padx = 10)

        self.passwordEntry = customtkinter.CTkEntry(master = frame, width = 240, height = 32, placeholder_text = "Password", show="*")
        self.passwordEntry.pack(pady = 12, padx = 10)

        button1 = customtkinter.CTkButton(master=frame, width = 240, height = 32, text = "Cadastrar", command = self.registerPress, font = Fonts.button_med_font())
        button1.pack(pady = 12, padx = 10)

        button2 = customtkinter.CTkButton(master = frame, width = 240, height = 32, text = "Voltar", command = self.voltarPress, font = Fonts.button_med_font())
        button2.pack(pady = 15, padx = 10)

        self.register.mainloop()
        
    def registerPress(self):
        name = self.nomeEntry.get()
        cpf = self.cpfEntry.get()
        username = self.usernameEntry.get()
        senha = self.passwordEntry.get()
        
        try:
            v.validarVazio(self.nomeEntry.get())
        except ValueError as e:
            CTkMessagebox(title = "Error", message = "Nome " + str(e), icon = "cancel")

        try:
            v.validarCpf(self.cpfEntry.get())
        except ValueError as e:
            CTkMessagebox(title = "Error", message = "CPF " + str(e), icon = "cancel")

        try:
            v.validarVazio(self.usernameEntry.get())
        except ValueError as e:
            CTkMessagebox(title = "Error", message = "Username " + str(e), icon = "cancel")
        
        try:
            v.validarVazio(self.passwordEntry.get())
        except ValueError as e:
            CTkMessagebox(title = "Error", message = "Password " + str(e), icon = "cancel")

        print(name, cpf, username, senha)
        #cria usario aqui e de acordo com o retorno escolhe a mensagem
        #CTkMessagebox(message="Usuario criado com sucesso!", icon="check", option_1="OK")
        #CTkMessagebox(title="Error", message="Usuário não criado", icon="cancel")

    def voltarPress(self):
        self.register.destroy()

if __name__ == '__main__':    
    Register()