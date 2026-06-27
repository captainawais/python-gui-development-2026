# ==========================
# IMPORTS
# ==========================

from utils.storage import Storage


# ==========================
# ACHIEVEMENT MANAGER
# ==========================

class AchievementManager:

    # ==========================
    # INIT
    # ==========================

    def __init__(self):

        self.storage = Storage()

        self.stats = self.storage.load_stats()

    # ==========================
    # CHECK ACHIEVEMENTS
    # ==========================

    def check(
        self,
        score,
        attempts,
        difficulty,
        seconds
    ):

        unlocked = []

        # ==========================
        # FIRST WIN
        # ==========================

        if not self.stats.get(
            "first_win",
            False
        ):

            self.stats["first_win"] = True

            unlocked.append(
                "🎉 First Victory"
            )

        # ==========================
        # LUCKY GUESS
        # ==========================

        if attempts <= 3:

            unlocked.append(
                "🎯 Lucky Guess"
            )

        # ==========================
        # SPEED MASTER
        # ==========================

        if seconds <= 30:

            unlocked.append(
                "⚡ Speed Master"
            )

        # ==========================
        # HARD MODE
        # ==========================

        if difficulty == "hard":

            unlocked.append(
                "🧠 Hard Mode Winner"
            )

        self.storage.save_stats(
            self.stats
        )

        return unlocked