import winsound
import os


def play_sound(filename):

    try:

        path = os.path.join(
            "assets",
            "sounds",
            filename
        )

        winsound.PlaySound(
            path,
            winsound.SND_FILENAME |
            winsound.SND_ASYNC
        )

    except:
        pass


def click():
    play_sound("click.wav")


def login():
    play_sound("login.wav")


def success():
    play_sound("success.wav")


def error():
    play_sound("error.wav")


def deposit():
    play_sound("deposit.wav")
    winsound.Beep(1200, 100)


def withdraw():
    play_sound("withdraw.wav")


def transfer():
    play_sound("transfer.wav")
    winsound.Beep(1200, 100)

def pin_beep():
    play_sound("atm-pin-entry-beep.wav")   