from bs4 import BeautifulSoup
import requests, csv
import re
def remove_tags(html):
    for data in html(['style', 'script']):
        data.decompose()
    return ' '.join(html.stripped_strings)

products_found = {}

file = open('export_data.csv', 'w', newline='')
writer = csv.writer(file)
headers = ["name",
            "link",
            "image",
            "description",
            "reference",
            "price_tunisianet",
            "availability_tunisianet"]
writer.writerow(headers)
for page in range(1, 31):

    url = f"https://www.tunisianet.com.tn/702-ordinateur-portable?page={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    
    products = doc.find_all(class_="thumbnail-container text-xs-center")
    for product in products:

        product_link_div = product.find(class_="wb-image-block col-lg-3 col-xl-3 col-md-4 col-sm-4 col-xs-6")
        link = str(product_link_div.find("a")["href"])
        image = str(product_link_div.find("a").find("img")["src"])
        
        product_desc_div = product.find(class_="wb-product-desc product-description col-lg-5 col-xl-5 col-md-6 col-sm-6 col-xs-6")
        title_div = product_desc_div.find(class_="h3 product-title")
        name = str(title_div.find("a").string)
        reference = str(product_desc_div.find("span").string[1:-1])
        desc_div = product_desc_div.find(class_="listds")
        description_div = desc_div.find("a")
        description = str(remove_tags(description_div))

        price_div = product.find(class_="wb-action-block col-lg-2 col-xl-2 col-md-2 col-sm-2 col-xs-12")
        price_tunisianet = str(price_div.find(class_="product-price-and-shipping").find("span").string)
        availability_tunisianet = str(price_div.find(id="stock_availability").find("span").string)
        # products_found[product] = {
        #     "name": name,
        #     "link": link,
        #     "image": image,
        #     "description": description,
        #     "reference": reference,
        #     "price_tunisianet": price,
        #     "availability": availability,
        # }
        file = open('export_data.csv', 'a', newline='', encoding='utf-8')
        writer = csv.writer(file)
        headers = ([name, link, image, description, reference, price_tunisianet, availability_tunisianet])
        writer.writerow(headers)
        file.close()


