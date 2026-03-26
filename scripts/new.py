from bs4 import BeautifulSoup
import pandas as pd
import requests

web = "https://loveandflair.com/"

p_link = []



r = requests.get("https://loveandflair.com/collections/activewear-1")
soup = BeautifulSoup(r.content,"html.parser")

p_list = soup.find_all("li", class_="collection-product-card quickview")
for item in p_list:
    for link in item.find_all("a",href = True):
        p_link.append(web + link["href"])

all_products = []
for link in p_link:
    r = requests.get(link)
    soup = BeautifulSoup(r.content,"html.parser")
    
    title = soup.find("h4",class_="product__title")
    top = title.text.strip()
    
    price_tag = soup.find("span",class_="money")
    price = price_tag.text.strip()
    
    in_stock_tag = soup.find("span", class_="advantage_title")
    in_stock = in_stock_tag.text.strip() if in_stock_tag else "N/A"
   
    available_size = soup.find("input",{"name": "Size", "checked": True})
    size = available_size["value"] if available_size else "N/A"

    p_list = {
        "Tops":top,
        "price": price,
        "Stock": in_stock,
        "Size": size,
    }
    
    all_products.append(p_list)
    
df = pd.DataFrame(all_products)
df.to_csv("all_product.csv", index=False)