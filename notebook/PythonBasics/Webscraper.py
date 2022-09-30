import sys
import requests
from bs4 import BeautifulSoup

res = requests.get('https://en.wikipedia.org/wiki/' + ' '.join(sys.argv[1:]))
res.raise_for_status()
soup = BeautifulSoup(res.text, 'html.parser')
for i in soup.select('p'):
    print(i.getText())
    print()
