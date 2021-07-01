# Author: Nicholas Assaderaghi

from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier
import argparse 
import requests
import time
import webbrowser

NOTIFICATION_DURATION = 20

TWENTY_ØNE_PILØTS_YOUTUBE_CHANNEL_URL = "https://www.youtube.com/channel/UCBQZwaNPFfJ1gZ1fLZpAEGw"

if __name__ == "__main__":
    print("\nSTARTING UP NOTIFIER...")
    SLEEP_DURATION = 10
    while True:
        r = requests.get(TWENTY_ØNE_PILØTS_YOUTUBE_CHANNEL_URL)
        if True:
            toast = ToastNotifier()
            toast.show_toast("NEW TWENTY ØNE PILØTS VIDEO!","Notification body", duration=NOTIFICATION_DURATION, icon_path="logo.ico", callback_on_click=lambda: webbrowser.open(TWENTY_ØNE_PILØTS_YOUTUBE_CHANNEL_URL, new=0, autoraise=True))
            break
        else:
            time.sleep(SLEEP_DURATION)