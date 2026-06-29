# ==========================
# IMPORTS
# ==========================

from datetime import datetime

# ==========================
# HELPERS
# ==========================


class Helpers:

    # ==========================
    # TODAY DATE
    # ==========================

    @staticmethod
    def today():

        return datetime.now().strftime("%Y-%m-%d")

    # ==========================
    # TODAY DAY NUMBER
    # ==========================

    @staticmethod
    def today_index():

        # Monday = 0
        return datetime.now().weekday()

    # ==========================
    # CURRENT MONTH
    # ==========================

    @staticmethod
    def current_month():

        return datetime.now().strftime("%B")

    # ==========================
    # CURRENT YEAR
    # ==========================

    @staticmethod
    def current_year():

        return datetime.now().year

    # ==========================
    # DAYS IN MONTH
    # ==========================

    @staticmethod
    def days_in_month():

        month = datetime.now().month
        year = datetime.now().year

        if month == 2:

            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:

                return 29

            return 28

        if month in [4, 6, 9, 11]:

            return 30

        return 31

    # ==========================
    # PERCENTAGE
    # ==========================

    @staticmethod
    def percentage(completed, total):

        if total == 0:

            return 0

        return round((completed / total) * 100, 1)

    # ==========================
    # FORMAT PERCENT
    # ==========================

    @staticmethod
    def percent_text(completed, total):

        return f"{Helpers.percentage(completed, total)}%"

    # ==========================
    # SAFE VALUE
    # ==========================

    @staticmethod
    def safe(value, default=0):

        if value is None:

            return default

        return value

    # ==========================
    # IS TODAY COMPLETED
    # ==========================

    @staticmethod
    def is_today_completed(history):

        today = Helpers.today()

        return today in history
