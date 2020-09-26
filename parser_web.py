import requests
from bs4 import BeautifulSoup
#import pandas as pd
import lxml


def parcer_web(ip):
    url = 'http://' + ip + '/general/status.html'# url страницы
    r = requests.get(url)
    with open('test.html', 'w') as output_file:
        output_file.write(r.text)
    pass


result = pd.DataFrame()

r = requests.get('http://10.1.1.33/general/status.html') #отправляем HTTP запрос и получаем результат
soup = BeautifulSoup(r.text, features='lxml') #Отправляем полученную страницу в библиотеку для парсинга
tables=soup.find_all(['td']) #Получаем все таблицы с вопросами
#print (tables)
line = str(tables)
#print (line, "\t", type(line))
index_start = line.find('height=') + 8
level_toner = line[index_start : index_start + 2]
