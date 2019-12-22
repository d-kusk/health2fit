import json
import datetime
# from src.helper.S3 import S3
from src.helper.Log import Log
from src.business.health_status import to_yestarday_health_status, one_month_health_status

logger = Log().getInstance()

def daily_health_status(event, context):
    response = to_yestarday_health_status()

    if len(response.data) == 0:
        return {'message': '体重データがありません'}

    # data = {}
    # data['data'] = response.data
    # now = datetime.datetime.now()
    # file_name = "daily/{%Y-%m-%d-%H-%M-%S}.json".format(now)
    # result = S3().putJson(data, file_name)

    if result:
        logger.info('[Finish]')
    else:
        logger.error('[Faild]')


def monthly_health_status(event, context):
    response = one_month_health_status()
    # ファイルを生成

    # S3にファイルを送る

    # 通知 Slackとか

    return response
