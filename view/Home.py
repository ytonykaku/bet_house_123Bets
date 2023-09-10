import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


from vision.Fontes import Fonts


class Main(ctk.CTk):

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("dark") 
        ctk.set_default_color_theme("green") 

        self.title('Login')
        self.geometry("600x440")

        frame = ctk.CTkFrame(master=self, width=320, height=360, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

        titulo = ctk.CTkLabel(master=frame, text="123Bet - Login", font=(Fonts.heading_font(), 20))
        titulo.place(x=50, y=45)

        self.username = ctk.CTkEntry(master=frame, width=220, placeholder_text='Username')
        self.username.place(x=50, y=110)

        self.password = ctk.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
        self.password.place(x=50, y=165)

        buttonLogin = ctk.CTkButton(master=frame, width=220, text="Login", command=self.on_login_click, corner_radius=6, font=Fonts.button_med_font())
        buttonLogin.place(x = 50, y = 240)

        buttonCadastrato = ctk.CTkButton(master=frame, width=220, text="Cadastro", command=self.on_register_click, corner_radius=6, font=Fonts.button_med_font())
        buttonCadastrato.place(x = 50, y = 280)

    def on_login_click(self):
        CTkMessagebox(title="Error", message="Acesso inválido", icon="cancel")

    def on_register_click(self):
        CTkMessagebox(title="Error", message="Acesso inválido", icon="cancel")

