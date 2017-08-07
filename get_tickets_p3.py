from bs4 import BeautifulSoup
import sys
from selenium import webdriver
import time

nt=input("Ведите количество страниц: ")
browser = webdriver.Firefox()
url='http://www.stoloto.ru/ruslotto/game?int=right'
browser.get(url)
ticket = browser.find_element_by_css_selector("ins.for_normal.with_icon.pseudo")
for i in range(1,int(nt)+1):
   html_file=open(str(i)+'.html','w')
   html_file.write(str(browser.page_source.encode('utf-8')))
   print("Страница сохранена как " + str(i) +".html!")
   if i<=int(nt):
      ticket.click()
   html_file.close()
   time.sleep(5)
print("Сохранение прошло успешно!")

for i in range(1,int(nt)+1):
   f=open(str(i)+'.html','r')
   s=f.read()
   soup = BeautifulSoup(s,'html.parser')
   tckid=soup.find_all('span',{'class':'ticket_id'})
   ticket=[]
   t=0
   for i in tckid:
      
      x=str(i).replace('<span class="ticket_id">','')
      x=x.replace('</span>','')
      ticket.append(int(x))
      ticket_file=open(str(x)+'.csv','w')
##    ticket_file.close()

      ss=soup.find_all('tr',{'class':'numbers'},'td')
      #ss=str(ss)

      numbers=[]
      #print ss
      td=0
      for j in ss:
              if td>=t*6 and td<(t*6+6):
                 x=str(j).replace('<tr class="numbers"><td>','')
                 x=x.replace('</td></tr>','')
                 x=x.split('</td><td>')
                 numbers.append(x)
              td+=1
      for j in range(0,len(numbers)):
         for z in range(0,9):
             if str(numbers[j][z])!='':
                ticket_file.writelines(str(numbers[j][z]).replace("'","")+",")
      ticket_file.close()
      t+=1
##         
##                          
##      my_dict={}
##      keys=[]
##      for i in range(1,91):
##          keys.append(i)
##          my_dict[keys[i-1]]=0
##      zu=[]
##      for item in z:
##              for meti in item:
##                      if meti!='': zu.append(meti)
##      for j in zu:
##          j=int(j)
##          my_dict[j]=my_dict.get(j)+1
##      #print my_dict
##      for tt in my_dict:
##          print my_dict[tt]
