import requests


response = requests.get('https://scrapethissite.com/pages/advanced/?gotcha=headers', headers={'Accept': 'text/html', 'User-Agent': 'Mozilla'})

# print(response.text)
assert "bot detected" not in response.text
