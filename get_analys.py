
from sqlite3 import *
db_name="tickets"
db_ext="db"
stat={}
anal=str(input("Введите индетификатор анализа: "))
circulation_loto=input("Введите номер тиража: ")

db_connection=connect(db_name+'.'+db_ext)

cursor=db_connection.cursor()
for number in range(1,91):
	cursor.execute("SELECT COUNT(numbers) FROM table_"+str(circulation_loto)+" WHERE numbers LIKE '"+str(number)+",%' OR numbers LIKE '% "+str(number)+",%' OR numbers LIKE '%, "+str(number)+"'")
	
	stat[number]=int(cursor.fetchall()[0][0])
print(stat)

str_anal="CREATE TABLE IF NOT EXISTS analys_"+str(circulation_loto)+ "(anal TEXT PRIMARY KEY NOT NULL, "
for i in range(1,len(stat)+1):
	if i!=len(stat):
		str_anal+="n_"+str(i)+" INTEGER NOT NULL, "
	else:
		str_anal+="n_"+str(i)+" INTEGER NOT NULL)"
print(str_anal)
cursor.execute(str_anal)

str_anal_add="INSERT INTO analys_"+str(circulation_loto)+" VALUES('"+anal+"', "
for key in stat:
	if key!=90:
		str_anal_add+=str(stat[key])+", "
	else:
		str_anal_add+=str(stat[key])+")"

print(str_anal_add)
cursor.execute(str_anal_add)
db_connection.commit()
#print(cursor.fetchall()[0][0])



db_connection.close()
