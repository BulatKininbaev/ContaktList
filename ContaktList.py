import csv



""" печать меню """
def print_menu():
    print('Выберете пункт меню от 0 до 6:')
    print(
        f'0 - Печать меню\n1 - Вывести список\n2 - Добавить контакт\n3 - Изменить номер\n4 - Удалить контакт\n5 - Найти контакт\n6 - Выйтий и сохранить изменения')


""" запись в файл и выход """
def close_app(filename: str ):
    with open(filename, 'w', encoding='utf-8', newline='') as CloseFile:
        data = [['ID', 'FIO', 'PHONE', 'COMMENT']]
        for key in contact_lst.keys():
            data.append([key, contact_lst[key][0], contact_lst[key][1], contact_lst[key][2]])
        writer = csv.writer(CloseFile, delimiter=';')
        writer.writerows(data)


""" список контактов"""

def show_list():
    for key in contact_lst.keys():
        print(
            f'Контакт ID {key} [Фамилия {contact_lst[key][0]} - Телефон {contact_lst[key][1]} Описание - {contact_lst[key][2]}]  ')


"""добавляем контакт """
def add_contact():
    contact_str = input('Введите через запятую ФИО и Телефон и примечания (Пример - Петров,+79845687124,Друг)')
    new_id = next(sequence_id)
    contact_lst[str(new_id)] = contact_str.split(',')
    return new_id


""" удалить контакт """
def delete_contact(ID: str):
    if ID in contact_lst:
        FIO = contact_lst[ID]
        del contact_lst[ID]
        print(f'Контакт {FIO} удален')


""" изменить номер телефона """
def change_contact(ch_str: str):
    if ch_str[0] in contact_lst:
        fio = contact_lst[ch_str[0]]
        contact_lst[ch_str[0]][1] = ch_str[1]
        print(f'Контакт {fio} изменен')


""" найти контакт """
def find_contact(ffio: str):
    i = 0
    for fio, phone, comment in contact_lst.values():
        if fio.find(ffio) > -1:
            i += 1
            print(f'[Фамилия {fio} - Телефон {phone} - Описание {comment}]')
    if i == 0:
        print('Контактов не найдено')


""" переменная контактов в памяти для работы словарь """
contact_lst = {}
# Пусть к файлу с контактами
filename = 'ContaktList.csv'

""" Читаем файл контактов """
DiskFile = open(filename , 'r', encoding='utf-8')
reader = csv.DictReader(DiskFile, delimiter=';')
for row in reader:
    contact_lst[row['ID']] = [row['FIO'], row['PHONE'], row['COMMENT']]

""" закрываем дескриптор """
DiskFile.close()

""" закончили импорт контактов """
print(f'Колличество прочитанных контактов {len(contact_lst)}')

"""  создаем генератов ID + 1000 к максимальному коду """

lstID = list(contact_lst.keys())
max_id = max(map(lambda x: int(x), lstID))
sequence_id = (x for x in range(max_id + 1, max_id + 1000))

""" Выводим меню """
print_menu()
p_number = '0'

""" цикл ожидания ввода """
while p_number != '6':
    p_number = input('Укажите пункт меню?')

    match p_number:
        case '0':
            print_menu()
        case '1':
            show_list()
        case '2':
            add_contact()
        case '3':
            change_contact(
                input('Введите через запятую ID удаляемого контакта и новый номер телефона 25,+79852476365 ').split(','))
        case '4':
            delete_contact(input('Введите ID удаляемого контакта'))
        case '5':
            find_contact(input('Введите ФИО контакта'))
        case _:
            continue

2
else:
    close_app(filename)
    print('Контакты сохранены')


