import json

USER_FILE = "data/users.json"


# ==========================
# LOAD USERS
# ==========================

def load_users():

    try:

        with open(
            USER_FILE,
            "r"
        ) as file:

            return json.load(file)

    except:

        return {
            "users": []
        }


# ==========================
# SAVE USERS
# ==========================

def save_users(data):

    with open(
        USER_FILE,
        "w"
    ) as file:

        json.dump(
            data,
            file,
            indent=4
        )


# ==========================
# ADD HISTORY
# ==========================

def add_history(
    user,
    text
):

    if "history" not in user:

        user["history"] = []

    user["history"].append(
        text
    )


# ==========================
# GET HISTORY
# ==========================

def get_history(user):

    return user.get(
        "history",
        []
    )


# ==========================
# LAST TRANSACTION
# ==========================

def get_last_transaction(user):

    history = user.get(
        "history",
        []
    )

    if history:

        return history[-1]

    return "No Transaction"