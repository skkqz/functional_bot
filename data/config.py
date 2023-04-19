import os
from dotenv import load_dotenv

load_dotenv()

BOT_API = os.getenv('BOT_API')
OW_API = os.getenv('OW_API')
ERD_API = os.getenv('ERD_API')
CURATE_API = os.getenv('CURATE_API')
