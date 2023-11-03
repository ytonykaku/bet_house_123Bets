import typing as t

import customtkinter as ctk
import CTkMessagebox

from models.User import User

from control.Controller import Controller

from view import Validation


class UserView(ctk.CTkFrame):

    def __init__(self, master, controller: Controller, post_login_callback, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.controller = controller
        self.post_login_callback = post_login_callback

        self.tabs = ctk.CTkTabview(master=self)

        # ----------------------------- x -----------------------------

        self.login_tab = self.tabs.add("Login")

        self.login_tab.grid_columnconfigure(0, weight=1)

        self.username_entry = ctk.CTkEntry(self.login_tab, placeholder_text="Username")

        self.password_entry = ctk.CTkEntry(self.login_tab, show="*", placeholder_text="Password")

        self.login_button = ctk.CTkButton(self.login_tab, text="Login", command=self.on_login_click)

        # ----------------------------- x -----------------------------

        self.register_tab = self.tabs.add("Register")

        self.register_tab.grid_columnconfigure(0, weight=1)

        self.name_entry = ctk.CTkEntry(master=self.register_tab, placeholder_text="Name")

        self.cpf_entry = ctk.CTkEntry(master=self.register_tab, placeholder_text="CPF")

        self.email_entry = ctk.CTkEntry(master=self.register_tab, placeholder_text="Email")

        self.r_username_entry = ctk.CTkEntry(master=self.register_tab, placeholder_text="Username")

        self.r_password_entry = ctk.CTkEntry(master=self.register_tab, placeholder_text="Password", show="*")

        self.register_button = ctk.CTkButton(master=self.register_tab, text="Register", command=self.on_register_click)

    def grid(self, **kwargs):
        super().grid(**kwargs)
        self.tabs.grid()

        self.username_entry.grid(pady=5)
        self.password_entry.grid(pady=5)
        self.login_button.grid(pady=5)

        self.name_entry.grid(pady=5)
        self.cpf_entry.grid(pady=5)
        self.email_entry.grid(pady=5)
        self.r_username_entry.grid(pady=5)
        self.r_password_entry.grid(pady=5)
        self.register_button.grid(pady=5)

    def on_login_click(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        u: User | None = self.controller.user.authenticate(username, password)

        self.username_entry.delete(0, len(username))
        self.password_entry.delete(0, len(password))

        if u is None:
            CTkMessagebox.CTkMessagebox(title="Error", message="Wrong username or password.", icon="cancel")
            return

        self.grid_forget()

        self.post_login_callback(u)

    def on_register_click(self):
        try:
            name     = Validation.validarVazio(self.name_entry.get())
            cpf      = Validation.validarCpf(self.cpf_entry.get())
            email    = Validation.validarVazio(self.email_entry.get())
            username = Validation.validarVazio(self.username_entry.get())
            password = Validation.validarVazio(self.password_entry.get())

            u = User(name=name, cpf=cpf, email=email, login=username, password=password)

            self.controller.user.register(u=u)

            CTkMessagebox.CTkMessagebox(title="OK", message="You are now registered!", icon="check")
        except:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Failed to register.", icon="cancel")
            return

        self.grid_forget()
