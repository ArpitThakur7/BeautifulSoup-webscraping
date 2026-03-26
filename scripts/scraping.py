import requests
import pandas as pd
from bs4 import BeautifulSoup

books_info = []

webs = "https://quotes.toscrape.com/"

r = requests.get(webs)
soup = BeautifulSoup(r.content,"html.parser")
book = soup.find_all("div", class_="quote")

for item in book:
    
    text = item.find("span",class_="text").text
    
    author = item.find("small",class_="author").text
    
    link = item.find("a")["href"]
    link = "https://quotes.toscrape.com/" + link
    
    tags = [tag.text for tag in item.find_all("a", class_="tag")]
    
    books_info.append({
        "Quote": text,
        "Author": author,
        "Author Link":link,
        "Tags": tags
    })
    
df = pd.DataFrame(books_info)

print(df)

df.to_csv("qoutes.csv",index = False)