import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

BOT_API = os.getenv('BOT_API')
OW_API = os.getenv('OW_API')


test_api = f'http://api.openweathermap.org/geo/1.0/direct?q=Тверь&limit=5&appid={OW_API}'
