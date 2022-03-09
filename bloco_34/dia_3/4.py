import requests
from parsel import Selector


start_url = 'http://books.toscrape.com/catalogue/'
fetch_url = start_url + 'the-grand-design_405/index.html'

response = requests.get(fetch_url)

selector = Selector(text=response.text)

title = selector.css('h1::text').get()
price = selector.css('p.price_color::text').re_first(r"\d+\.\d{2}")
description = selector.css('article.product_page > p::text').get()

suffix = '...more'
if suffix in description:
    description = description[:-len(suffix)]

image_src = selector.css('div.active img::attr(src)').get()
image_url = start_url + image_src[6:]

quantity = selector.css('table.table-striped tr:nth-of-type(6) > td::text').re_first(r"\d")

print(f"{title}, {price}, {description}, {image_url}, {quantity}")
