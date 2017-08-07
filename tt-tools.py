# Функция для проверки интернет соединения
# Самодуров Т. П. 08.2017


def check_connection(url='https://ya.ru'):

    try: 
        import urllib
    except ImportError:
        print("Ошибка! Не удалось импортировать модуль 'urllib'!")
        
    try:
        connection_status = urllib.urlopen(url)
    except IOError:
        connection_status = False
    finally:
        return connection_status
