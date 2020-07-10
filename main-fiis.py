import requests
from bs4 import BeautifulSoup


agencia = ['BBPO11', 'RBVA11']
escritorio = ['HGRU11', 'RECT11', 'RNGO11']
logistica = ['FIIB11', 'GGRC11', 'GRLV11', 'HGLG11', 'KNRI11', 'LVBI11', 'NEWL11', 'SDIL11', 'VILG11', 'VVPR11', 'XPIN11']
papel = ['HABT11', 'HCTR11']
shopping = ['ABCP11', 'FVPQ11', 'HGBS11', 'MALL11', 'SCPF11', 'VISC11', 'XPML11']
hospital = [ 'NSLU11','HCRI11']


fiis = [agencia, escritorio, logistica, papel, shopping, hospital]

print(','.join(['ticker', 'tipo', 'preco', 'rendimento', 'dy']))

for categoria in fiis:
    for f in categoria:
    
        url = 'https://fiis.com.br/'+f
        
        # inciando uma sessao
        s = requests.Session()
        
        # obtendo a pagina da url
        response = s.get(url)
        
        # criando nossa sopa
        soup = BeautifulSoup(response.text, 'html.parser')
        
        #buscando a tabela pelo id
        table = soup.find(id='last-revenues--table')
        
        # buscando por todos os elmentos  'tr' dentro da tabela e acessando a segunda posicao
        linha2 = table.findAll('tr')[1]
        
        # dentro da linha, buscamos por todos os elementos 'td' e acessamos a ultima posicao
        ultima_celula = linha2.findAll('td')[-1]

        # obtemos e tratamos o texto da celula
        rendimento = float(ultima_celula.get_text().replace('R$','').replace(',','.').strip())
        
        
        # find 
        # findChild
        
        # find_all
        # findChildren

	# encadeamos comandos para o código ficar mais Pythonizado
	# buscamos um elemento div com atributo 'class' cujo valor e 'item quotation'
	# em seguida, buscamos por todos os elementos span com atributo 'class' cujo valor é 'value'
        preco = soup.find('div', {'class' : 'item quotation'}).findChild('span', {'class' : 'value'}).get_text() 
        preco = float(preco.replace(',', '.').strip())
        
        
        # buscamos por um elemento 'div' com 'id' cujo valor eh 'informations--basic'
        # em seguida, buscamos por todos os div aninhados e acessamos o primeiro
        row = soup.find('div', {'id':'informations--basic'}).findAll('div')[0]
        

        # buscamos por todos os elementos div com atributo 'class' cujo valor eh 'item e acessamos o segundo
        # em seguida, buscamos como  filho um elemento 'span' com atributo 'class' cujo valor eh 'value'
        tipo = row.findAll('div', {'class':'item'})[1].findChild('span', {'class':'value'}).get_text().replace(':','')
        
        # printamos separado por ',' para gerar um arquivo csv
        print('%s,%s,%.2f,%.2f,%.2f'%(f,tipo, preco, rendimento, (rendimento/preco)*100))