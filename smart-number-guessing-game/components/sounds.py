# ==========================
# IMPORTS
# ==========================

import winsound

# ==========================
# BUTTON CLICK
# ==========================


def play_click():

    try:

        winsound.PlaySound(
            "assets/click.wav", winsound.SND_FILENAME | winsound.SND_ASYNC
        )

    except:

        pass


# ==========================
# WIN SOUND
# ==========================


def play_win():

    try:

        winsound.PlaySound("assets/win.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

    except:

        pass


# ==========================
# LOSE SOUND
# ==========================


def play_lose():

    try:

        winsound.PlaySound(
            "assets/lose.wav", winsound.SND_FILENAME | winsound.SND_ASYNC
        )

    except:

        pass


# ==========================
# NEAR SOUND
# ==========================


def play_near():

    try:

        winsound.PlaySound(
            "assets/near.wav", winsound.SND_FILENAME | winsound.SND_ASYNC
        )

    except:

        pass


# ==========================
# ERROR SOUND
# ==========================


def play_error():

    try:

        winsound.PlaySound(
            "assets/error.wav", winsound.SND_FILENAME | winsound.SND_ASYNC
        )

    except:

        pass

# ==========================
# FAR SOUND     
# ==========================

def play_far():

    try:

        winsound.PlaySound(
            "assets/far.wav", winsound.SND_FILENAME | winsound.SND_ASYNC
        )

    except:

        pass