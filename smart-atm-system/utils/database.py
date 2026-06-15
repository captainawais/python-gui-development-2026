import json

USER_FILE = "data/users.json"
HISTORY_FILE = "data/history.json"


def load_users():

    with open(USER_FILE, "r") as file:
        return json.load(file)


def save_users(data):

    with open(USER_FILE, "w") as file:
        json.dump(data, file, indent=4)


def load_history():

    try:
        with open(HISTORY_FILE, "r") as file:
            return json.load(file)

    except:
        return []


def save_history(history):

    with open(HISTORY_FILE, "w") as file:
        json.dump(history, file, indent=4)


def add_history(text):

    history = load_history()

    history.append(text)

    save_history(history)