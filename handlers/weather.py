from config import TOKEN, AMAP_WEATHER_KEY, GD_URL
import requests
import telebot

def get_weather():
    """获取实时天气"""
    params = {
        'key': AMAP_WEATHER_KEY,# 高德天气 API key
        'city': '440300',       # 深圳
        'extensions': 'base',   # base: 返回实况天气 all: 返回预报天气
        'output': 'json',
    }
    resp = requests.get(GD_URL, params=params)
    data = resp.json()
    return handle_resp_json(data)

def handle_resp_json(data):
    """处理高德天气 API 返回的 json 数据"""
    if data['status'] == '1':
        today_weather_info =  data['lives'][0]
        return today_weather_info
    else:
        return data

def send_weather(msg, bot):
    w_info = get_weather()
    if isinstance(w_info, dict):
        resp = (
            f"城市: {w_info['province']}{w_info['city']}\n",
            f"天气: {w_info['weather']}\n",
            f"温度: {w_info['temperature']}°C\n",
            f"风力: {w_info['windpower']}\n",
            f"报道时间: {w_info['reporttime']}\n",
        )
        resp = ''.join(resp)
    else:
        resp = "获取天气信息失败:\n" + w_info
    bot.reply_to(msg, resp)


if __name__ == '__main__':
    print(get_weather())