# ==========================
# IMPORTS
# ==========================

from utils.storage import Storage


# ==========================
# XP SYSTEM CLASS
# ==========================

class XPSystem:

    # ==========================
    # INIT
    # ==========================

    def __init__(self):

        self.storage = Storage()

        self.stats = self.storage.load_stats()

    # ==========================
    # SAVE
    # ==========================

    def save(self):

        self.storage.save_stats(
            self.stats
        )

    # ==========================
    # ADD XP
    # ==========================

    def add_xp(
        self,
        xp
    ):

        self.stats["xp"] += xp

        self.update_level()

        self.save()

    # ==========================
    # UPDATE LEVEL
    # ==========================

    def update_level(self):

        xp = self.stats["xp"]

        if xp < 100:

            self.stats["level"] = 1

        elif xp < 250:

            self.stats["level"] = 2

        elif xp < 500:

            self.stats["level"] = 3

        elif xp < 1000:

            self.stats["level"] = 4

        else:

            self.stats["level"] = 5

    # ==========================
    # GET XP
    # ==========================

    def get_xp(self):

        return self.stats["xp"]

    # ==========================
    # GET LEVEL
    # ==========================

    def get_level(self):

        return self.stats["level"]