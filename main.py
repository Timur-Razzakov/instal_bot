import logging
from urllib.parse import urlencode

import requests
from flask import Flask, request

from data.config import settings
from src.handlers import handle_message

app = Flask(__name__)


@app.route('/')
def home():
    # Генерация ссылки для авторизации
    params = {
        'client_id': settings.CLIENT_ID,
        'redirect_uri': settings.REDIRECT_URI,
        'scope': 'user_profile,user_media',
        'response_type': 'code'
    }
    auth_url = f'https://api.instagram.com/oauth/authorize?{urlencode(params)}'
    return f'Перейдите по ссылке для авторизации: <a href="{auth_url}">Authorize</a>'

@app.route('/callback')
def instagram_callback():
    code = request.args.get('code')
    if code:
        # Используем код для получения краткосрочного токена
        params = {
            'client_id': settings.CLIENT_ID,
            'client_secret': settings.CLIENT_SECRET,
            'grant_type': 'authorization_code',
            'redirect_uri': settings.REDIRECT_URI,
            'code': code
        }
        response = requests.get(settings.ACCESS_TOKEN_URL, params=params)
        token_info = response.json()
        print(324234, token_info)
        return token_info
    else:
        return "Authorization failed", 400



@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data['object'] == 'instagram':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:
                if messaging_event.get('message'):
                    sender_id = messaging_event['sender']['id']
                    message_text = messaging_event['message']['text']
                    if message_text:
                        logging.info(f"Получено сообщение от {sender_id}: {message_text}")
                        handle_message(sender_id, message_text)
                    else:
                        logging.warning(f"Сообщение от {sender_id} не содержит текста")
    return "ok", 200


@app.route('/webhook', methods=['GET'])
def verify_token():
    token_sent = request.args.get("hub.verify_token")
    if token_sent == settings.VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Invalid verification token", 403


if __name__ == "__main__":
    app.run(port=5000, debug=True)
