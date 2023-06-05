import requests

class InvalidUrlError(Exception):
    def __init__(self, url):
        self.url = url
        super().__init__(f"Invalid URL: {url}")

def check_wikipedia_url(url):
    if not url.startswith('https://en.wikipedia.org/wiki/'):
        raise InvalidUrlError(url)

    response = requests.head(url)
    if response.status_code != 200:
        raise InvalidUrlError(url)

    print("Valid Wikipedia URL")

url = 'https://en/wikipedia.org/wiki/4_Vesta'
try:
    check_wikipedia_url(url)
except InvalidUrlError as e:
    print(e)