import os
import requests
from requests.exceptions import HTTPError
from src.helper.log import Log

logger = Log().getInstance()
GET_OAUTH_URL = 'https://www.healthplanet.jp/oauth/auth'
REDIRECT_URL = 'https://www.healthplanet.jp/success.html'

def getOauth():
    """
    OAuthコードの取得
    ブラウザからアクセスの想定
    """
    payload = {
        'client_id': os.environ.get('HEALTH_CLIENT_ID'),
        'redirect_uri': REDIRECT_URL,
        'scope': 'innerscan',
        'response_type': 'code'
    }
    try:
        logger.info('[Request oauth] start')
        response = requests.get(GET_OAUTH_URL, params=payload)
        logger.info('[Request oauth] end {}'.format(response.content))
        return response.text
    except HTTPError:
        logger.warn('Request FAILD on health oauth status:{} {}'.format(response.status_code, response.reason))
