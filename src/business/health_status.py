import os
import requests
from datetime import datetime, timedelta
from requests.exceptions import HTTPError
from src.helper.log import Log

logger = Log().getInstance()
STATUS_API = 'https://www.healthplanet.jp/status/innerscan.json'

def health_status():
    """
    StatusのAPI から体重のデータを抜き出す
    @url https://www.healthplanet.jp/apis/api.html
    """
    date_format = "%Y%m%d%H%M%S"
    today = datetime.today()
    yestarday = today - timedelta(days=1)

    payload = {
        'access_token': os.environ.get('HEALTH_ACCESS_TOKEN'),
        'tag': '6021', # 体重のみ
        'date': 0, # 登録日付
        'from': yestarday.strftime(date_format),
        'to': today.strftime(date_format)
    }

    try:
        logger.info('[Request start]')
        response = requests.get(STATUS_API, params=payload)
        return response.text
        logger.info('[Request Success]')
    except HTTPError:
        logger.warn('[Request Faild] status:{}'.format(response.status_code, response.reason))

