
import time
import requests
import hmac
from hashlib import sha256

APIURL = "https://api-app.qq-os.com/api/v3/trader/orders/v3?uid=1173556654743941121&pageId=0&pageSize=10&apiIdentity=1194211014359031809&copyTradeLabelType=1";
APIKEY = "tYQlxMgZdl7gIXjUhD7uf2tP6K52KbHJvaE0tU3X3v2a38rOJhQEYOEVLDd5i7IxWsCainbsRgeXoOFyI5wag"
SECRETKEY = "nHI0gP3hNhs1pUnfFJZm45h52UKC9RRoDriYQPYXzCCinO1G2EPUI9bbrcKTRjhONXy4YbABnf5u4JSGnuzg"

def demo():
    payload = {
        "uid": "1173556654743941121",
        "pageId": "0",
        "pageSize": "10",
        "apiIdentity": "1194211014359031809",
        "copyTradeLabelType": "1",
    }
    path = '/api/v3/trader/orders/v3?uid=1173556654743941121&pageId=0&pageSize=10&apiIdentity=1194211014359031809&copyTradeLabelType=1'
    method = "GET"
    paramsMap = {
    "symbol": "BTC-USDT",
    "orderId": 0,
    "startTime": 0,
    "endTime": 0,
    "limit": "500",
    "recvWindow": 0,
    "timestamp": "1696094307214"
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
    # print("demo:", demo())
    metod = "GET"
    path =  "/api/v3/trader/orders/v3?uid=1173556654743941121&pageId=0&pageSize=10&apiIdentity=1194211014359031809&copyTradeLabelType=1"
    payload = {
        "uid": "1173556654743941121",
        "pageId": "0",
        "pageSize": "10",
        "apiIdentity": "1194211014359031809",
        "copyTradeLabelType": "1",
    }
    urlpa = "/api/v3/trader/orders"
    print(send_request(metod, path, urlpa, payload))

   