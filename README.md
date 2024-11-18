# tg_bot

## 本地调试

### 配置项目环境
```bash
pip -m venv venv

pip install -r requirements.txt
```

### 配置环境变量
新建 `.env` 文件, 写入以下内容：

```.env
# telegram
TOKEN=YOUR_BOT_TOKEN
CHAT_ID=YOUR_CHAT_ID

# 高德开放平台 API
GD_URL=https://restapi.amap.com/v3/weather/weatherInfo?
AMAP_WEATHER_KEY=YOUR_AMAP_WEATHER_KEY
```

高德开放平台 天气API 相关信息：https://lbs.amap.com/api/webservice/guide/api/weatherinfo/


### 本地运行

```bash
python main.py
```