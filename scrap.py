import requests
from bs4 import BeautifulSoup, SoupStrainer, UnicodeDammit

url = "https://www.zapimoveis.com.br/aluguel/imoveis/go+goiania/"
default_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Dnt": "1",
    "Pragma": "no-cache",
    "Sec-Ch-Ua": '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Windows",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

rent = "aluguel"
buying = "venda"
where = ",Goiás,Goiânia,,,,,city,BR>Goias>NULL>Goiania,-16.686891,-49.264794,"

def scrap():
    params = { "onde": where, "transacao": rent, "pagina": 1}
    r = requests.get(url=url, params=params, headers=default_headers, timeout=2)
    print("[ ", r.status_code, " ] -", r.reason, ":", r.url)
    print("[ ", r.encoding, " ]")

    with open("body", "wb+") as f:
        f.write(r.content)

    # soup = BeautifulSoup(txt, 'lxml')
    # print("original encoding:", soup.original_encoding)
    # print("prettify:", soup.prettify())
    # print("title:", soup.title)
    # for link in soup.find_all('a'):
    #     print("link:", link.get('href'))

if __name__ == "__main__":
    # test()
    scrap()
    print("finished")

def test():
    r = requests.get(url="https://www.google.com", timeout=2)
    print("[ ", r.status_code, " ] -", r.reason, ":", r.url)
    print("[ ", r.encoding, " ]")

    soup = BeautifulSoup(r.text, 'html.parser')
    soup.prettify()
    print(soup.get_text())