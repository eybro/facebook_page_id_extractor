import time
from bs4 import BeautifulSoup
import requests


page_list = []
with open('pages.txt', 'r') as f:
    for line in f:
        page_list.append(line.strip())

page_id_dict = {}

for page in page_list:
    headers = {
        "User-Agent": "Mozilla/5.0"
        }
    request = requests.get(f"https://facebook.com/{page}", headers=headers)
    time.sleep(5)
    soup = BeautifulSoup(request.content, "html.parser")
    head_content = soup.head

    meta_tag = soup.find("meta", {"property": "al:android:url"})
    if meta_tag:
        android_url = meta_tag.get("content")
        print(f"{page} : {android_url}")
        page_id_dict[page] = android_url.split("/")[-1]

with open("output.txt", "w") as f:
    for page, page_id in page_id_dict.items():
        f.write(f"{page} : {page_id}\n")


