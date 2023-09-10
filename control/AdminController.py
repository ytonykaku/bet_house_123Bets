from persistence.AdminPersistence import AdminPersistence


class AdminController():

    def __init__(self, persistence: AdminPersistence):
        self.persistence = persistence

