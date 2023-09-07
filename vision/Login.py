import tkinter
import customtkinter
from CTkMessagebox import CTkMessagebox
import Register
import Fontes.Fonts as Fonts
from CTkMessagebox import CTkMessagebox

class Login:
    def __init__(self, login):
        customtkinter.set_appearance_mode("dark") 
        customtkinter.set_default_color_theme("green") 

        login.geometry("600x440")
        login.title('Login')

        frame = customtkinter.CTkFrame(master = login, width = 320, height = 360, corner_radius = 15)
        frame.place(relx = 0.5, rely = 0.5, anchor = tkinter.CENTER)

        titulo = customtkinter.CTkLabel(master = frame, text = "123Bet - Login", font = (Fonts.heading_font(), 20))
        titulo.place(x = 50, y = 45)

        self.username = customtkinter.CTkEntry(master = frame, width = 220, placeholder_text = 'Username')
        self.username.place(x = 50, y = 110)

        self.password = customtkinter.CTkEntry(master = frame, width = 220, placeholder_text = 'Password', show = "*")
        self.password.place(x = 50, y = 165)

        buttonLogin = customtkinter.CTkButton(master = frame, width = 220, text = "Login", command = self.loginPress, corner_radius = 6, font = Fonts.button_med_font())
        buttonLogin.place(x = 50, y = 240)

        buttonCadastrato = customtkinter.CTkButton(master = frame, width = 220, text = "Cadastro", command = self.cadastroPress, corner_radius = 6, font = Fonts.button_med_font())
        buttonCadastrato.place(x = 50, y = 280)        

        login.mainloop()

    def loginPress(self):
        login = self.username.get()
        password = self.password.get()
        print(login, password)

        #verificar login com controle se ok entao pegar user e chamar home caso contrario mensagem de erro
        #CTkMessagebox(title="Error", message="Acesso inválido", icon="cancel")

    def cadastroPress(self):
        Register.visionRegister()
        
if __name__ == '__main__':
    login = customtkinter.CTk()
    Login(login)
    login.mainloop()

