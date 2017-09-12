from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.http import Http404
from django.shortcuts import render

from .models import Ticket

import requests
import time

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


def index(request):
	list_tickets=Ticket.objects.all()
	length = len(list_tickets)
	context = {
		'list_tickets' : list_tickets,
		'length' : length,
		}
	return render(request,'gettickets/index.html',context)

def details(request,ticket_number):
	try:
		ticket=Ticket.objects.get(number=ticket_number)
	except Ticket.DoesNotExist:
		raise Http404("Билета не существует")
	return render(request, 'gettickets/details.html',{'ticket':ticket})

def test(request):
	
	act_tickets_count=0
	while act_tickets_count<int(request.POST['test']):
		try: 
			req=requests.post(url=ruloto_change_url,headers=ruloto_change_headers,data=ruloto_change_numbers)
		except requests.exceptions.ConnectionError:
			status='not connected'
			pass
		else:
			status=req.json()['status']
			time.sleep(0.5)
			if status=='ok':
				combinations=req.json()['combinations']
				for i in range(0,20):
					ticket=Ticket(number=combinations[i]['number'],content=combinations[i]['numbers'])
					ticket.save()
					act_tickets_count+=1
	return render(request,'gettickets/analys.html',{'ticket_count': act_tickets_count } )
	

