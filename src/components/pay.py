import json
from src.components.getToken import getAccessToken
import src.constants.urls as urls
import requests as req



def pay(data):

    token = getAccessToken()
    token = json.loads(token)

    authToken = token.get('access_token')
    print("Token", authToken)
    url = urls.PAYOUT
    headers = {
        "Authorization": "Bearer {token}".format(token=authToken),
        "content-type": "application/json"
    }
    payload  = {
        "sender_batch_header": {
        "sender_batch_id": "2014021806",
        "recipient_type": "EMAIL",
        "email_subject": "You have money!",
        "email_message": "You received a payment. Thanks for using our service!"
    },
    "items": [
        {
        "amount": {
            "value": "5.00",
            "currency": "USD"
        },
        "sender_item_id": "201403140006",
        "recipient_wallet": "PAYPAL",
        "receiver": "sb-43xbfg6263844@personal.example.com"
        }
    ]
    
    }

    response = req.post(url, headers=headers, data=json.dumps(payload))
    print("Response",response)
    print("Content",response.content)

    return response.content