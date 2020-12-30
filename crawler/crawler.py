import bs4
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0'}

result = requests.get("https://www.amazon.com/s?i=aps&k=flask%20development", headers=headers)
amazon_page = result.text #open('amazon_flask.html','r')
soup = bs4.BeautifulSoup(amazon_page, features="lxml")


titles = soup.findAll('span',{"class":"a-size-base-plus a-color-base a-text-normal"})

rows = soup.findAll('div',{"class":"sg-row"})

all_rows = True
previous_title = None
for row in rows:
    inners = row.findAll('div',{"class":"sg-col-inner"})
    print(inners)
    for inner in inners:
        title = inner.findAll('span',{"class":"a-size-base-plus a-color-base a-text-normal"})
        if len(title) == 1 and previous_title!=title[0].text:
            if all_rows:
                all_rows = False
                continue
            previous_title=title[0].text
            price = inner.findAll('span',{"class": "a-price", "data-a-size":"l"})
            if len(price) > 0:
                review = inner.findAll('span',{"class":"a-icon-alt"})
                print(title[0].text)
                print(price[0].next_element.text)