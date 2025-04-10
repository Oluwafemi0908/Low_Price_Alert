import requests
from bs4 import BeautifulSoup


class OnlineStore:
    def __init__(self, url):
        self.url = url
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                      "*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Sec-Ch-Ua": "\"Chromium\";v=\"110\", \"Not A(Brand\";v=\"24\", \"Google Chrome\";v=\"110\"",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/110.0.0.0 Safari/537.36",
          }
        self.response = requests.get(url=url, headers=self.headers)
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        self.product_name = " ".join(self.soup.select_one("#productTitle").getText().split())
        self.price = float(f'{self.soup.select_one("#corePriceDisplay_desktop_feature_div .a-price-whole").getText()}'
                           f'{self.soup.select_one("#corePriceDisplay_desktop_feature_div .a-price-fraction").getText()}')
        print(self.price)
        self.subject = None
        self.body = None

    def compare_price(self, set_price):
        if set_price >= self.price:
            self.subject = "Low Price Alert"
            self.body = f"{self.product_name} is now ${self.price}\n{self.url}"
            return True
