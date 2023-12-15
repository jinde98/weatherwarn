import json
from run_github import send_email 


if __name__ == '__main__':
    with open('config.json', 'r', encoding='utf-8') as f:
        res = json.loads(f.read())

    email_settings = res['email_settings']
    send_email('测试' ,[{'信息key': '信息value'}], **email_settings)