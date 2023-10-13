import typing as t

import customtkinter as ctk
import CTkMessagebox

from view.fonts import Fonts

from models.User import User
from models.Admin import Admin

from control.AdminController import AdminController

class PermissionsTab(ctk.CTkFrame):

    def __init__(self, master, elevate_callback, depress_callback, **kwargs):
        super().__init__(master, **kwargs)

        self.cpf = ctk.CTkEntry(master=self, width=300, height=30, placeholder_text="CPF")
        self.cpf.grid(padx=10)

        elevate_button = ctk.CTkButton(master=self,
                                       text="Elevate",
                                       width=300, height=30,
                                       command=elevate_callback,
                                       corner_radius=6,
                                       font=Fonts.button_med_font())
        elevate_button.grid(pady=5)

        depress_button = ctk.CTkButton(master=self,
                                       text="Depress",
                                       width=300, height=30,
                                       command=depress_callback,
                                       corner_radius=6,
                                       font=Fonts.button_med_font())
        depress_button.grid(pady=5)

class UsersTab(ctk.CTkFrame):

    def __init__(self, master, fetch_callback, **kwargs):
        super().__init__(master, **kwargs)

        self.cpf = ctk.CTkEntry(self, width=300, placeholder_text="CPF")
        self.cpf.grid()

        ctk.CTkButton(master=self,
                      text="Fetch",
                      width=300, height=30,
                      command=fetch_callback,
                      corner_radius=6,
                      font=Fonts.button_med_font()).grid(pady=5)

        self.users = ctk.CTkScrollableFrame(master=self,
                                            width=300, height=30,
                                            corner_radius=6)
        self.users.grid(pady=5)

    def clear(self):
        for s in self.users.grid_slaves():
            s.destroy()

class FightersTab(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        tabs = ctk.CTkTabview(self)

        create_tab = tabs.add("Create")

        create_tab.grid()

        self.name_to_create = ctk.CTkEntry(create_tab, width=300, placeholder_text="NAME")
        self.category = ctk.CTkEntry(create_tab, width=300, placeholder_text="CATEGORY")
        self.height = ctk.CTkEntry(create_tab, width=300, placeholder_text="HEIGHT")
        self.nationality = ctk.CTkEntry(create_tab, width=300, placeholder_text="NATIONALITY")

        self.name_to_create.grid()
        self.category.grid()
        self.height.grid()
        self.nationality.grid()

        create_tab.grid()

        delete_tab = tabs.add("Delete")

        self.name_to_delete = ctk.CTkEntry(delete_tab, width=300, placeholder_text="NAME")

        self.name_to_delete.grid()

        ctk.CTkButton(master=delete_tab,
                      text="Fetch",
                      width=300, height=30,
                      command=lambda : print("Not Implemented Yet."),
                      corner_radius=6,
                      font=Fonts.button_med_font()).grid(pady=5)

        update_tab = tabs.add("Update")

        self.name_to_update = ctk.CTkEntry(update_tab, width=300, placeholder_text="NAME")

        self.name_to_update.grid()

        ctk.CTkButton(master=update_tab,
                      text="Fetch",
                      width=300, height=30,
                      command=lambda : print("Not Implemented Yet."),
                      corner_radius=6,
                      font=Fonts.button_med_font()).grid(pady=5)

        tabs.grid()

class FightsTab(ctk.CTkFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        tabs = ctk.CTkTabview(self)

        create_tab = tabs.add("Create")

        create_tab.grid()

        self.fighterA = ctk.CTkEntry(create_tab, width=300, placeholder_text="Fighter A")
        self.fighterB = ctk.CTkEntry(create_tab, width=300, placeholder_text="Fighter B")

        self.fighterA.grid()
        self.fighterB.grid()

        create_tab.grid()

        delete_tab = tabs.add("Delete")

        # TODO: List fights.

        delete_tab.grid()

        update_tab = tabs.add("Update")

        # TODO: List fights.

        update_tab.grid()

        tabs.grid()

class AdminView(object):

    def __init__(self, master: ctk.CTk, controller: AdminController):
        self.controller = controller

        self.main_frame = ctk.CTkFrame(master, corner_radius=0, height=400, width=400)

        self.main_label = ctk.CTkLabel(self.main_frame,
                                       text="[BUG DETECTED]",
                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))

        tabs = ctk.CTkTabview(self.main_frame)

        self.permissions_tab = PermissionsTab(master=tabs.add("Permissions"),
                                              elevate_callback=self.elevate_user_by_cpf,
                                              depress_callback=self.depress_user_by_cpf)
        self.permissions_tab.grid()

        self.users_tab = UsersTab(master=tabs.add("Users"),
                                  fetch_callback=self.fetch_users)
        self.users_tab.grid()

        self.fighters_tab = FightersTab(master=tabs.add("Fighters"))
        self.fighters_tab.grid()

        self.fights_tab = FightsTab(master=tabs.add("Fights"))
        self.fights_tab.grid()

        tabs.grid(row=1, column=0)

        ctk.CTkButton(self.main_frame,
                      text="Logout",
                      command=self.on_logout_click,
                      fg_color="red",
                      hover_color="red").grid(row=3, column=0, padx=30, pady=(15, 15))

    def activate_view(self, user: Admin, post_logout_callback: t.Callable[..., None]):
        self.current_admin = user
        self.post_logout_callback = post_logout_callback

        self.main_label.configure(text=f"Welcome, [ADMIN] {str(user)}!")

        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=50, pady=50)

    def fetch_users(self):
        self.users_tab.clear()

        cpf = self.users_tab.cpf.get()

        users_fetched: list[User] = list()

        if cpf == "":
            users_fetched.extend(self.controller.fetch_users())
        else:
            users_fetched.append(self.controller.fetch_user_by_cpf(cpf))

        for _, user in enumerate(users_fetched):
            master = ctk.CTkFrame(self.users_tab.users,
                                  width=300, height=10,
                                  bg_color="white")
            ctk.CTkLabel(master,
                         width=300,
                         text=f"Name: {str(user)}").grid(padx=5, pady=5)
            ctk.CTkLabel(master,
                         width=300,
                         text=f"CPF: {user.cpf}").grid(padx=5, pady=5)
            ctk.CTkButton(master,
                          width=300,
                          text="Delete",
                          fg_color="red",
                          command=lambda user=user: self.delete_user(user)).grid(padx=5, pady=5)

            master.grid()

    def delete_user(self, u: User):
        if u.id == self.current_admin.id:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Can not delete connected user.", icon="cancel")
            return

        if u.utype == 0:
            if self.controller.has_money_or_bets(u):
                CTkMessagebox.CTkMessagebox(title="ERROR", message="Can not delete user with money or bets on the system.", icon="cancel")
                return

        self.controller.delete_user(u)
        self.fetch_users()

    def on_logout_click(self):
        self.main_frame.grid_forget()
        self.post_logout_callback()

    def elevate_user_by_cpf(self):
        cpf = self.permissions_tab.cpf.get()

        try:
            self.controller.elevate_by_cpf(cpf)

            CTkMessagebox.CTkMessagebox(title="OK", message="Elevation executed with sucess.", icon="check")
        except:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Elevation failed to execut.", icon="cancel")

    def depress_user_by_cpf(self):
        cpf = self.permissions_tab.cpf.get()

        try:
            self.controller.depress_by_cpf(cpf)

            CTkMessagebox.CTkMessagebox(title="OK", message="Depression executed with sucess.", icon="check")
        except:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Depression failed to execut.", icon="cancel")

