# ==========================
# IMPORTS
# ==========================

import json
import os

# ==========================
# SETTINGS
# ==========================


class Settings:

    FILE = "data/settings.json"

    DEFAULT_SETTINGS = {
        "auto_save": True,
        "notifications": True,
        "dark_mode": False,
        "cloud_sync": False,
    }

    # ==========================
    # LOAD SETTINGS
    # ==========================

    @staticmethod
    def load():

        if not os.path.exists(Settings.FILE):

            Settings.save(Settings.DEFAULT_SETTINGS)

            return Settings.DEFAULT_SETTINGS.copy()

        with open(Settings.FILE, "r", encoding="utf-8") as file:

            return json.load(file)

    # ==========================
    # SAVE SETTINGS
    # ==========================

    @staticmethod
    def save(settings):

        with open(Settings.FILE, "w", encoding="utf-8") as file:

            json.dump(settings, file, indent=4)

    # ==========================
    # UPDATE SETTING
    # ==========================

    @staticmethod
    def update(key, value):

        settings = Settings.load()

        settings[key] = value

        Settings.save(settings)

    # ==========================
    # GET SETTING
    # ==========================

    @staticmethod
    def get(key, default=None):

        settings = Settings.load()

        return settings.get(key, default)

    # ==========================
    # RESET SETTINGS
    # ==========================

    @staticmethod
    def reset():

        Settings.save(Settings.DEFAULT_SETTINGS)
