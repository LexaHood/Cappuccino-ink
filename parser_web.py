import requests
from bs4 import BeautifulSoup
import lxml
from packege_class import net_packege_printer


def check_web_conection(ip):
    try:
        requests.get('http://' + ip + '/general/status.html')
        return True
    except requests.exceptions.ConnectionError:
        return False


def parcer_web_brother(cell: net_packege_printer):
    r = requests.get('http://' + cell.get_ip() + '/general/status.html') #отправляем HTTP запрос и получаем результат
    soup = BeautifulSoup(r.text, features='lxml') #Отправляем полученную страницу в библиотеку для парсинга
    tables=soup.find_all(['td']) #Получаем все таблицы с вопросами
    #print (tables)
    line = str(tables)
    #print (line, "\t", type(line))
    index_start = line.find('height=') + 1
    index_start = line.find('"', index_start) + 1
    index_end = line.find('"',index_start + 1)
    level_toner = int(line[index_start : index_end]) * 1.75
    cell.add_toner(level_toner)
    #print (level_toner)
    #print("toner status", level_toner, "%")
    return cell
