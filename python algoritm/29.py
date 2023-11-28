import requests
import json
import calendar
import time

current_GMT = time.gmtime()

time_stamp = calendar.timegm(current_GMT)
x = 0
url = 'https://api-app.luck-in.com/api/v3/trader/orders/v3?uid=1046719849098305537&pageId={}&pageSize=10&apiIdentity=0&copyTradeLabelType=1'.format(x)

headers = {
    "authority": "api-app.luck-in.com",
    "method" : "GET",
    "path": "/api/v3/trader/orders/v3?uid=1046719849098305537&pageId=0&pageSize=10&apiIdentity=0&copyTradeLabelType=1",
    "scheme": "https",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9,fa;q=0.8,fr;q=0.7",
    "App_version": "4.73.7",
    "Appid": "30004",
    "Channel": "copychadingSEO",
    "Device_id": "69a7a4d2b6e74893acd2c34ff72edee7",
    "Lang": "en",
    "Mainappid": "10009",
    "Origin": "https://bingx.com",
    "Platformid": "30",
    "Referer": "https://bingx.com/",
    "Reg_channel": "copychadingSEO",
    "Sec-Ch-Ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "Sign": "C54A4851C98AD36C00DE3BF74437C2CDD8456C66F49BAF89433CE3E41CB95C5A",
    "Timestamp": "1696434182686",
    "Timezone": "3.5",
    "Traceid":"8bf60a2c6a194cc8b0b03dda4e52377f",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Visitorid": "-1",

}
payload = {
    "uid": "1046719849098305537",
    "pageId": "0",
    "pageSize": "10",
    "apiIdentity": "0",
    "copyTradeLabelType": "1",
}

r = requests.get(url,headers=headers, params=payload)
print(r.status_code)
x = r.json()
for k,v in x.items():
    print(f"{k}={v}")

