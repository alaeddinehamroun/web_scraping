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
            "price_mytek",
            "availability_mytek"]
writer.writerow(headers)
for page in range(1, 56):

    url = f"https://www.mytek.tn/informatique/ordinateurs-portables/pc-portable.html?cat=53%2C56%2C7048%2C57%2C54&p={page}"
    page = requests.get(url).text
    doc = BeautifulSoup(page, "html.parser")
    
    products = doc.find_all(class_="item product product-item product-item-info")
    for product in products:

        product_link_div = product.find(class_="col-lg-2 col-sm-2 col-md-2 col-xs-2 padingRight")
        link = str(product_link_div.find(class_="image-product").find("a")["href"])
        image = str(product_link_div.find(class_="image-product").find("a").find("span").find("span").find("img")["src"])

        product_desc_div = product.find(class_="col-lg-9 col-sm-7 col-md-7 col-xs-7 padingLeft").find(class_="product details product-item-details")
        title_div = product_desc_div.find(class_="desctopNameProduct")
        name = str(remove_tags(title_div))
        
        ref_div = product_desc_div.find(class_="row").find(class_="col-lg-4 col-md-4 col-sm-4 mobileWidth")
        reference = str(remove_tags(ref_div)[1:-1])
        desc_div = product_desc_div.find(class_="product description").find(class_="strigDesc")
        description = str(remove_tags(desc_div))

        price_div = product.find(class_="col").find(class_="mobileNone").find(class_="row align-items-center marginclass displayDesctop").find(class_="mobileWidthLeft").find(class_="priceDesctop").find(class_="price-box price-final_price")
        if price_div.find(class_="special-price"):
            price_mytek =str(price_div.find(class_="special-price").find(class_="price-container price-final_price tax weee").find(class_="price-wrapper").find("span").string)[:-3]+ "DT"
        else:
            price_mytek =str(price_div.find(class_="price-container price-final_price tax weee").find(class_="price-wrapper").find("span").string)[:-3]+ "DT"

        # price_mytek =re.findall(r"[-+]?(?:\d*\,*\d+)", str(remove_tags(price_div)))[0]+" DT"
        avail_div = product.find(class_="col").find(class_="mobileNone").find(class_="row align-items-center marginclass displayDesctop").find(class_="mobileWidthLeft").find(class_="dispoDesc").find(class_="dispo mt-2")
        if(len(remove_tags(avail_div).split(' ', 1))>1):
            availability_mytek = str(remove_tags(avail_div).split(' ', 1)[1])
        else:
            availability_mytek = "Epuisé"

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
        headers = ([name, link, image, description, reference, price_mytek, availability_mytek])
        writer.writerow(headers)
        file.close()


