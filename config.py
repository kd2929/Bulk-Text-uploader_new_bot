import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6047785902:AAFmHAKkyofYcB6yS67nREtc5CKshZ1zhUE")
    API_ID = int(os.environ.get("API_ID", 24250238))
    API_HASH = os.environ.get("API_HASH", "cb3f118ce5553dc140127647edcf3720")
    AUTH_USERS = os.environ.get("AUTH_USERS", "6175650047")
