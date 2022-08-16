import requests
from bs4 import BeautifulSoup

url = "https://habr.com/ru/flows/develop/"
r = requests.get(url)
src = r.text

with open("index.html", "w", encoding = "utf-8-sig") as file:
    file.write(src)
    
with open("index.html", "r", encoding = "utf-8") as file:
    soup = BeautifulSoup(file, "lxml")
st = soup.find_all(class_="tm-article-snippet__title-link")

for i in st:
    part_of_link = link.get("href")
    print(i.text, f"https://habr.com{part_of_link}")
