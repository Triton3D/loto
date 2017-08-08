from bs4 import BeautifulSoup
from random import randint
import sys
from selenium import webdriver
import time

pages_count = input("Введите количество страниц: ")
browser = webdriver.Firefox()  # Запускаем браузер
url = 'http://www.stoloto.ru/ruslotto/game?int=right'
print("Загрузка страницы...")
browser.get(url)  # Загружаем страницу с билетами
print("Страница успешно загружена!")
refresh_tickets = browser.find_element_by_css_selector(
    "ins.for_normal.with_icon.pseudo")  # Ищем кнопку "Обновить билеты"

for i in range(0, int(pages_count)):
    # Загружаем html-код в память
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # Ищем теги с номерами билетов
    tckid_tags = soup.find_all('span', {'class': 'ticket_id'})

    for j in tckid_tags:
        x = str(j).replace('<span class="ticket_id">', '')
        x = x.replace('</span>', '')
        # Создаем файл с именем - номером билета
        ticket_file = open('.\\tickets\\' + str(x) + '.csv', 'w')
        # Ищем все номера бочонков в билетах
        tickets_content = soup.find_all('tr', {'class': 'numbers'}, 'td')
        numbers = []
        td = 0
        for k in tickets_content:
            # Распределяем номера бочонков построчно
            if td >= tckid_tags.index(j) * 6 and td < (tckid_tags.index(j) * 6 + 6):
                x = str(k).replace('<tr class="numbers"><td>', '')
                x = x.replace('</td></tr>', '')
                x = x.split('</td><td>')
                numbers.append(x)
            td += 1
        for a in range(0, len(numbers)):
            for b in range(0, 9):
                if str(numbers[a][b]) != '':
                    ticket_file.writelines(
                        str(numbers[a][b]).replace("'", "") + ",")  # Записываем номера бочоков билета в соответствующий билету файл
        ticket_file.close()
        sys.stderr.write("Обработано " + str(i) + " из " + str(pages_count) +
                         " страниц. Сохранено " + str(i * 20 + tckid_tags.index(j) + 1) + " билетов.\r")

    if i <= int(pages_count):
        refresh_tickets.click()  # Обновлям билеты на странице
        # Случайный период между обновлениями билетов для исключения бана со стороны сервера лото
        time.sleep(randint(3, 10))

sys.stderr.write("Обработано " + str(i + 1) + " из " + str(pages_count) +
                 " страниц. Сохранено " + str(i * 20 + tckid_tags.index(j) + 1) + " билетов.\r")
browser.quit()
print("\nГотово!")
