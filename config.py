from dotenv import load_dotenv
import os

# 从 .env 文件中加载环境变量
load_dotenv()

# tg
TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

# 高德天气 API
GD_URL = os.getenv('GD_URL')
AMAP_WEATHER_KEY = os.getenv('AMAP_WEATHER_KEY')