# Модуль сбора статистики присутствия чисел в билетах Русское Лото
import os
import time
import sys

dir=".\\tickets\\"
files=os.listdir(dir)

numbers_list=[i for i in range(1,91)]
number_stats={numbers_list[i]:0 for i in range(0,90) }
print("Найдено "+str(len(files))+" файлов билетов.\nНомер первого билета: " + \
     files[0][:-len('.csv')]+"\nНомер последнего билета: " + files[len(files)-1][:-len('.csv')]+ "\n")
  

for curfile in files:
    try:
        file=open(dir+curfile,'r')
    except FileNotFoundError:
        print("Файл " + curfile+" был удален или перемещен в процессе работы программы")
        continue
    tickets_contents_numbers=file.readline()[:-1].split(',')
    for i in range(0,len(tickets_contents_numbers)):
        number_stats[int(tickets_contents_numbers[i])]+=1 
    file.close()
    time.sleep(0.05)
    sys.stderr.write("Сбор статистики: " + str(int(files.index(curfile)*100/len(files))+1)+'%\r')
print("\nГотово!")
time.sleep(1)
try:
    stats_csv=open('stats.csv','w')
except PermissionError:
    print("\nФайл открыт в другой программе! Закройте пожалуйста и повторите попытку.")
stats_csv.writelines("Количество билетов ," + str(len(files))+ \
                    "\n\nНомер бочонка,Количество\n")
                 
for i in range(1,91):
    stats_csv.writelines(str(i)+','+str(number_stats[i])+'\n')
stats_csv.close()
print("\nРезультаты статистических данных успешно записаны в файл stats.csv ")