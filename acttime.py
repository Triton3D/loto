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
	
def str_time():
	hour=time.localtime(time.time()).tm_hour
	minute=time.localtime(time.time()).tm_min
	second=time.localtime(time.time()).tm_sec

	if hour<10:
		str_hour='0'+str(hour)
	else:
		str_hour=str(hour)

	if minute<10:
		str_minute='0'+str(minute)
	else:
		str_minute=str(minute)

	if second<10:
		str_second='0'+str(second)
	else:
		str_second=str(second)
	
	return str_hour+':'+str_minute+':'+str_second

def str_date():
	year=time.localtime(time.time()).tm_year
	month=time.localtime(time.time()).tm_mon
	day=time.localtime(time.time()).tm_mday
	str_year=str(year)
	if month<10:
		str_month='0'+str(month)
	else:
		str_month=str(month)

	if day<10:
		str_day='0'+str(day)
	else:
		str_day=str(day)

	return str_day+'/'+str_month+'/'+str_year

def more_date_time(time):
	
	return
		

def test():
	while True:
		time.sleep(0.3)
		print(str_date()+"\r", end='')

