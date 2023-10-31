import typing as t

import customtkinter as ctk
import CTkMessagebox

from models.User import User

from control.Controller import Controller

from view import Validation


class UserView(object):

    def __init__(self, master: ctk.CTk, controller: Controller):
        self.controller = controller

        self.main_frame = ctk.CTkFrame(master=master, corner_radius=0, bg_color="transparent")

        self.login_frame = ctk.CTkFrame(master=self.main_frame, corner_radius=0, bg_color="transparent")

        self.login_label = ctk.CTkLabel(self.login_frame, text="Login", font=ctk.CTkFont(size=20, weight="bold"))

        self.username_entry = ctk.CTkEntry(self.login_frame, width=300, placeholder_text="Username")

        self.password_entry = ctk.CTkEntry(self.login_frame, width=300, show="*", placeholder_text="Password")

        self.login_button = ctk.CTkButton(self.login_frame, text="Login", command=self.on_login_click, width=200)

        self.register_button = ctk.CTkButton(self.login_frame, text="Register", command=self.on_register_click, width=200)

        self.login_frame.grid()
        self.login_label.grid(padx=30, pady=(15, 0))
        self.username_entry.grid(padx=30, pady=(15, 0))
        self.password_entry.grid(padx=30, pady=(15, 0))
        self.login_button.grid(padx=30, pady=(15, 0))
        self.register_button.grid(padx=30, pady=(15, 15))

    def activate_view(self, post_login_callback: t.Callable[[User], None]):
        self.post_login_callback = post_login_callback
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=50, pady=50) # Show main frame

    def on_login_click(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        u: User | None = self.controller.user.authenticate(username, password)

        self.username_entry.delete(0, len(username))
        self.password_entry.delete(0, len(password))

        if u is None:
            CTkMessagebox.CTkMessagebox(title="Error", message="Wrong username or password.", icon="cancel")
            return

        self.main_frame.grid_forget()

        self.post_login_callback(u)

    def on_register_click(self):
        self.login_frame.grid_forget()

        self.register_form_frame = ctk.CTkFrame(master=self.main_frame, corner_radius=0, bg_color="transparent")

        label = ctk.CTkLabel(master=self.register_form_frame,
                             width=300, height=30,
                             text="Register",
                             font=('Roboto', 24))

        self.nameEntry = ctk.CTkEntry(master=self.register_form_frame,
                                      width=300, height=30,
                                      placeholder_text="Name")

        self.cpfEntry = ctk.CTkEntry(master=self.register_form_frame,
                                     width=300, height=30,
                                     placeholder_text="CPF")

        self.emailEntry = ctk.CTkEntry(master=self.register_form_frame,
                                     width=300, height=30,
                                     placeholder_text="Email")

        self.usernameEntry = ctk.CTkEntry(master=self.register_form_frame,
                                          width=300, height=30,
                                          placeholder_text="Username")

        self.passwordEntry = ctk.CTkEntry(master=self.register_form_frame,
                                          width=300, height=30,
                                          placeholder_text="Password",
                                          show="*")

        confirm_register_button = ctk.CTkButton(master=self.register_form_frame,
                                                width=300, height=30,
                                                text="Register",
                                                command=self.on_confim_register_click)

        back_button = ctk.CTkButton(master=self.register_form_frame,
                                    width=300, height=30,
                                    text="Back",
                                    command=self.on_back_click)

        self.register_form_frame.grid(padx=30)
        label.grid(padx=30, pady=(15, 0))
        self.nameEntry.grid(padx=30, pady=(15, 0))
        self.cpfEntry.grid(padx=30, pady=(15, 0))
        self.emailEntry.grid(padx=30, pady=(15, 0))
        self.usernameEntry.grid(padx=30, pady=(15, 0))
        self.passwordEntry.grid(padx=30, pady=(15, 0))
        confirm_register_button.grid(padx=30, pady=(15, 0))
        back_button.grid(padx=30, pady=(15, 15))

    def on_confim_register_click(self):
        try:
            name     = Validation.validarVazio(self.nameEntry.get())
            cpf      = Validation.validarCpf(self.cpfEntry.get())
            email    = Validation.validarVazio(self.emailEntry.get())
            username = Validation.validarVazio(self.usernameEntry.get())
            password = Validation.validarVazio(self.passwordEntry.get())

            u = User(name=name, cpf=cpf, email=email, login=username, password=password)

            self.controller.user.register(u=u)

            CTkMessagebox.CTkMessagebox(title="OK", message="You are now registered!", icon="check")
        except Exception as e:
            print(e)
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Failed to register.", icon="cancel")
            return

        self.register_form_frame.grid_forget()
        self.login_frame.grid()

    def on_back_click(self):
        self.register_form_frame.grid_forget()
        self.login_frame.grid()

