import os
import requests
from datetime import datetime, timedelta
import calendar
from requests.exceptions import HTTPError
from src.helper.Log import Log

logger = Log().getInstance()
STATUS_API = 'https://www.healthplanet.jp/status/innerscan.json'

DATE_FORMAT = "%Y%m%d%H%M%S"

def to_yestarday_health_status():
    """
    昨日から今日の測定記録を取得
    """
    today = datetime.today()
    yestarday = today - timedelta(days=1)

    __health_status(start=yestarday.strftime(DATE_FORMAT), end=today.strftime(DATE_FORMAT))

def one_month_health_status():
    """
    1ヶ月分の測定記録を取得
    """
    today = datetime.today()
    this_month = calendar.monthrange(today.year, today.month)
    first_date = this_month[0]
    last_date = this_month[1]

    __health_status(start=first_date.strftime(DATE_FORMAT), end=last_date.strftime(DATE_FORMAT))

def __health_status(start, end):
    """
    StatusのAPI から体重のデータを抜き出す
    @url https://www.healthplanet.jp/apis/api.html
    """

    payload = {
        'access_token': os.environ.get('HEALTH_ACCESS_TOKEN'),
        'tag': '6021', # 体重のみ
        'date': 0, # 登録日付
        'from': start,
        'to': end
    }

    try:
        logger.info('[Request start]')
        response = requests.get(STATUS_API, params=payload)
        logger.info('[Request Success]')
        return response.text
    except HTTPError:
        logger.warn('[Request Faild] status:{}'.format(response.status_code, response.reason))
