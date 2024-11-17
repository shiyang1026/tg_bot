import telebot
from config import TOKEN, WEBHOOK_URL
import  logging
from handlers.weather import send_weather
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

logging.basicConfig(level=logging.INFO)
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)


bot = telebot.TeleBot(TOKEN)
app = FastAPI()

@app.post('/webhook')
async def webhook(request: Request):
    """Set webhook"""
    if request.headers.get('content-type') == 'application/json':
        json_str = await request.body()
        update = telebot.types.Update.de_json(json_str.decode('UTF-8'))
        bot.process_new_updates([update])
        return JSONResponse(status_code=200, content={})
    else:
        return JSONResponse(status_code=400, content={"message": "Invalid request"})

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the bot!")

@bot.message_handler(commands=['weather'])
def handle_weather(msg):
    send_weather(msg, bot)

if __name__ == '__main__':
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8080)