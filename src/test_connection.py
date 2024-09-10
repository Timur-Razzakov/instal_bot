from datetime import datetime
from urllib.parse import urlencode

import requests

from data.config import settings


print(23423, settings.CLIENT_ID)
print(23423, settings.REDIRECT_URI)
def get_instagram_short_lived_token():
    params = {
        'client_id': settings.CLIENT_ID,
        'redirect_uri': settings.REDIRECT_URI,
        'scope': 'user_profile,user_media',
        'response_type': 'code'
    }
    url = f'https://api.instagram.com/oauth/authorize?{urlencode(params)}'
    return url


get_instagram_short_lived_token()


def refresh_long_lived_token(long_lived_token):
    url = "https://graph.instagram.com/refresh_access_token"
    params = {
        'grant_type': 'ig_refresh_token',
        'access_token': long_lived_token
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['access_token']
    else:
        raise Exception("Error refreshing token: " + response.text)


def check_and_refresh_token(token_data):
    expiration_time = token_data['expires_at']
    current_time = datetime.datetime.now().timestamp()

    if current_time > expiration_time:
        print("Token has expired. Refreshing...")
        new_token = refresh_long_lived_token(token_data['access_token'])
        # Обновите данные токена и сохраните их в хранилище
        token_data['access_token'] = new_token
        token_data['expires_at'] = current_time + 60 * 60 * 24 * 60  # Обновить на 60 дней
        save_token_data(token_data)
    return token_data['access_token']
