import requests
import json
import os
from datetime import datetime

push_url = 'http://pushplus.hxtrip.com/send/'
push_token = os.environ['PUSH_PLUS_TOKEN']
push_msg = {
    'token': push_token,
    # 'template': 'html'
}

def send_msg(msg):
    body=json.dumps(msg).encode(encoding='utf-8')
    headers = {'Content-Type':'application/json'}
    r = requests.post(push_url,data=body,headers=headers)
    print(r.text)

if __name__ == '__main__':
    now = datetime.now()
    push_msg['title'] = "Github Action 运行通知"
    push_msg['content'] = "现在的时间是: {}".format(now)
    send_msg(push_msg)
