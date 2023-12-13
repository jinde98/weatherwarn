import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_email(city, datas):
    message_text = ""
    for data in datas:
        message = "\n".join(f"{key}: {value}" for key, value in data.items())
        if message_text:  # 如果message_text不为空，则先添加两个换行符
            message_text += '\n\n'
        message_text += message  # 追加当前消息
    # SMTP服务器配置
    smtp_server = 'smtp.163.com'  # SMTP服务器地址
    smtp_port = 25  # SMTP服务端口
    from_email = 'jinde98@163.com'  # 发件人邮箱
    to_email = 'huaguorong@app.com.cn'  # 收件人邮箱
    password = os.environ['EMAIL_PASSWORD']  # 从环境变量获取邮箱密码或授权码

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = f'{city}气象预警信息'
    msg.attach(MIMEText(message_text, 'plain'))

    # 发送邮件
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # 启用安全传输模式
        server.login(from_email, password)
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()
        print("邮件发送成功")
    except Exception as e:
        print(f"邮件发送失败: {e}")

def run():
    citys = [
        ("如东", "101190504"),
        ("镇江", "101190301"),
        ("钦州", "101301101"),
        ("清远", "101281301"),
        ("孝感", "101200401"),
        ("淄博", "101120301"),
        ("儋州", "101310205"),
        ("宁波", "101210401"),
        ("盐城", "101190701"),
        ("北京", "101010100"),
        ("昆山", "101190404")
    ]

    url = 'https://devapi.qweather.com/v7/warning/now'
    key = os.environ['API_KEY']  # 从环境变量获取API密钥

    for city, code in citys:
        params = {
            'location': code,
            'lang': 'zh',
            'key': key
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # 如果响应状态码不是200，则抛出异常
            datas = response.json().get('warning')
            if datas:
                send_email(city, datas)
        except requests.RequestException as e:
            print(f"Error occurred when retrieving data for {city}: {e}")

if __name__ == '__main__':
    run()
