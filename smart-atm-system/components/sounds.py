import winsound
import os


# ==========================
# SOUND PATH
# ==========================

BASE_PATH = os.path.join(
    "assets",
    "sounds"
)


# ==========================
# PLAY SOUND
# ==========================

def play_sound(filename):

    try:

        sound_path = os.path.join(
            BASE_PATH,
            filename
        )

        winsound.PlaySound(
            sound_path,
            winsound.SND_FILENAME
            | winsound.SND_ASYNC
        )

    except Exception:
        pass


# ==========================
# STOP SOUND
# ==========================

def stop_sound():

    try:

        winsound.PlaySound(
            None,
            winsound.SND_PURGE
        )

    except Exception:
        pass


# ==========================
# BUTTON CLICK
# ==========================

def click():

    play_sound(
        "click.wav"
    )


# ==========================
# LOGIN SOUND
# ==========================

def login():

    play_sound(
        "login.wav"
    )


# ==========================
# SUCCESS SOUND
# ==========================

def success():

    play_sound(
        "success.wav"
    )


# ==========================
# ERROR SOUND
# ==========================

def error():

    play_sound(
        "error.wav"
    )


# ==========================
# DEPOSIT SOUND
# ==========================

def deposit():

    play_sound(
        "deposit.wav"
    )


# ==========================
# WITHDRAW SOUND
# ==========================

def withdraw():

    play_sound(
        "withdraw.wav"
    )


# ==========================
# TRANSFER SOUND
# ==========================

def transfer():

    play_sound(
        "transfer.wav"
    )


# ==========================
# ATM PIN BEEP
# ==========================

def pin_beep():

    try:

        winsound.Beep(
            1200,
            40
        )

    except Exception:
        pass


# ==========================
# ATM PROCESSING SOUND
# ==========================

def loading():

    try:

        winsound.Beep(
            900,
            100
        )

    except Exception:
        pass


# ==========================
# CARD INSERT SOUND
# ==========================

def card_insert():

    try:

        winsound.Beep(
            700,
            150
        )

    except Exception:
        pass


# ==========================
# CARD EJECT SOUND
# ==========================

def card_eject():

    try:

        winsound.Beep(
            500,
            200
        )

    except Exception:
        pass
    
# ==========================
# STOP CURRENT SOUND
# ==========================

def stop():

    try:

        winsound.PlaySound(
            None,
            winsound.SND_PURGE
        )

    except Exception:
        pass  