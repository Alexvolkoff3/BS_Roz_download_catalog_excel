import requests
from bs4 import BeautifulSoup
from time import sleep


headers = {"User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"}


def get_url():
    for count in range(1, 6):

        url = f"https://bt.rozetka.com.ua/tochechnye-svetilniki/c105283/page={count};producer=videx;sell_status=available/"

        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find_all("li", class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")
        
        for i in data:
            card_url = i.find("a", class_="goods-tile__heading ng-star-inserted").get("href")
            yield card_url


def array():

    for card_url in get_url():

        response = requests.get(card_url, headers=headers)
        sleep(3)
        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find("rz-product", class_="ng-star-inserted")
        prod = data.find("strong", class_="ng-star-inserted").text.strip()
        prod_sts = data.find('rz-status-label', class_="ng-star-inserted").text.strip()
        name_p = data.find("h1", class_="product__title").text.strip()
        pprice = data.find("p", class_="product-prices__big").text.strip()
        img_url = data.find("img", class_="picture-container__picture").get("src")
        yield prod, prod_sts, name_p, pprice, img_url, card_url
