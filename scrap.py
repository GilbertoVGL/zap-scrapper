import http.client
import requests
from urllib.parse import urlencode
from bs4 import BeautifulSoup

default_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
host = "www.zapimoveis.com.br"
resource = "/aluguel/imoveis/go+goiania/"
rent = "aluguel"
buying = "venda"
where = ",Goiás,Goiânia,,,,,city,BR>Goias>NULL>Goiania,-16.686891,-49.264794,"

def req_scrap():
    query = urlencode({"onde": where, "transacao": rent, "pagina": 1})
    r = requests.get(url=f"https://{host}{resource}", params=query, headers=default_headers, timeout=2)
    print(f"[ {r.status_code} ] - {r.reason}: {r.url}")
    print("encoding:", r.encoding)
    txt = r.content.decode(r.encoding)
    with open("body_requests.html", "w+") as f:
        f.write(txt)
    soup = BeautifulSoup(txt, 'lxml')
    print("original encoding:", soup.original_encoding)
    print("title:", soup.title)

def scrap():
    query = urlencode({"onde": where, "transacao": rent, "pagina": 1})
    path = f"{resource}?{query}"

    conn = http.client.HTTPSConnection(host=host, timeout=2)
    conn.request("GET", path, headers=default_headers)
    r = conn.getresponse()
    encoding = r.headers.get_content_charset('latin-1')

    print(f"[ {r.status} ] - {r.reason}: {conn.host+path}")
    print("encoding:", encoding)

    body = r.read().decode(r.headers.get_content_charset('latin-1'))
    with open("body_httpclient.html", "w+") as f:
        f.write(body)

    soup = BeautifulSoup(body, 'lxml')
    print("original encoding:", soup.original_encoding)
    print("title:", soup.title)
    for link in soup.find_all('a'):
        print("link:", link.get('href'))


if __name__ == "__main__":
    # scrap()
    req_scrap()
    print("finished")
