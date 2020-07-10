from bs4 import BeautifulSoup

html = '<div id=preco>20,00</div><div id=desconto>5.00</div>'
soup = BeautifulSoup(html)

soup.find('div')
soup.findAll('div')
soup.findAll('div', {'id': 'preco'})

preco_div = soup.find('div', {'id': 'preco'})
preco = preco_div.get_text()
print(preco)