# ==========================
# IMPORTS
# ==========================

import json
import os

# ==========================
# STORAGE CLASS
# ==========================


class Storage:

    FILE = "data/habits.json"

    # ==========================
    # LOAD DATA
    # ==========================

    @staticmethod
    def load():

        if not os.path.exists(Storage.FILE):

            return {
                "habits": [],
                "current_streak": 0,
                "best_streak": 0,
                "last_completed_date": "",
            }

        with open(Storage.FILE, "r", encoding="utf-8") as file:

            return json.load(file)

    # ==========================
    # SAVE DATA
    # ==========================

    @staticmethod
    def save(data):

        with open(Storage.FILE, "w", encoding="utf-8") as file:

            json.dump(data, file, indent=4, ensure_ascii=False)

    # ==========================
    # RESET DATA
    # ==========================

    @staticmethod
    def reset():

        Storage.save(
            {
                "habits": [],
                "current_streak": 0,
                "best_streak": 0,
                "last_completed_date": "",
            }
        )
