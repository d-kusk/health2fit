import json
from src.business.oauth import getOauth
from src.business.token import getToken
from src.business.health_status import health_status

def oauthHandler(event, context):
    return getOauth()

def tokenHandler(event, context):
    return getToken()

def fitHandler(eventm, context):
    response = health_status()
    return response
