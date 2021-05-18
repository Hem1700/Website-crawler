import requests
import re

def request(url):
    try:    
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass    

target_url = "10.0.2.4/mutillidae/"

# To get all the links on a webpage 
repsonse = request(target_url)
href_links = re.findall('(?:href=")(.*?)"', str(repsonse.content))
print(href_links)

# To check the subdomains 
with open("C:\\Users\\dharm\\PycharmProjects\\crawler\\subdomains.txt", "r") as word_list:
    for line in word_list:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(target_url)
        if response:
            print("[+] Discovered a subdomain --> " + test_url)


# To check directories
with open("C:\\Users\dharm\\PycharmProjects\\crawler\\directories.txt", "r") as directory_list:
    for line in directory_list:
        directory = line.strip()
        direct_url =  target_url + "/" + directory
        response = request(direct_url)
        if response:
            print("[+] Discovered URL --> " + direct_url)