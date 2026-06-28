# ==========================
# IMPORTS
# ==========================

import json
import os


# ==========================
# STORAGE
# ==========================

class Storage:

    FILE = "data/habits.json"

    @classmethod
    def load(cls):

        if not os.path.exists(cls.FILE):

            return {
                "habits":[]
            }

        with open(

            cls.FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(file)


    @classmethod
    def save(cls,data):

        with open(

            cls.FILE,

            "w",

            encoding="utf-8"

        ) as file:

            json.dump(

                data,

                file,

                indent=4

            )