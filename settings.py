import os
from dotenv import load_dotenv

load_dotenv(override=True)

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, "data")
AUDIO_QUOTES = os.path.join(DATA_DIR, "audio_quotes")
TEXT_QUOTES = os.path.join(DATA_DIR, "text_quotes")

