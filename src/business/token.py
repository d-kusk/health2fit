import os
import requests
from requests.exceptions import HTTPError
from src.helper.log import Log

GET_TOKEN_URL = 'https://www.healthplanet.jp/oauth/token'
REDIRECT_URL = 'https://lkrey2rlb5.execute-api.us-west-2.amazonaws.com/dev/token' # 'https://www.healthplanet.jp/success.html',
logger = Log().getInstance()

def getToken():
    """
    Health Planet API のトークンを取得する
    ブラウザからアクセスの想定
    """
    payload = {
        'client_id': os.environ.get('HEALTH_CLIENT_ID'),
        'client_secret': os.environ.get('HEALTH_CLIENT_SECRET'),
        'redirect_uri': REDIRECT_URL,
        'code': os.environ.get('HEALTH_CODE'),
        'grant_type': 'authorization_code' # APIの付与タイプ
    }

    try:
        response = requests.get(GET_TOKEN_URL, params=payload)
    except HTTPError:
        logger.warn('[Request FAILD] status:{} message: {}'.format(response.status_code, response.reason))

