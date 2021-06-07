from flask import Flask
import requests
# import subprocess
from flask_apscheduler import APScheduler


# set configuration values
class Config:
    SCHEDULER_API_ENABLED = True

app = Flask(__name__)


# initialize scheduler
scheduler = APScheduler()
# if you don't wanna use a config, you can set options here:
# scheduler.api_enabled = True
# scheduler.init_app(app)

# cron examples
@scheduler.task('cron', id='ping', minute='*')
def job2():
    response = requests.get("http://punlaonline.herokuapp.com")
    print(response.status_code)
    print('Job 2 executed')

scheduler.start()

@app.route("/")
def index():
    flag = True
    while(flag):
        response = requests.get("http://punlaonline.herokuapp.com")
        print(response.status_code)
        if response.status_code == 200:
            flag=False
            break
    
    

    return "Flag is %s " % flag

# @app.route("/app-running")
# def page():
#     subprocess.call(["python","ping.py"], shell=False)
#     return "App is runnning"

