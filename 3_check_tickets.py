#
#
import os

try:
    numbers_list = str(open('numbers.txt', 'r').readline()).split(',')
    # print(numbers_list)
except:
    print('Файл numbers.txt не найден!')
    numbers_list = str(
        input('Введите список номеров бочонков в порядке их выпадения:')).split(',')
files = os.listdir('.\\tickets\\')
for ticket_file in files:
    cur_ticket_file = open('.\\tickets\\' + ticket_file, 'r')
    tmp_numbers_list = str(cur_ticket_file.readline()).split(',')
    coeq = 0
    for number in tmp_numbers_list:
        if tmp_numbers_list.index(number) % 5 == 0:
            coeq = 0
        if numbers_list.count(number):
            coeq += 1
        if coeq == 5:
            print("Билет №" +
                  ticket_file[:-len(".csv")] + " выиграл в первом туре!")
            break
    if coeq < 5:
        print("Билет №" + ticket_file[:-len(".csv")
                                      ] + " не выиграл в первом туре")
print("Завершено")
# print(tmp_numbers_list)
# class Ticket:
#     '''Билет'''

#     def __init__(self, number):
#         self.number = number
#         self.content = [[], [], [], [], [], []]

#     def fill_from_csv(self, tfile):
#         try:
#             ticket_file = open(tfile, 'r')
#         except FileNotFoundError:
#             print("Файл " + tfile + " не найден!")
#             return False
#         for i in range(0, 6):
#             for j in range(1, 6):
#                 self.content[i][j] = int(
#                     str(ticket_file.readline().split(',')[i * 5 + j]))
#         ticket_file.close()
#         return True


# dir = '.\\tickets\\'
# files = os.listdir(dir)

# print(str(len(files)) + " билетов найдено в папке")

# numbers_fact = input(
#     "Введите номера бочонков в порядке их выпадения, через запятую:").split(',')

# # print(type(numbers_str.split(',')))

# for i in range(0, len(files)):
#     curTicket = Ticket()
#     curTicket.fill_from_csv(dir + files[i])
#     print(curTicket.content)
