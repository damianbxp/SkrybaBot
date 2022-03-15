import os
from dotenv import load_dotenv

load_dotenv(override=True)

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, "data")
QUOTE_TYPES = {
    "normal_audio": {
        "dir": os.path.join(DATA_DIR, "audio_quotes"),
        "file": "audio_quotes.json"
    },
    "insult_audio": {
        "dir": os.path.join(DATA_DIR, "audio_quotes"),
        "file": "audio_insults.json"
    },
    "normal_text": {
        "dir": os.path.join(DATA_DIR, "text_quotes"),
        "file": "text_quotes.json"
    },
    "skryba_text": {
        "dir": os.path.join(DATA_DIR, "text_quotes"),
        "file": "skryba_tale.json"
    },
}

