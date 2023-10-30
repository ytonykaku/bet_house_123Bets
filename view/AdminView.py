import typing as t

import customtkinter as ctk
import CTkMessagebox


from models.User import User
from models.Admin import Admin
from models.Fighter import Fighter

from control.Controller import Controller

class PermissionsTab(ctk.CTkFrame):

    def __init__(self, master, elevate_callback, depress_callback, **kwargs):
        super().__init__(master, **kwargs)

        self.cpf = ctk.CTkEntry(master=self, width=300, height=30, placeholder_text="CPF")
        self.cpf.grid(padx=10)

        elevate_button = ctk.CTkButton(master=self,
                                       text="Elevate",
                                       width=300, height=30,
                                       command=elevate_callback,
                                       corner_radius=6)
        elevate_button.grid(pady=5)

        depress_button = ctk.CTkButton(master=self,
                                       text="Depress",
                                       width=300, height=30,
                                       command=depress_callback,
                                       corner_radius=6)
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
                      corner_radius=6).grid(pady=5)

        self.users = ctk.CTkScrollableFrame(master=self,
                                            width=300, height=30,
                                            corner_radius=6)
        self.users.grid(pady=5)

    def clear(self):
        for s in self.users.grid_slaves():
            s.destroy()

class FightersTab(ctk.CTkFrame):

    def __init__(self, master, create_callback, fetch_callback, **kwargs):
        super().__init__(master, **kwargs)

        tabs = ctk.CTkTabview(self)

        # -----------------------------------------------------------------------------------------

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

        ctk.CTkButton(master=create_tab,
                      text="Create",
                      width=300, height=30,
                      command=create_callback,
                      corner_radius=6).grid(pady=5)

        # -----------------------------------------------------------------------------------------

        find_tab = tabs.add("Find")

        self.name_to_find = ctk.CTkEntry(find_tab, width=300, placeholder_text="NAME")

        self.name_to_find.grid()

        self.fighters = ctk.CTkScrollableFrame(master=find_tab,
                                            width=300, height=30,
                                            corner_radius=6)
        ctk.CTkButton(master=find_tab,
                      text="Fetch",
                      width=300, height=30,
                      command=fetch_callback,
                      corner_radius=6).grid(pady=5)
    
        self.fighters.grid()

        # -----------------------------------------------------------------------------------------

        tabs.grid()
    
    def clear(self):
        for s in self.fighters.grid_slaves():
            s.destroy()

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

        find_tab = tabs.add("Find")

        # TODO: List fights.

        find_tab.grid()

        tabs.grid()

class AdminView(object):

    def __init__(self, master: ctk.CTk, controller: Controller):
        self.controller = controller

        self.main_frame = ctk.CTkFrame(master, corner_radius=0, height=400, width=400)

        self.main_label = ctk.CTkLabel(self.main_frame,
                                       text="[BUG DETECTED]",
                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))

        tabs = ctk.CTkTabview(self.main_frame)

        self.users_tab = UsersTab(master=tabs.add("Users"),
                                  fetch_callback=self.fetch_users)
        self.users_tab.grid()

        self.fighters_tab = FightersTab(master=tabs.add("Fighters"),
                                        create_callback=self.create_fighter,
                                        fetch_callback=self.fetch_fighters)
        self.fighters_tab.grid()

        self.fights_tab = FightsTab(master=tabs.add("Fights"))
        self.fights_tab.grid()

        tabs.grid(row=1, column=0)

        ctk.CTkButton(self.main_frame,
                      text="Logout",
                      command=self.on_logout_click,
                      fg_color="red",
                      hover_color="red").grid(row=3, column=0, padx=30, pady=(15, 15))

    def create_fighter(self):
        try:
            f = Fighter(name=self.fighters_tab.name_to_create.get(),
                        category=self.fighters_tab.category.get(),
                        height=float(self.fighters_tab.height.get()),
                        nationality=self.fighters_tab.nationality.get(),
                        n_wins=0,
                        n_loss=0)

            self.controller.fighter.create_fighter(f=f)
        except:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Failed to creater fighter.", icon="cancel")
            return

        self.fighters_tab.name_to_create.delete(0, len(self.fighters_tab.name_to_create.get()))
        self.fighters_tab.category.delete(0, len(self.fighters_tab.category.get()))
        self.fighters_tab.height.delete(0, len(self.fighters_tab.height.get()))
        self.fighters_tab.nationality.delete(0, len(self.fighters_tab.nationality.get()))

        CTkMessagebox.CTkMessagebox(title="OK", message="Fighter created with sucess.", icon="check")

    def fetch_fighters(self):
        self.fighters_tab.clear()

        name = self.fighters_tab.name_to_find.get()

        fighters_fetched: list[Fighter] = list()

        if name == "":
            fighters_fetched.extend(self.controller.fighter.fetch_fighters())
        else:
            f = self.controller.fighter.fetch_fighter_by_name(name)
            if f:
                fighters_fetched.append(f)

        for _, fighter in enumerate(fighters_fetched):
            master = ctk.CTkFrame(self.fighters_tab.fighters,
                                  width=300, height=10,
                                  bg_color="white")

            ctk.CTkLabel(master,
                         width=300,
                         text=f"Name: {str(fighter.name)}").grid(padx=5, pady=5)
            ctk.CTkLabel(master,
                         width=300,
                         text=f"Nationality: {str(fighter.height)}").grid(padx=5, pady=5)
            ctk.CTkLabel(master,
                         width=300,
                         text=f"Category: {str(fighter.category)}").grid(padx=5, pady=5)

            ctk.CTkButton(master,
                          width=300,
                          text="Delete",
                          command=lambda fighter=fighter: self.delete_fighter(fighter)).grid(padx=5, pady=5)

            master.grid()

    def delete_fighter(self, f: Fighter):
        # TODO: check if in any fights not finished.
        self.controller.fighter.delete_fighter_by_name(f.name)
        self.fetch_fighters()

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
            users_fetched.extend(self.controller.admin.fetch_users())
        else:
            users_fetched.append(self.controller.admin.fetch_user_by_cpf(cpf))

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
                          command=lambda user=user: self.delete_user(user)).grid(padx=5, pady=5)
            ctk.CTkButton(master,
                          width=300,
                          text="Elevate",
                          command=lambda user=user: self.elevate_user(user)).grid(padx=5, pady=5)
            ctk.CTkButton(master,
                          width=300,
                          text="Depress",
                          command=lambda user=user: self.depress_user(user)).grid(padx=5, pady=5)

            master.grid()

    def delete_user(self, u: User):
        if u.id == self.current_admin.id:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Can not delete connected user.", icon="cancel")
            return

        if u.utype == 0:
            if self.controller.admin.has_money_or_bets(u):
                CTkMessagebox.CTkMessagebox(title="ERROR", message="Can not delete user with money or bets on the system.", icon="cancel")
                return

        self.controller.admin.delete_user(u)
        self.fetch_users()

    def depress_user(self, u: User):
        try:
            self.controller.admin.depress_by_cpf(u.cpf)

            CTkMessagebox.CTkMessagebox(title="OK", message="Depression executed with sucess.", icon="check")
        except:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Depression failed to execut.", icon="cancel")

    def elevate_user(self, u: User):
        try:
            self.controller.admin.elevate_by_cpf(u.cpf)

            CTkMessagebox.CTkMessagebox(title="OK", message="Elevation executed with sucess.", icon="check")
        except:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Elevation failed to execut.", icon="cancel")


    def on_logout_click(self):
        self.main_frame.grid_forget()
        self.post_logout_callback()

