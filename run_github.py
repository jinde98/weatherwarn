import json
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from pathlib import Path
import pandas as pd

csv_filename = 'weather_report.csv'

def save_csv(datas: [dict]) -> None:
    '''
        保存csv文件
        param: datas: [{key: value}]
        return: None
    '''
    new_df = pd.DataFrame(datas)
    # 检查文件是否存在
    if Path(csv_filename).exists():
        # 读取现有的数据
        old_df = pd.read_csv(csv_filename)
        # 筛选出那些在旧数据中不存在的新数据
        new_df = new_df[~new_df['id'].isin(old_df['id'])]
        # 如果有新数据，追加到旧数据上
        if not new_df.empty:
            df = pd.concat([old_df, new_df], ignore_index=True)
        else:
            return
    else:
        # 如果文件不存在，直接使用新数据
        df = new_df
    # 保存到CSV文件
    try:
        df.to_csv(csv_filename, index=False)
        print("数据已保存到CSV文件")
    except Exception as e:
        print(f"保存数据到CSV文件时出错: {e}")


def error_log(message: str) -> None:
    '''
        错误记录
        param: message 错误信息
        return: 
    '''
    with open('error.log', 'a', encoding='utf-8') as f:
        f.write(message)


def send_email(
        city: list,
        datas: [dict],
        smtp_server: str,
        smtp_port: int, 
        from_email: str, 
        password: str,  
        to_email: str       
        ) -> None:
    '''
        发送邮件
        params: 
                city: [城市名称, 城市代码] 
                datas: [{key: value}]
                smtp_server: SMTP服务器地址
                smtp_port: SMTP服务器端口
                from_email: 发件人邮箱
                to_email: 收件人邮箱
        return: 
    '''
    message_text = ""
    datas=[{
        'pubTime': item['pubTime'],
        'title': item['title'],
        'text': item['text']
        } for item in datas]
    for data in datas:
        message = "\n".join(f"{key}: {value}" for key, value in data.items())
        if message_text:  # 如果message_text不为空，则先添加两个换行符
            message_text += '\n\n'
        message_text += message  # 追加当前消息

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
        message = f"邮件发送失败: {e}"
        print(message)
        error_log(message)

def run():
    with open('config.json', 'r', encoding='utf-8') as f:
        settings = json.loads(f.read())
    settings['email_settings']['password'] = os.environ['EMAIL_PASSWORD']
    email_settings = settings['email_settings']
    weather_api_settings = settings['api_settings']

    url = weather_api_settings['url']
    key = weather_api_settings['key']
    citys = weather_api_settings['cities']
    new_datas=[]
    new_cities=''
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
            if datas != []:
                new_df = pd.DataFrame(datas)
                # 检查文件是否存在
                if Path(csv_filename).exists():
                    # 读取现有的数据
                    old_df = pd.read_csv(csv_filename)
                    new_ids = new_df[~new_df['id'].isin(old_df['id'])]['id'].tolist()
                    datas = [data for data in datas if data['id'] in new_ids]
                    if datas: 
                        new_datas.extend(datas)
                        new_cities = new_cities + '【' + city + '】' 

                else:
                    new_datas.extend(datas)
                    new_cities = new_cities + '【' + city + '】' 
                    
        except requests.RequestException as e:
            print(f"Error occurred when retrieving data for {city}: {e}")

    if new_datas:
        send_email(new_cities, new_datas , **email_settings)
        save_csv(new_datas)
        

if __name__ == '__main__':
    run()
