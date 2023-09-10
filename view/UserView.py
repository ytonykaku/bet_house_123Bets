import typing as t

import customtkinter as ctk
import CTkMessagebox

from models.User import User

from control.UserController import UserController


class UserView(object):

    def __init__(self, master: ctk.CTk, controller: UserController):
        self.controller = controller

        self.login_frame = ctk.CTkFrame(master=master, corner_radius=0)
        self.login_frame.grid(row=0, column=0, sticky="ns")

        self.login_label = ctk.CTkLabel(self.login_frame, text="Login", font=ctk.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))

        self.username_entry = ctk.CTkEntry(self.login_frame, width=200, placeholder_text="Username")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))

        self.password_entry = ctk.CTkEntry(self.login_frame, width=200, show="*", placeholder_text="Password")
        self.password_entry.grid(row=2, column=0, padx=30, pady=(0, 15))

        self.login_button = ctk.CTkButton(self.login_frame, text="Login", command=self.on_login_click, width=200)
        self.login_button.grid(row=3, column=0, padx=30, pady=(15, 15))


    def activate_view(self, post_login_callback: t.Callable[[User], None]):
        self.post_login_callback = post_login_callback
        self.login_frame.grid(row=0, column=0, sticky="nsew", padx=100) # Show main frame

    def on_login_click(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        u: User | None = self.controller.authenticate(username, password)

        self.username_entry.delete(0, len(username))
        self.password_entry.delete(0, len(password))

        if u is None:
            CTkMessagebox.CTkMessagebox(title="Error", message="Wrong username or password.", icon="cancel")
            return

        self.login_frame.grid_forget()

        self.post_login_callback(u)

        # match u.utype:
        #     case 0:
        #         p: Punter = self.punter_controller.get_from_user(u)
        #         p.wallet = self.wallet_controller.get_by_id(p.id)
        #         self.punter_view.activate_view(return_frame=self.login_frame, user=p)

        #     case 1:
        #         a: Admin = self.admin_controller.get_from_user(u)
        #         self.admin_view.activate_view(return_frame=self.login_frame, user=a)

