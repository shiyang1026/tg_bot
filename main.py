import os
import uvicorn
import telebot
from config import TOKEN, WEBHOOK_URL
import  logging
from handlers.weather import send_weather
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from pyngrok import ngrok


logging.basicConfig(level=logging.INFO)
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)


bot = telebot.TeleBot(TOKEN)
app = FastAPI()

@app.get('/', response_class=HTMLResponse)
async def read_root():
    html_content = """
    <html>
        <head>
            <title>tg_bot</title>
        </head>
        <body>
            <h1>Bot is running</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, media_type="text/html")
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

def run_ngrok_local():
    """启动 ngrok 内网穿透，用于本地调试"""
    http_tunnel = ngrok.connect('8080')
    public_url = http_tunnel.public_url
    logger.info(f"Access the root page at: {public_url}")
    # 设置 WEBHOOK_URL 环境变量
    os.environ['WEBHOOK_URL'] = f'{public_url}/webhook'
    bot.remove_webhook()
    # 设置 Webhook
    bot.set_webhook(url=os.environ['WEBHOOK_URL'])
    uvicorn.run(app, host='0.0.0.0', port=8080)

def run_vercel():
    """Vercel 部署"""
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)
    port = int(os.environ.get('PORT', 8080))
    uvicorn.run(app, host='0.0.0.0', port=port)

if __name__ == '__main__':
    if os.getenv('VERCEL') is not None:
        run_vercel()
    else:
        run_ngrok_local()