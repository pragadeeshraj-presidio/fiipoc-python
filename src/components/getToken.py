import src.constants.constants as constants
import requests as req
import src.constants.urls as urls
from requests.auth import HTTPBasicAuth


def getAccessToken():

    clientId = constants.CLIENT_ID
    secretKey = constants.SECRET_KEY

    url = urls.AUTH_TOKEN
    auth = HTTPBasicAuth(clientId, secretKey)
    payload = {"grant_type": "client_credentials"}
    headers = {"content-type": "application/x-www-form-urlencoded"}

    response = req.post(url, auth=auth,data=payload,headers=headers)

    return response.content