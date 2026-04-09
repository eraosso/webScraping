
from bs4 import BeautifulSoup
from urllib.request import urlopen


url = "http://www.pythonscraping.com/pages/warandpeace.html"

def retorna_bs(url):
    html = urlopen(url)
    return BeautifulSoup(html.read(), features="html.parser")

bs = retorna_bs(url)
nameList = bs.find_all("span", {'class': 'green'})

for name in nameList:
    print(name.get_text())

lista=bs.find_all('span', {'class': ["green", "red"]})

for x in lista:
    print(x.get_text())


url = "https://www.pythonscraping.com/pages/page3.html"
bs = retorna_bs(url)

for child in bs.find("table", {'id': 'giftList'}).children:
    print(child)

for sibling in bs.find("table", {'id': 'giftList'}).tr.next_siblings:
    print(sibling)

'''
no exemplo abaixo, a imagem é selecionada, 
depois é selecionado o "pai" da imagem que tem tag "td", 
dapois é selecionado seu "previous sibling" (também "td")
e somente aí é que extrai-se o texto
'''
print(bs.find('img',
              {'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())

