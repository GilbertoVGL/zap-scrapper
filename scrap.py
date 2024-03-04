import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup

default_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
url = "https://www.zapimoveis.com.br/aluguel/imoveis/go+goiania/"
rent = "aluguel"
buying = "venda"
where = ",Goiás,Goiânia,,,,,city,BR>Goias>NULL>Goiania,-16.686891,-49.264794,"

def scrap():
    query = urlencode({"onde": where, "transacao": rent, "pagina": 1})
    r = requests.get(url=url, params=query, headers=default_headers, timeout=2)
    print(f"[ {r.status_code} ] - {r.reason}: {r.url}")

    soup = BeautifulSoup(r.content, 'lxml')
    print("title:", soup.title.text)

    for price_div in soup.find_all("div", class_="listing-price"):
        print(f"price: {price_div.p.text}")

if __name__ == "__main__":
    print("Hello")
    scrap()
    print("finished")
