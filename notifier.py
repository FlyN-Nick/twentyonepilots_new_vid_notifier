# Author: Nicholas Assaderaghi

from bs4 import BeautifulSoup as bs
from selenium.webdriver import Chrome
from win10toast import ToastNotifier
import argparse 
import time
import webbrowser

CHROME_DRIVER_PATH = "chromedriver.exe"
SPECIAL_CHANNEL_NAME = "TWENTY ØNE PILØTS"


if __name__ == "__main__":
    print("\nSTARTING UP NOTIFIER...")

    parser = argparse.ArgumentParser(description='Keep\'s you updated about a YouTube channel.')
    parser.add_argument(
        '-c',
        '--channel',
        type=str,
        default="https://www.youtube.com/user/twentyonepilots/videos",
        help='The url of the channel you want notifications from (default https://www.youtube.com/user/twentyonepilots/videos)'
    )
    parser.add_argument(
        '-s',
        '--sleep_duration',
        type=int,
        default=10,
        help='Set the duration between each fetch (default 10)'
    )
    parser.add_argument(
        '-e',
        '--endless',
        action='store_true',
        help='Run script endlessly, instead of quitting when a new video is released.'
    )

    args = parser.parse_args()

    YOUTUBE_CHANNEL_URL = args.channel
    SLEEP_DURATION = args.sleep_duration
    ENDLESS = args.endless

    with Chrome(executable_path=CHROME_DRIVER_PATH) as driver:
        driver.minimize_window()

        MOST_RECENT_VID_TITLE = ""
        while True:
            driver.get(YOUTUBE_CHANNEL_URL)
            time.sleep(2)

            print("\nPARSING...")
            soup = bs(driver.page_source, 'html.parser')

            newest_vid = soup.find("div", {"id": "items", "class": "style-scope ytd-grid-renderer"})
            newest_vid_title = soup.find("a", {"id": "video-title"})
            newest_vid_title_text = newest_vid_title.text

            if MOST_RECENT_VID_TITLE == "":
                MOST_RECENT_VID_TITLE = newest_vid_title_text
                CHANNEL_NAME = soup.find("yt-formatted-string", {"id": "text", "class": "style-scope ytd-channel-name"}).text.upper()
                print("\nDONE PARSING.")
            elif MOST_RECENT_VID_TITLE != newest_vid_title_text:
                print("\nDONE PARSING.")
                newest_vid_link = "https://www.youtube.com" + newest_vid_title['href']
                toast = ToastNotifier()
                if CHANNEL_NAME == "TWENTY ONE PILOTS":
                    CHANNEL_NAME = SPECIAL_CHANNEL_NAME
                toast.show_toast(f"NEW {CHANNEL_NAME} VIDEO!", newest_vid_title_text, duration=10, icon_path="logo.ico", callback_on_click=lambda: webbrowser.open(newest_vid_link, new=0, autoraise=True))
                if not ENDLESS:
                    driver.close()
                    break
                else:
                    MOST_RECENT_VID_TITLE = newest_vid_title_text
            else:
                print("\nDONE PARSING.")
            
            print(f"\nSLEEPING FOR {SLEEP_DURATION} SECONDS.")
            time.sleep(SLEEP_DURATION-2)
            print("\nREFRESHING...")