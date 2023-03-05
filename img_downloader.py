import os
import sys
import requests
from bs4 import BeautifulSoup
import time

if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    url = input("画像を取得するURLを入力：")

sub_dir = ""
if len(sys.argv) > 2:
    sub_dir = sys.argv[2] + "/"


str_now = time.strftime("%Y%m%d%H%M%S")
save_dir = "./images/" + sub_dir + str_now

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# HTMLを取得する
res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")

# aタグを取得する
a_tags = soup.find_all("a")

# aタグのhref属性から画像のURLを取得し、保存する
for a in a_tags:
    href = a.get("href")
    if href and (href.lower().endswith((".jpg", ".jpeg", ".png", ".bmp"))):
        print(href)
        img_res = requests.get(href)
        with open(os.path.join(save_dir, os.path.basename(href)), "wb") as f:
            f.write(img_res.content)
