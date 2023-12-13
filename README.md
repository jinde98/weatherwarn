天气预警自动发送邮件

历史天气预警记录自动保存到weather_report.csv文件中。

默认每6个小时更新一次，如果需要调整时间。请修改workflow/main.yml中cron后面的参数。不懂可以自己搜索cron相关参数。

![image](https://github.com/jinde98/weatherwarn/assets/127750182/03bef2b3-7d94-4e98-b9a2-b8767f6d108d)

可以fork本项目自行部署，但需要设置自己的API_KEY和自己邮箱发件SMTP服务器。
