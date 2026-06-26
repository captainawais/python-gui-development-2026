# ==========================
# IMPORTS
# ==========================

import json
import os


# ==========================
# STORAGE CLASS
# ==========================

class Storage:

    # ==========================
    # INIT
    # ==========================

    def __init__(self):

        self.stats_file = "data/stats.json"

        self.settings_file = "data/settings.json"

        self.achievements_file = "data/achievements.json"

    # ==========================
    # LOAD JSON
    # ==========================

    def load(self, file_path):

        if not os.path.exists(file_path):

            return {}

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    # ==========================
    # SAVE JSON
    # ==========================

    def save(
        self,
        file_path,
        data
    ):

        with open(
            file_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

    # ==========================
    # LOAD STATS
    # ==========================

    def load_stats(self):

        return self.load(
            self.stats_file
        )

    # ==========================
    # SAVE STATS
    # ==========================

    def save_stats(
        self,
        data
    ):

        self.save(
            self.stats_file,
            data
        )

    # ==========================
    # LOAD SETTINGS
    # ==========================

    def load_settings(self):

        return self.load(
            self.settings_file
        )

    # ==========================
    # SAVE SETTINGS
    # ==========================

    def save_settings(
        self,
        data
    ):

        self.save(
            self.settings_file,
            data
        )

    # ==========================
    # LOAD ACHIEVEMENTS
    # ==========================

    def load_achievements(self):

        return self.load(
            self.achievements_file
        )

    # ==========================
    # SAVE ACHIEVEMENTS
    # ==========================

    def save_achievements(
        self,
        data
    ):

        self.save(
            self.achievements_file,
            data
        )