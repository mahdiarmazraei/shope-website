
import time
import requests
import hmac
from hashlib import sha256

APIURL = "https://api-app.qq-os.com/api/v3/trader/orders/v3?uid=1210989152672821256&pageId=0&pageSize=10&apiIdentity=0&copyTradeLabelType=1";
APIKEY = "jteFieGvPSaJ1FE5fH4FBXpoGvfVxxLVXIbZe1D8pZ2fwpNfq9PNnNiVkaNLZf03oBiT1LwTOHycFdfhzVA"
SECRETKEY = "SURfvXEGKfMVQS6t6Qkj68xduKybmjkqPozEJ7l03aNMbDhJzWqmoFgv0nQlhe2Cpw2Kb6ScNEB9AfXrkGQ"

def demo():
    payload = {}
    path = '/api/v3/trader/orders/v3?uid=1210989152672821256&pageId=0&pageSize=10&apiIdentity=0&copyTradeLabelType=1'
    method = "GET"
    paramsMap = {
    "symbol": "BTC-USDT",
    "orderId": "1210989152672821256",
    "startTime": 0,
    "endTime": 0,
    "limit": "500",
    "recvWindow": 0
}
    paramsStr = praseParam(paramsMap)
    return send_request(method, path, paramsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, urlpa, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlpa, get_sign(SECRETKEY, urlpa))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def praseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsStr = "&".join(["%s=%s" % (x, paramsMap[x]) for x in sortedKeys])
    return paramsStr+"&timestamp="+str(int(time.time() * 1000))


if __name__ == '__main__':
    print("demo:", demo())
