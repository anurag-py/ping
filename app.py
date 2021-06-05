from flask import Flask
import requests
import subprocess


app = Flask(__name__)

@app.route("/")
def index():
    flag = True
    while(flag):
        response = requests.get("http://punlaonline.herokuapp.com")
        print(response.status_code)
        if response.status_code == 200:
            flag=False
            break
    subprocess.call(["python","ping.py"], shell=False)
    

    return "Flag is %s " % flag