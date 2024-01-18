# 天气预警自动发送邮件项目

## 项目概述

这个项目使用和风天气的API，旨在提供天气预警信息，并通过邮件自动发送通知。同时，历史天气预警记录会自动保存到weather_report.csv文件中。

## 配置和使用

### API_KEY 和 邮箱设置

1. 获取和风天气的API_KEY，请参考[开发文档](https://dev.qweather.com/docs/configuration/project-and-key/)。
2. Fork本项目到你的仓库，并设置你自己的API_KEY。
3. 设置发件邮箱的SMTP服务器和密码，以及发件人、收件人等相关信息。详见[设置说明](#设置说明)。

### 配置文件

修改 `config.json` 文件，根据你的需求配置以下信息：

- `cities`: 发送天气预警的城市列表，城市代码可参考[LocationList](https://github.com/qwd/LocationList)中的CSV文件。
- 其他邮件和天气API的配置。

### 更新时间

默认每6个小时更新一次，如果需要调整时间，请修改 `workflow/main.yml` 中cron后面的参数。

## 截图

![示例截图](https://github.com/jinde98/weatherwarn/assets/127750182/03bef2b3-7d94-4e98-b9a2-b8767f6d108d)

## 设置说明

1. 在项目 Settings >> Actions secrets and variables >> Repository secrets 中添加 `EMAIL_PASSWORD` 变量，值为发件邮箱的密码。
   ![设置邮箱密码](https://github.com/jinde98/weatherwarn/assets/127750182/a3f89047-7bfc-4c6f-b08d-0c69e17a7d63)

2. 修改 `config.json` 文件中的邮箱配置，确保SMTP服务器、端口等信息正确。

## 贡献和问题反馈

如果您希望贡献代码或报告问题，请参考贡献指南。我们欢迎您的反馈和建议。

## 致谢

感谢使用本项目，同时感谢和风天气提供的API。

[<img src="https://github.com/hualayn.png" width="50" height="50">](https://github.com/hualayn) [hualayn](https://github.com/hualayn)


