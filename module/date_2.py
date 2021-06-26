import csv, time, urllib.request
from dateutil import parser
from apscheduler.schedulers.blocking import BlockingScheduler
import line_chatbot_2

def job_function(user_data_dict):
    for key, value in user_data_dict.items():
        if value >= 0:
            print(key)
            msg = line_chatbot_2.linebot_push_message(user_id = key)
            print(msg)

nowtime = time.localtime()
year, month, day = nowtime.tm_year, nowtime.tm_mon, nowtime.tm_mday
nowtime_str = time.strftime("%Y-%m-%d %H:%M:%S", nowtime)
    
url = "https://docs.google.com/spreadsheets/d/19OiyE1Pqp44BTDD9cXtpebntvuQHmPYRTLDy_OJCi2c/export?format=csv"
webpage = urllib.request.urlopen(url)
data = csv.DictReader(webpage.read().decode('utf-8-sig').splitlines())

user_data_dict = dict()
for i in data:
    user_data_dict[i["userid"]] = (parser.parse(nowtime_str) - parser.parse(i["時間"][0:10])).days
print(user_data_dict)
sched = BlockingScheduler()
sched.add_job(job_function, 'cron', month=str(month), day=str(day), hour='12,18,22', minute="0",args=[user_data_dict])
sched.start()
