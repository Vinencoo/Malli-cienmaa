from os import environ
from logging import basicConfig, INFO, StreamHandler, getLogger, WARNING, Logger
from logging.handlers import RotatingFileHandler
from script import StartTxT, HelpTxT, AboutTxT

basicConfig( level=INFO, format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s", datefmt='%d-%b-%y %H:%M:%S', handlers=[ RotatingFileHandler("filtersbot.txt", maxBytes=50000000, backupCount=10), StreamHandler() ] )

getLogger("pyrogram").setLevel(WARNING)

def LOGGER(name: str) -> Logger:
    return getLogger(name)

if bool(environ.get("WEBHOOK", False)):

    try:
        API_ID = int(environ.get("API_ID",29712556 ))
    except Exception as e:
        print(f"API_ID Invalid: \n\nLogs: {e}")

    try:
        API_HASH = environ.get("API_HASH", "ecfb01f9c3b7f307470afb79d8a6d154")
    except Exception as e:
        print(f"API_HASH Invalid: \n\nLogs: {e}")

    try:
        BOT_TOKEN = environ.get("BOT_TOKEN", "6747473491:AAH4V11rTgYrbRDo4LAXbaGZfFJU22V7FxA")
    except Exception as e:
        print(f"BOT_TOKEN Invalid: \n\nLogs: {e}")

    try:
        DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://nisanonisano2:<nisanonisano2>@cluster0.p2faypc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    except Exception as e:
        print(f"DATABASE_URI Invalid: \n\nLogs: {e}")

    try:
        DATABASE_NAME = environ.get("DATABASE_NAME", ">cluster0")
    except Exception as e:
        print(f"DATABASE_NAME Invalid: \n\nLogs: {e}")

    try:
        ADMINS = set(str(x) for x in environ.get("ADMINS", "6426017463").split())
    except Exception as e:
        print(f"ADMINS Invalid: \n\nLogs: {e}")

    # OPTIONAL - To set alternate BOT COMMANDS

    ADD_FILTER_CMD = environ.get("ADD_FILTER_CMD", "add")

    DELETE_FILTER_CMD = environ.get("DELETE_FILTER_CMD", "del")

    DELETE_ALL_CMD = environ.get("DELETE_ALL_CMD", "delall")

    CONNECT_COMMAND = environ.get("CONNECT_CMD", "connect")

    DISCONNECT_COMMAND = environ.get("DISCONNECT_CMD", "disconnect")

    BOT_PICS = (environ.get('BOT_PICS', "https://graph.org/file/9f7beeabeea3eef692602.jpg")).split()

    FORCE_SUB = environ.get("UPDATE_CHANNEL", "-1002135903431")

    SUPPORT_CHAT = environ.get("SUPPORT_CHAT", "cccyyyuuue")
    START_TXT = environ.get("START_TXT", StartTxT)

    HELP_TXT = environ.get("HELP_MESSAGE", HelpTxT)

    ABOUT_TXT = environ.get("ABOUT_MESSAGE", AboutTxT)

    AUTO_DELETE = bool(environ.get("AUTO_DELETE", True))

    AUTO_DELETE_SECOND = int(environ.get("AUTO_DELETE_SECOND", 300))

    PORT = environ.get('PORT', '8080')

else:

    print("WEBHOOK is Disabled 😴")
