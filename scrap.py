import argparse
import requests
import json
from urllib.parse import urlencode
from bs4 import BeautifulSoup

default_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
rent = "aluguel"
buying = "venda"
where = ",Goiás,Goiânia,,,,,city,BR>Goias>NULL>Goiania,-16.686891,-49.264794,"

def scrap(city: str, state: str):
    url = "https://www.zapimoveis.com.br/aluguel/imoveis/go+goiania/"
    query = urlencode({"onde": where, "transacao": rent, "pagina": 1})

    r = requests.get(url=url, params=query, headers=default_headers, timeout=2)
    print(f"[ {r.status_code} ] - {r.reason}: {r.url}")

    soup = BeautifulSoup(r.content, 'lxml')
    print("title:", soup.title.text)

    for price_div in soup.find_all("div", class_="listing-price"):
        print(f"price: {price_div.p.text}")

def location(target_city: str, target_state: str):
    url = "https://glue-api.zapimoveis.com.br/v3/locations?"
    params = {
        "portal": "ZAP",
        "fields": "neighborhood,city,account,condominium,poi,street",
        "includeFields": "address.neighborhood,address.city,address.state,address.zone,address.locationId,address.point,url,advertiser.name,uriCategory.page,condominium.name,address.street",
        "size": 6,
        "q": target_city,
        "amenities": "Amenity_NONE",
        "constructionStatus": "ConstructionStatus_NONE",
        "listingType": "USED",
        "businessType": "SALE",
        "unitTypes": "",
        "usageTypes": "",
        "unitSubTypes": "",
        "unitTypesV3": "",
        "__vt": "",
    }

    b = get(url, params, {"Authorization": "Bearer "})
    try:
        payload = json.loads(b)
        locations = payload.get("city", {}).get("result", {}).get("locations")
        for location in locations:
            state = location.get("address", {}).get("state")
            city = location.get("address", {}).get("city")

            if not isinstance(state, str) or not isinstance(city, str):
                continue

            if state == target_state and city == target_state:
                return location
        return None

    except (json.JSONDecodeError, TypeError):
        return None



def get(url, params, headers = {}) -> bytes:
    headers = default_headers.update(headers)
    r = requests.get(url=url, params=params, headers=headers, timeout=2)
    print(f"[ {r.status_code} ] - {r.reason}: {r.url}")

    return r.content

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A CLI to help you scrape real state data from Zap Imóveis")
    parser.add_argument("-city", "-c", required=True, help="City to look for real state")
    parser.add_argument("-state", "-s", required=True, help="State to look for real state")
    args = parser.parse_args()

    print(f"Scraping in: {args.city} - {args.state}")

    loc = location(args.city, args.state)
    print("location:", location)
    # scrap(args.city, args.state)

    print("finished scraping")
