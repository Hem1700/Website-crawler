import requests
import re
import urllib.parse


target_url = "10.0.2.4/mutillidae/"
webpage_links = []

def extract_link(url):
# To get all the links on a webpage 
    repsonse = requests.get("http://" + url)
    return re.findall('(?:href=")(.*?)"', str(repsonse.content))

href_link = extract_link(target_url)
for link in href_link:
    link  = urllib.parse.urljoin(target_url, link)

    if '#' in link:
        link = link.split('#')[0]

    if target_url in link and link not in webpage_links:
        webpage_links.append(link)
        print(href_link)


def get_subdomains(url):
# To check the subdomains 
    with open("C:\\Users\\dharm\\PycharmProjects\\crawler\\subdomains.txt", "r") as word_list:
        for line in word_list:
            word = line.strip()
            test_url = word + "." + url
            response = requests.get(url)
            if response:
                print("[+] Discovered a subdomain --> " + test_url)


def get_directories(url):
# To check directories
    with open("C:\\Users\dharm\\PycharmProjects\\crawler\\directories.txt", "r") as directory_list:
        for line in directory_list:
            directory = line.strip()
            direct_url =  url + "/" + directory
            response = requests.get(url)
            if response:
                print("[+] Discovered URL --> " + direct_url)



