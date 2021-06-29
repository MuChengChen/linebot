# Linebot-project

## Table of contents
* [About The Project](#about-the-project)
* [Technologies](#technologies)
* [Getting Started](#getting-started)
* [Check](#check)

## About The Project
The goal of this project is to build an APP to help university students reduce their unnecessary living expenses.

Here's the function of APP :
* Chart function : Show the comparison of before and future's living expenses, percentage of monthly expenses, etc.
* Price comparison function : Compare different price on different online shop.
* Reminder function : When users did not track their expenses in two days, the reminder will notice users in next day.
* Consume analyze function: Compare each term of expenses of users with university students.
* Balance inquiry function : Until the end of a month, show the average amount of money which can be used per day. 
* Modify data function: Able to revise the numbers that users had already input.
* Expenses inquiry function : Search for the Xth expenses, the expenses of today, etc.

## Technologies
Project is created with :
* Python version : 3.9.2
* Django version : latest

## Getting Started
This is an example of how you may give instructions on setting up your project locally. To get a local copy up and running follow these simple example steps.

### Prerequisites
```
$ pip install django
$ pip install line-bot-sdk
```
* Create a linebot account 
1. Copy the channel secret and channel access token of your account's basic setting to connect python script and Line Bot.
2. Open final project folder and open setting.py.
3. Change line 24 and 25 to users' channel secret and channel access token.

* Ngrok
1. Sign up for [ngrok](https://ngrok.com/) and download file which is coressponding to your computer's version.  
2. Unzip the file and enter `$ ngrok authtoken <your authtoken>` and `$ ngrok http 8000`
![](https://playlab.computing.ncku.edu.tw:3001/uploads/upload_e4f71cf1b9cde8300de6b8db6919663d.png)
3. Copy the link generate by ngrok to Webhook URL in Line Messaging API and add `/callback`.
4. Open Use webhook
![](https://playlab.computing.ncku.edu.tw:3001/uploads/upload_d266b21c2251bbcaf372b6c18742e492.png)

### Installation
1. Open the terminal and enter :

```
$ pip install matplotlib
$ pip install pandas
$ pip install numpy
$ pip install dateutil
$ pip install apscheduler
$ pip install gspread
$ pip install oauth2client.service_account
$ pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
$ pip install beautifulsoup4
$ pip install regex
$ pip install selenium
```
### Richmenu

1.另外創一個叫richmenu.py的檔案
輸入以下程式碼 run 一次
會得到richmenu id
```python=
import requests
import json

headers = {"Authorization":"Bearer your channel access token","Content-Type":"application/json"}       # 打上你的 access token

body = {
    "size": {"width": 2500, "height": 1686},
    "selected": "true",
    "name": "Controller",
    "chatBarText": "選單",
    "areas":[
        {
          "bounds": {"x": 0, "y": 0, "width": 833, "height": 833},
          "action": {"type": "message", "text": "記支出"}
        },
        {
          "bounds": {"x": 833, "y": 0, "width": 833, "height": 833},
          "action": {"type": "message", "text": "圖表"}
        },
        {
          "bounds": {"x": 1666, "y": 0, "width": 833, "height": 833},
          "action": {"type": "message", "text": "比價"}
        },
        {
          "bounds": {"x": 0, "y": 843, "width": 833, "height": 833},
          "action": {"type": "message", "text": "記收入"}
        },
        {
          "bounds": {"x": 833, "y": 843, "width": 833, "height": 833},
          "action": {"type": "message", "text": "修改資料"}
        },
        {
          "bounds": {"x": 1666, "y": 843, "width": 833, "height": 833},
          "action": {"type": "message", "text": "查詢"}
        }
    ]
  }

req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu',
                       headers=headers,data=json.dumps(body).encode('utf-8'))

print(req.text)                    #  得到選單 id

```
2.再創一個叫rich2.py的檔案
輸入以下程式碼
run 一次
圖片(richmenu.jpg)要跟rich2.py放在同一層資料夾
```
from linebot import (
    LineBotApi, WebhookHandler
)

line_bot_api = LineBotApi('your channel access token')         # 改成自己的token

with open("richmenu.jpg", 'rb') as f:                              # 輸入圖片檔名
    line_bot_api.set_rich_menu_image("your rich menu id", "image/jpeg", f)        # 輸入richmenu id

import requests
headers = {"Authorization":"Bearer your channel access token","Content-Type":"application/json"}         # 改成自己的token
req = requests.request('POST', 'https://api.line.me/v2/bot/user/all/richmenu/your rich menu id',
                       headers=headers)                          # 輸入richmenu id

print(req.text)
```

### Execute the Line Bot:
* Find views.py in moneyapp folder and open it.
* In views.py, change line 72 to your own PATH.
  (just input the PATH exclude \linebot)
* Open terminal and enter `$ python manage.py runserver`.
* Go back to Webhook URL, click the button "Verify", Line Bot will work if succeed.

## Check
Check whether the input data has been correctly upload or not.
* Expenses data: 
https://docs.google.com/spreadsheets/d/19OiyE1Pqp44BTDD9cXtpebntvuQHmPYRTLDy_OJCi2c/edit?usp=sharing

* Income data: 
https://docs.google.com/spreadsheets/d/1OGn7xzKwI8xySKstNWhpnqglK3AzooVPT11MCBAOGH4/edit?usp=sharing

* Budget data: 
https://docs.google.com/spreadsheets/d/14VUMIPWXfOynfr_Eixa8S2La7ksA-3i5zTWWTUd-8JA/edit?usp=sharing

* Picture of the chart function: 
https://drive.google.com/drive/folders/1C-84x5gomshiGb1wxDxemewMyLwwsU1m
