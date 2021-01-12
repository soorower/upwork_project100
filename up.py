from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import string


def disease(letter):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
    r = requests.get('https://www.mayoclinic.org/diseases-conditions/index?letter='+letter, headers=headers)#, proxies=proxies)
    content = r.content
    soup = BeautifulSoup(content, 'lxml')
   
    print(f'for letter {letter}:')
   
    data_table = soup.find('div', attrs ={'class': 'index content-within'})
    all_data = data_table.findAll('li')
    for d in all_data:
        all1=[]
        name = d.find('a')
        all1.append(name.text)
        print(all1)

letters = string.ascii_uppercase
lette = list(letters)
for i in lette:
    print(disease(i))


# python up.py