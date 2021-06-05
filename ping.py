import requests
flag = True
while(flag):
    response = requests.get("http://punlaonline.herokuapp.com")
    print(response.status_code)
    if response.status_code == 200:
        flag=False
        break
    

