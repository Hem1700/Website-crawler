import requests


def request(url):
    try:    
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass    

target_url = "google.com"
with open("C:\\Users\\dharm\\PycharmProjects\\crawler\\subdomains.txt", "r") as word_list:
    for line in word_list:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(target_url)
        if response:
            print("[+] Discovered a subdomain --> " + test_url)

  