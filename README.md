# twentyønepilots_new_vid_nøtifier

Notifies your windows computer when twenty øne piløts releases a new video to their youtube channel.

To install needed dependencies:

1. Install all the libraries except for win10toast with pip.
2. Downgrade your pip to version 19.3 (don't ask me why): ```python -m pip install pip==19.3```.
3. Install win10toast: ```pip3 install git+https://github.com/Charnelx/Windows-10-Toast-Notifications.git#egg=win10toast```.
4. Restore pip to most recent version: ```python -m pip install --upgrade pip```.

To run:

1. Navigate to the root directory of your local copy of this repo.
2. Run ```python3 notifier.py```.
