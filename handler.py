import json
from src.components.pay import pay


def payWithPaypal(event, context):

    data = event.get('body')

    payResponse = pay(data)

    print("Pay response",payResponse)
    print(type(payResponse))

    

    response = {
        "statusCode":200,
        "body": json.dumps(json.loads(payResponse))
    }
    return response