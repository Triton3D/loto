#
#
import os


class Ticket:
    '''Билет'''

    def __init__(self):
        self.number = 99999999
        self.content = [[], [], [], [], [], []]

    def fill_from_csv(self, tfile):
        try:
            ticket_file = open(tfile, 'r')
        except FileNotFoundError:
            print("Файл " + tfile + " не найден!")
            return False
        for i in range(0, 6):
            for j in range(1, 6):
                self.content[i][j] = int(
                    str(ticket_file.readline().split(',')[i * 5 + j]))
        ticket_file.close()
        return True


dir = '.\\tickets\\'
files = os.listdir(dir)

print(str(len(files)) + " билетов найдено в папке")

numbers_fact = input(
    "Введите номера бочонков в порядке их выпадения, через запятую:").split(',')

# print(type(numbers_str.split(',')))

for i in range(0, len(files)):
    curTicket = Ticket()
    curTicket.fill_from_csv(dir + files[i])
    print(curTicket.content)
