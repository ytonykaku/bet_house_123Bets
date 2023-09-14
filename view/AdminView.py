import typing as t

import customtkinter as ctk
import CTkMessagebox

from view.fonts import Fonts

from models.Admin import Admin
from control.AdminController import AdminController


class AdminView(object):

    def __init__(self, master: ctk.CTk, controller: AdminController):
        self.controller = controller

        self.main_frame = ctk.CTkFrame(master, corner_radius=0, height=400, width=400)

        self.main_label = ctk.CTkLabel(self.main_frame,
                                       text="[BUG DETECTED]",
                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))

        tabs = ctk.CTkTabview(self.main_frame)
        tabs.grid(row=1, column=0)

        self.permissions = tabs.add("Permissions")

        self.cpf_entry = ctk.CTkEntry(master=self.permissions, width=300, height=30, placeholder_text="CPF")
        self.cpf_entry.grid(padx=10)

        elevate_button = ctk.CTkButton(master=self.permissions,
                                text="Elevate",
                                width=300, height=30,
                                command=self.elevate_user_by_cpf,
                                corner_radius=6,
                                font=Fonts.button_med_font())
        elevate_button.grid(pady=5)

        depress_button = ctk.CTkButton(master=self.permissions,
                                text="Depress",
                                width=300, height=30,
                                command=self.depress_user_by_cpf,
                                corner_radius=6,
                                font=Fonts.button_med_font())
        depress_button.grid(pady=5)

        self.users = tabs.add("Users")
        fetch_button = ctk.CTkButton(master=self.users,
                                     text="Fetch",
                                     width=300, height=30,
                                     command=self.fetch_users,
                                     corner_radius=6,
                                     font=Fonts.button_med_font())
        fetch_button.grid(pady=5)

        self.users_list = ctk.CTkScrollableFrame(master=self.users,
                                                 width=300, height=30,
                                                 corner_radius=6)
        self.users_list.grid(pady=5)

        self.logout_button = ctk.CTkButton(self.main_frame,
                                           text="Logout",
                                           command=self.on_logout_click,
                                           fg_color="red",
                                           hover_color="red")
        self.logout_button.grid(row=3, column=0, padx=30, pady=(15, 15))

    def activate_view(self, user: Admin, post_logout_callback: t.Callable[..., None]):
        self.post_logout_callback = post_logout_callback

        self.main_label.configure(text=f"Welcome, [ADMIN] {str(user)}!")

        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=50, pady=50)

    def fetch_users(self):
        for s in self.users_list.grid_slaves():
            s.destroy()

        users_fetched = self.controller.fetch_users();

        for _, user in enumerate(users_fetched):
            master = ctk.CTkFrame(self.users_list,
                                  width=300, height=10,
                                  bg_color="white")
            ctk.CTkLabel(master,
                         width=300,
                         text=f"Name: {str(user)}").grid(padx=5, pady=5)
            ctk.CTkLabel(master,
                         width=300,
                         text=f"CPF: {user.cpf}").grid(padx=5, pady=5)

            master.grid()

    def on_logout_click(self):
        self.main_frame.grid_forget()
        self.post_logout_callback()

    def elevate_user_by_cpf(self):
        cpf = self.cpf_entry.get()

        try:
            self.controller.elevate_by_cpf(cpf)

            CTkMessagebox.CTkMessagebox(title="OK", message="Elevation executed with sucess.", icon="check")
        except:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Elevation failed to execut.", icon="cancel")

    def depress_user_by_cpf(self):
        cpf = self.cpf_entry.get()

        try:
            self.controller.depress_by_cpf(cpf)

            CTkMessagebox.CTkMessagebox(title="OK", message="Depression executed with sucess.", icon="check")
        except:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Depression failed to execut.", icon="cancel")

