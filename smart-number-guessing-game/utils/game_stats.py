# ==========================
# IMPORTS
# ==========================

from utils.storage import Storage


# ==========================
# GAME STATS CLASS
# ==========================

class GameStats:

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
    # GAMES PLAYED
    # ==========================

    def update_games_played(self):

        self.stats["games_played"] += 1

        self.save()

    # ==========================
    # GAMES WON
    # ==========================

    def update_games_won(self):

        self.stats["games_won"] += 1

        self.save()

    # ==========================
    # GAMES LOST
    # ==========================

    def update_games_lost(self):

        self.stats["games_lost"] += 1

        self.save()

    # ==========================
    # TOTAL SCORE
    # ==========================

    def update_total_score(
        self,
        score
    ):

        self.stats["total_score"] += score

        self.save()

    # ==========================
    # TOTAL GUESSES
    # ==========================

    def update_total_guesses(
        self,
        guesses
    ):

        self.stats["total_guesses"] += guesses

        self.save()

    # ==========================
    # GET STATS
    # ==========================

    def get_stats(self):

        return self.stats
    
    # ==========================
    # UPDATE HIGH SCORE
    # ==========================

    def update_high_score(
        self,
        difficulty,
        score
    ):

        key = f"{difficulty}_high_score"

        if score > self.stats[key]:

            self.stats[key] = score

            self.save()
            
    # ==========================
    # GET HIGH SCORE
    # ==========================

    def get_high_score(
        self,
        difficulty
    ):

        key = f"{difficulty}_high_score"

        return self.stats[key]       
    
    # ==========================
    # UPDATE WIN STREAK
    # ==========================

    def update_win_streak(self):

        self.stats["current_streak"] += 1

        if self.stats["current_streak"] > self.stats["best_streak"]:

            self.stats["best_streak"] = self.stats["current_streak"]

        self.save()


    # ==========================
    # RESET WIN STREAK
    # ==========================

    def reset_win_streak(self):

        self.stats["current_streak"] = 0

        self.save()


    # ==========================
    # GET CURRENT STREAK
    # ==========================

    def get_current_streak(self):

        return self.stats["current_streak"]


    # ==========================
    # GET BEST STREAK
    # ==========================

    def get_best_streak(self):

        return self.stats["best_streak"]
    
    # ==========================
    # LOAD STATS
    # ==========================

    def load_stats(self):

        self.stats = self.storage.load_stats()

        return self.stats