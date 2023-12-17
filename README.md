天气预警自动发送邮件

本项目使用和风天气的API，具体见开发文档https://dev.qweather.com/docs/configuration/project-and-key/

历史天气预警记录自动保存到weather_report.csv文件中。

默认每6个小时更新一次，如果需要调整时间。请修改workflow/main.yml中cron后面的参数。不懂可以自己搜索cron相关参数。

![image](https://github.com/jinde98/weatherwarn/assets/127750182/03bef2b3-7d94-4e98-b9a2-b8767f6d108d)

可以fork本项目自行部署，但需要设置自己的API_KEY和自己邮箱发件SMTP服务器。

发件邮箱的密码需要在项目Setting>>Actions secrets and variables>>Repository secrets中添加 自己的EMAIL_PASSWORD密码
![image](https://github.com/jinde98/weatherwarn/assets/127750182/a3f89047-7bfc-4c6f-b08d-0c69e17a7d63)

自己发件邮箱、收件箱、邮箱smtp及端口需要根据自己的来修改config.json中的配置，如果是outlook的smtp服务器和端口可以不修改了，默认就是找个。

和风天气的API key可以自己去申请，免费的key每天可以一天可以申请获得1000条信息。本项目中的key，调试中使用，如有需要自己去申请。

日后待完善功能。

本项目为第一个ithub部署自动运行项目，自己学习为主。
