import requests
import time
import sqlite3
import sys


from bs4 import BeautifulSoup as BS
from pathlib import Path

print("Подключаемся!...",end='')


ruloto_url="http://www.stoloto.ru/ruslotto/game"
ruloto_get="int=right"
ruloto_get_headers={'Host': 'www.stoloto.ru',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:54.0) Gecko/20100101 Firefox/54.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Referer': 'http://www.stoloto.ru/',
'Cookie': 'isgua=false; K=1502334953085; flocktory-uuid=e41cea7d-25af-412a-b025-c112dc0ba054-9;_vwo_uuid_v2=6DE74A98EBA5B47452AD11BC200ED973|2b0724335ee665d57b9f7f4205fa9aaf;__utma=35201507.437908472.1502335018.1502357192.1502362069.4;__utmz=35201507.1502335018.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none);__sonar=686074347937311293; _ga=GA1.2.437908472.1502335018;__auc=6ad1ccb615dca253862de56127e; _ym_uid=1502335040809830587; welcome=true;SESSION=b7e7c137-54ec-4116-a0a9-113e15b581c3; _gid=GA1.2.986871628.1503892284;_ym_isad=2; tmr_detect=0%7C1503898353945;pregen_player_id=c93bed3f-7396-4cae-8194-0fe941fb9507;JSESSIONID=node011lzzubkrwujb88jcge68y2431096979.node0;__asc=442265d415e2752bdbb7568aa5a; _ym_visorc_15627616=b',
'DNT': '1',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'Pragma': 'no-cache',
'Cache-Control': 'no-cache'}


ruloto_change_url="http://www.stoloto.ru/services/site/game/pregen/ruslotto/change"
ruloto_change_headers={'Host': 'www.stoloto.ru',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:54.0) Gecko/20100101 Firefox/54.0',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'Content-Type': 'application/x-www-form-urlencoded',
'X-Requested-With': 'XMLHttpRequest',
'Referer': 'http://www.stoloto.ru/ruslotto/game?int=right',
'Content-Length': '22',
'Cookie': 'isgua=false; K=1502334953085;flocktory-uuid=e41cea7d-25af-412a-b025-c112dc0ba054-9;_vwo_uuid_v2=6DE74A98EBA5B47452AD11BC200ED973|2b0724335ee665d57b9f7f4205fa9aaf;__utma=35201507.437908472.1502335018.1502357192.1502362069.4;__utmz=35201507.1502335018.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none);__sonar=686074347937311293;_ga=GA1.2.437908472.1502335018;__auc=6ad1ccb615dca253862de56127e;_ym_uid=1502335040809830587;welcome=true;SESSION=b7e7c137-54ec-4116-a0a9-113e15b581c3;_gid=GA1.2.986871628.1503892284;__asc=80f17a1f15e26f744bb6ab1cbc9;_ym_isad=2; _ym_visorc_15627616=w;tmr_detect=0%7C1503892340440;pregen_player_id=c93bed3f-7396-4cae-8194-0fe941fb9507;JSESSIONID=node01ezlqsijd6u881updtficl53ia1081503.node0',
'DNT': '1',
'Connection': 'keep-alive'}
ruloto_change_numbers={'numbersToChange':'[]'}
act_tickets_count=0
circulation_loto=0
# Парсим текущий номер тиража

db_name="tickets"
try:
	ruloto_html=requests.get(url=ruloto_url,data=ruloto_get).text
except:
	input("Не могу подключиться!")
	exit()
print("OK!")
soup=BS(ruloto_html,'html.parser')
circulation_loto=int(BS(str(soup.select('div[class="col col2"]')),'html.parser').h3.contents[0][-4:])

print("Текущий тираж №"+str(circulation_loto))

#need_tickets_count=input('Сколько билетов надо спарсить? - ')\

if len(sys.argv)>1 and sys.argv[1]=='time':
	need_end_time = sys.argv[2]
elif sys.argv[1]=='all':
	need_end_time=time.strftime("%d/%m/%Y - %H:%M:%S",time.localtime(2*time.time()))
else:
	need_end_time=input("До какого времени парсить? (dd/mm/yyyy - hh:mm:ss) - ")

end_time=int(time.mktime(time.strptime(need_end_time,"%d/%m/%Y - %H:%M:%S")))
#print(str(end_time))

db_file=Path('./'+db_name)
if db_file.exists():
	print("Подключение к базе данных "+db_name+".db...",end='')
else:
	print("Создание базы данных "+db_name+".db...",end='')
try:
	db_connection=sqlite3.connect(db_name+".db")
except sqlite3.OperationalError:
	time.sleep(1)
	print("Ошибка!")	
else:
	time.sleep(1)
	print("Успешно!")

cursor=db_connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS table_"+str(circulation_loto)+"(ticket_number INTEGER PRIMARY KEY NOT NULL,numbers TEXT NOT NULL,date_time TEXT NOT NULL)")
start_time=time.time()
print("Начало в "+ time.strftime("%d/%m/%Y - %H:%M:%S",time.localtime(time.time())))
act_time=time.time()

while act_time<end_time :
	act_time=time.time()
	if time.localtime(act_time).tm_wday==5:
		break
	try: 
		req=requests.post(url=ruloto_change_url,headers=ruloto_change_headers,data=ruloto_change_numbers)
		ruloto_html=requests.get(url=ruloto_url,data=ruloto_get).text
		soup=BS(ruloto_html,'html.parser')
		circulation_loto=int(BS(str(soup.select('div[class="col col2"]')),'html.parser').h3.contents[0][-4:])
	except requests.exceptions.ConnectionError:
		print("\nНет интернета!")
		status='not connected'
		pass
	else:
		status=req.json()['status']
	time.sleep(0.3)
	if status=='ok':
		combinations=req.json()['combinations']
		
		for i in range(0,20):
			try:
				cursor.execute("INSERT INTO table_"+str(circulation_loto)+" VALUES("+combinations[i]['number']+",'"+str(combinations[i]['numbers'])[1:-1]+"','"+time.strftime("%d/%m/%Y - %H:%M:%S",time.localtime(act_time))+"')")
				act_tickets_count+=1
			except:
				#print("\nНе удалось записать в базу данные билета №"+str(combinations[i]['number']))
				pass
			else:
				print("Добавлено билетов: "+str(act_tickets_count)+" - скорость парсинга: " + str(int((act_tickets_count)/(act_time-start_time)*60)) + " билетов в минуту" + "\r",end='')
				db_connection.commit()
	
	
if db_connection:
	print("Отключение от базы данных "+db_name+".db...",end='')
try:
	db_connection.close()
except:
	print("Не удалось!")
else:
	print("Успешно!")
print("\nЗавершено в " +time.strftime("%d/%m/%Y - %H:%M:%S",time.localtime(time.time())) + "!")
#input("Нажмите любую клавишу для выхода...")
