import typing as t

import customtkinter as ctk

from models.Punter import Punter
from control.PunterController import PunterController


class PunterView(object):

    def __init__(self, master: ctk.CTk, controller: PunterController):
        self.controller = controller

        self.return_frame: ctk.CTkFrame | None = None

        self.main_frame = ctk.CTkFrame(master, corner_radius=0)
        self.main_frame.grid_columnconfigure(0, weight=1)

        self.main_label = ctk.CTkLabel(self.main_frame,
                                       text="[BUG DETECTED]",
                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))

        self.logout_button = ctk.CTkButton(self.main_frame,
                                           text="Logout",
                                           command=self.on_logout_click,
                                           width=200,
                                           fg_color="red",
                                           hover_color="red")
        self.logout_button.grid(row=1, column=0, padx=30, pady=(15, 15))

    def activate_view(self, user: Punter, post_logout_callback: t.Callable[..., None]):
        self.post_logout_callback = post_logout_callback

        self.main_label.configure(text=user.name)

        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=100) # Show main frame

    def on_logout_click(self):
        self.main_frame.grid_forget()
        self.post_logout_callback()

