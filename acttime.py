import time
import requests

url='http://www.vniiftri.ru/templates/vniif3/servertime.php'
data={}
#Добавляем текущее время в тело запроса
data['t']=int(time.time()*1000)

#print(data)

def ac_local_time(showtime=True,showdate=False):
	str_time=''
	str_date=''

	req=requests.get(url,data)
	diff_time=int(req.text.split(':')[0])
	#print('diff: ',diff_time)
	query_time=int(req.text.split(':')[1])
	#print('query: ',query_time)
	act_time=int(time.time()*1000)
	#print('act: ',act_time)
	real_time=2*act_time-query_time+diff_time
	#print('real: ',real_time)
	out_time=time.localtime(real_time/1000.)

	if out_time.tm_hour<10:
		hour='0'+str(out_time.tm_hour)
	else:
		hour=str(out_time.tm_hour)
	if out_time.tm_min<10:
		minute='0'+str(out_time.tm_min)
	else:
		minute=str(out_time.tm_min)
	if out_time.tm_sec<10:
		second='0'+str(out_time.tm_sec)
	else:
		second=str(out_time.tm_sec)
	if out_time.tm_mon<10:
		month='0'+str(out_time.tm_mon)
	else:
		month=str(out_time.tm_mon)
	if out_time.tm_mday<10:
		day='0'+str(out_time.tm_mday)
	else:
		day=str(out_time.tm_mday)
	
	if showtime:
		str_time=hour+':'+minute+':'+second+' '
	if showdate:
		str_date=day+'.'+month+'.'+str(out_time.tm_year)
	return(str_time+str_date)
	

