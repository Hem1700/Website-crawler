import requests

target_url = "http://10.0.2.4/dvwa/login.php"
login_info_dict ={"username": "admin", "password": "password", "Login": "submit"}
response = requests.post(target_url , data= login_info_dict)
print(response.content)