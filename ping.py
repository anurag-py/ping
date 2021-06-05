import requests
import time
flag = True
while(flag):
    response = requests.get("http://punlaonline.herokuapp.com")
    print(response.status_code)
    time.sleep(60)
    # if response.status_code == 200:
    #     flag=False
    #     break
    

