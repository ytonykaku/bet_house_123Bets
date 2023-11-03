import typing as t

import customtkinter as ctk
import CTkMessagebox

from models.User import User
from models.Admin import Admin
from models.Fighter import Fighter
from models.Fight import Fight

from control.Controller import Controller

from view import Frames


class FightersTab(ctk.CTkFrame):

    def __init__(self, master, create_callback, fetch_callback, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.tabs = ctk.CTkTabview(self, width=500)

        # -----------------------------------------------------------------------------------------

        self.create_tab = self.tabs.add("Create")

        self.create_tab.grid_columnconfigure(0, weight=1)

        self.name_to_create = ctk.CTkEntry(self.create_tab, placeholder_text="Name")
        self.category = ctk.CTkEntry(self.create_tab, placeholder_text="Category")
        self.height = ctk.CTkEntry(self.create_tab, placeholder_text="Height")
        self.nationality = ctk.CTkEntry(self.create_tab, placeholder_text="Nationality")

        self.create_button = ctk.CTkButton(master=self.create_tab, text="Create", command=create_callback)

        # -----------------------------------------------------------------------------------------

        self.find_tab = self.tabs.add("Find")

        self.find_tab.grid_columnconfigure(0, weight=1)

        self.fighters = Frames.SearchFrame(master=self.find_tab,
                                           keyword="Name",
                                           fetch_callback=fetch_callback)

    def clear(self):
        self.fighters.clear()

        self.name_to_create.delete(0, len(self.name_to_create.get()))
        self.category.delete(0, len(self.category.get()))
        self.height.delete(0, len(self.height.get()))
        self.nationality.delete(0, len(self.nationality.get()))
    
    def grid(self, **kwargs):
        super().grid(**kwargs)
        self.tabs.grid()

        # self.create_tab.grid()

        self.name_to_create.grid(pady=5)
        self.category.grid(pady=5)
        self.height.grid(pady=5)
        self.nationality.grid(pady=5)

        self.create_button.grid(pady=5)

        # self.find_tab.grid()
        self.fighters.grid()

class FightsTab(ctk.CTkFrame):

    def __init__(self, master, create_callback, fetch_callback, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.tabs = ctk.CTkTabview(self)

        # -----------------------------------------------------------------------------------------

        self.create_tab = self.tabs.add("Create")

        self.create_tab.grid_columnconfigure(0, weight=1)

        self.fight_name = ctk.CTkEntry(self.create_tab, placeholder_text="Fight Name")
        self.fighterA = ctk.CTkEntry(self.create_tab, placeholder_text="Fighter A")
        self.oddFighterA = ctk.CTkEntry(self.create_tab, placeholder_text="Odd Fighter A")
        self.fighterB = ctk.CTkEntry(self.create_tab, placeholder_text="Fighter B")
        self.oddFighterB = ctk.CTkEntry(self.create_tab, placeholder_text="Odd Fighter B")

        self.create_button = ctk.CTkButton(master=self.create_tab, text="Create", command=create_callback)

        # -----------------------------------------------------------------------------------------
        self.find_tab = self.tabs.add("Find")

        self.find_tab.grid_columnconfigure(0, weight=1)

        self.fights = Frames.SearchFrame(master=self.find_tab,
                                         keyword="Name",
                                         fetch_callback=fetch_callback)

    def clear(self):
        self.fights.clear()

        self.fight_name.delete(0, len(self.fight_name.get()))
        self.fighterA.delete(0, len(self.fighterA.get()))
        self.oddFighterA.delete(0, len(self.oddFighterA.get()))
        self.fighterB.delete(0, len(self.fighterB.get()))
        self.oddFighterB.delete(0, len(self.oddFighterB.get()))

    def grid(self, **kwargs):
        super().grid(**kwargs)
        self.tabs.grid()

        # self.create_tab().grid()

        self.fight_name.grid(pady=5)

        self.fighterA.grid(pady=5)
        self.oddFighterA.grid(pady=5)

        self.fighterB.grid(pady=5)
        self.oddFighterB.grid(pady=5)

        self.create_button.grid(pady=5)

        # self.find_tab.grid()

        self.fights.grid()

class AdminView(ctk.CTkFrame):

    def __init__(self,
                 master,
                 controller: Controller,
                 admin: Admin,
                 post_logout_callback: t.Callable[..., None],
                 **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.controller = controller
        self.admin = admin
        self.post_logout_callback = post_logout_callback

        # -------------------------- x --------------------------

        self.admin_frame = Frames.AdminFrame(master=self,
                                             admin=self.admin)

        # -------------------------- x --------------------------

        self.tabs = ctk.CTkTabview(self)

        # -------------------------- x --------------------------

        self.t1 = self.tabs.add("Users")

        self.t1.grid_columnconfigure(0, weight=1)

        self.users_tab = Frames.SearchFrame(master= self.t1,
                                            keyword="CPF",
                                            fetch_callback=self.fetch_users)

        # -------------------------- x --------------------------

        self.t2 = self.tabs.add("Fighters")

        self.t2.grid_columnconfigure(0, weight=1)

        self.fighters_tab = FightersTab(master=self.t2,
                                        create_callback=self.create_fighter,
                                        fetch_callback=self.fetch_fighters)

        # -------------------------- x --------------------------

        self.t3 = self.tabs.add("Fights")

        self.t3.grid_columnconfigure(0, weight=1)

        self.fights_tab = FightsTab(master=self.t3,
                                    create_callback=self.create_fight,
                                    fetch_callback=self.fetch_fights)

        # -------------------------- x --------------------------

        self.logout_button = ctk.CTkButton(self, text="Logout", fg_color="red", command=self.on_logout_click)


    def grid(self, **kwargs):
        super().grid(**kwargs)
        self.admin_frame.grid()

        self.tabs.grid()

        #self.t1.grid()
        self.users_tab.grid()

        #self.t2.grid()
        self.fighters_tab.grid()

        #self.t3.grid()
        self.fights_tab.grid()

        self.logout_button.grid(pady=5)

    def fetch_users(self):
        cpf = self.users_tab.get_input()

        self.users_tab.clear()

        users_fetched: list[User] = list()

        if cpf == "":
            users_fetched.extend(self.controller.admin.fetch())
        else:
            u = self.controller.admin.fetch_user_by_cpf(cpf)
            if u:
                users_fetched.append(u)

        for user in users_fetched:
            master = ctk.CTkFrame(self.users_tab.container,)

            Frames.UserFrame(master, user).grid()

            if user.utype == 0:
                elevate_button = ctk.CTkButton(master=master, text="Elevate", command=lambda u=user: self.elevate_user(u=u))
                elevate_button.grid(pady=5)

            if user.utype == 1:
                depress_button = ctk.CTkButton(master=master, text="Depress", command=lambda u=user: self.depress_user(u=u))
                depress_button.grid(pady=5)

            delete_button = ctk.CTkButton(master=master, text="Delete", command=lambda u=user: self.delete_user(u=u))

            delete_button.grid(pady=5)
            master.grid()

    def delete_user(self, u: User):
        if u.cpf == self.admin.cpf:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Can not delete connected user.", icon="cancel")
            return

        try:
            self.controller.admin.delete(u)
            CTkMessagebox.CTkMessagebox(title="OK", message="Deletion executed with sucess.", icon="check")
        except:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Can not delete user with money or bets.", icon="cancel")

        self.fetch_users()

    def depress_user(self, u: User):
        if u.cpf == self.admin.cpf:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Can not delete connected user.", icon="cancel")
            return

        try:
            self.controller.admin.depress(u)

            CTkMessagebox.CTkMessagebox(title="OK", message="Depression executed with sucess.", icon="check")
        except Exception as e:
            print(e)
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Depression failed to execut.", icon="cancel")

        self.fetch_users()

    def elevate_user(self, u: User):
        try:
            self.controller.admin.elevate(u)

            CTkMessagebox.CTkMessagebox(title="OK", message="Elevation executed with sucess.", icon="check")
        except Exception as e:
            print(e)
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Elevation failed to execut.", icon="cancel")

        self.fetch_users()

    def create_fighter(self):
        try:
            f = Fighter(name=self.fighters_tab.name_to_create.get(),
                        category=self.fighters_tab.category.get(),
                        height=float(self.fighters_tab.height.get()),
                        nationality=self.fighters_tab.nationality.get(),
                        n_wins=0,
                        n_loss=0)

            self.controller.fighter.create(f=f)
        except:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Failed to creater fighter.", icon="cancel")
            return

        self.fighters_tab.clear()

        CTkMessagebox.CTkMessagebox(title="OK", message="Fighter created with sucess.", icon="check")

    def create_fight(self):
        try:
            fA = self.controller.fighter.fetch_by_name(self.fights_tab.fighterA.get())

            if not fA:
                CTkMessagebox.CTkMessagebox(title="ERROR", message="Fighter A not found.", icon="cancel")
                return

            fB = self.controller.fighter.fetch_by_name(self.fights_tab.fighterB.get())

            if not fB:
                CTkMessagebox.CTkMessagebox(title="ERROR", message="Fighter B not found.", icon="cancel")
                return

            if fA == fB:
                CTkMessagebox.CTkMessagebox(title="ERROR", message="Please, provide different fighters.", icon="cancel")
                return

            oddA = self.fights_tab.oddFighterA.get()
            oddB = self.fights_tab.oddFighterB.get()

            fight_name = self.fights_tab.fight_name.get()

            if not fight_name:
                CTkMessagebox.CTkMessagebox(title="ERROR", message="PLease, provide a fight name.", icon="cancel")
                return

            self.controller.fight.create(Fight(fight_name, fA, oddA, fB, oddB))

            CTkMessagebox.CTkMessagebox(title="OK", message="Fight created with success.", icon="check")
        except:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Could not create this fight.", icon="cancel")
        finally:
            self.fights_tab.clear()

    def fetch_fighters(self):
        name = self.fighters_tab.fighters.get_input()

        self.fighters_tab.clear()

        fighters_fetched: list[Fighter] = list()

        if name == "":
            fighters_fetched.extend(self.controller.fighter.fetch())
        else:
            f = self.controller.fighter.fetch_by_name(name)
            if f:
                fighters_fetched.append(f)

        for _, fighter in enumerate(fighters_fetched):
            master = ctk.CTkFrame(self.fighters_tab.fighters.container)
            
            Frames.FighterFrame(master=master, fighter=fighter).grid()

            ctk.CTkButton(master,
                          text="Delete",
                          command=lambda fighter=fighter: self.delete_fighter(fighter)).grid(padx=5, pady=5)

            master.grid()

    def delete_fighter(self, f: Fighter):
        try:
            self.controller.fighter.delete(f.name)
            CTkMessagebox.CTkMessagebox(title="OK", message="Fighter deleted with success.", icon="check")
        except:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Could not delete this fighter.", icon="cancel")

        self.fetch_fighters()

    def fetch_fights(self):
        self.fights_tab.clear()

        fights = list(filter(lambda f: f.winner == None, self.controller.fight.read()))

        for _, fight in enumerate(fights):
            master = ctk.CTkFrame(self.fights_tab.fights.container)

            fight_frame = Frames.FightFrame(master=master, fight=fight)

            form = ctk.CTkFrame(master=master, fg_color="transparent")

            declareA_winner = ctk.CTkButton(form,
                                            text=f"Declare {fight.fA.name} Winner",
                                            command=lambda fight=fight, fighter=fight.fA: \
                                                           self.declare_winner(fight, fighter))

            declareB_winner = ctk.CTkButton(form,
                                            text=f"Declare {fight.fB.name} Winner",
                                            command=lambda fight=fight, fighter=fight.fB: \
                                                           self.declare_winner(fight, fighter))

            delete_button = ctk.CTkButton(master,
                                          text="Delete",
                                          command=lambda fight=fight: self.delete_fight(fight),
                                          width=200)

            master.grid()
            fight_frame.grid()
            form.grid()
            declareA_winner.grid(row=0, column=0, pady=5, padx=5)
            declareB_winner.grid(row=0, column=1, pady=5, padx=5)
            delete_button.grid(pady=5)

    def delete_fight(self, fight: Fight):
        try:
            self.controller.fight.delete(fight)
            CTkMessagebox.CTkMessagebox(title="OK", message="Fight deleted with sucess.", icon="check")
        except:
            CTkMessagebox.CTkMessagebox(title="ERROR", message="Could not delete this fight.", icon="cancel")

        self.fetch_fights()

    def declare_winner(self, fight: Fight, fighter: Fighter):
        self.controller.fight.declare_winner(fight, fighter)
        CTkMessagebox.CTkMessagebox(title="OK", message="Fight finished with success.", icon="check")
        self.fetch_fights()

    def on_logout_click(self):
        self.grid_forget()
        self.post_logout_callback()
