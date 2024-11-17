# tg_bot

## 本地调试

### 配置项目环境
```bash
pip -m venv venv

pip install -r requirements.txt
```

### 安装 ngork 实现内网穿透：

参考：https://dashboard.ngrok.com/get-started/setup/macos

```bash
ngrok http http://localhost:8080
```

### 配置环境变量

新建 `.env` 文件, 写入以下内容：

```.env
# telegram
TOKEN=xxxxx
CHAT_ID=xxxxx
WEBHOOK_URL=xxxxx # ngrok 生成的 https 链接

# 高德开放平台 API
GD_URL=https://restapi.amap.com/v3/weather/weatherInfo?
AMAP_WEATHER_KEY=xxxxx
```

高德开放平台 天气API 相关信息：https://lbs.amap.com/api/webservice/guide/api/weatherinfo/


### 本地运行

```bash
python main.py
```