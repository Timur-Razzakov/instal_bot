import requests
from data.config import settings


def send_message(recipient_id, message_text, quick_replies=None):
    params = {
        "recipient": {"id": recipient_id},
        "message": {
            "text": message_text
        }
    }

    if quick_replies:
        params['message']['quick_replies'] = quick_replies

    headers = {
        "Content-Type": "application/json"
    }
    url = f"{settings.INSTAGRAM_API_URL}?access_token={settings.ACCESS_TOKEN}"
    response = requests.post(url, json=params, headers=headers)
    return response.json()


def create_quick_replies(options):
    return [{"content_type": "text", "title": option, "payload": option} for option in options]
