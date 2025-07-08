import csv



# печать меню
def PrintMenu():
    print('Выберете пункт меню от 0 до 6:')
    print(
        f'0 - Печать меню\n1 - Вывести список\n2 - Добавить контакт\n3 - Изменить номер\n4 - Удалить контакт\n5 - Найти контакт\n6 - Выйтий и сохранить изменения')


# запись в файл и выход
def CloseApp(FileName):
    with open(FileName, 'w', encoding='utf-8', newline='') as CloseFile:
        data = [['ID', 'FIO', 'PHONE', 'COMMENT']]
        for key in contact_lst.keys():
            data.append([key, contact_lst[key][0], contact_lst[key][1], contact_lst[key][2]])
        writer = csv.writer(CloseFile, delimiter=';')
        writer.writerows(data)

    # список контактов
1

def ShowList():
    for key in contact_lst.keys():
        print(
            f'Контакт ID {key} [Фамилия {contact_lst[key][0]} - Телефон {contact_lst[key][1]} Описание - {contact_lst[key][2]}]  ')


# добавляем контакт
def AddContact():
    contact_str = input('Введите через запятую ФИО и Телефон и примечания (Пример - Петров,+79845687124,Друг)')
    newid = next(squenceID)
    contact_lst[str(newid)] = contact_str.split(',')
    return newid


# удалить контакт
def DeleteContact(ID):
    if ID in contact_lst:
        FIO = contact_lst[ID]
        del contact_lst[ID]
        print(f'Контакт {FIO} удален')


# изменить номер телефона
def ChangeContakt(chstr):
    if chstr[0] in contact_lst:
        FIO = contact_lst[chstr[0]]
        contact_lst[chstr[0]][1] = chstr[1]
        print(f'Контакт {FIO} изменен')


# найти контакт
def FindContact(FFIO):
    i = 0
    for FIO, PNONE, Comment in contact_lst.values():
        if FIO.find(FFIO) > -1:
            i += 1
            print(f'[Фамилия {FIO} - Телефон {PNONE} - Описание {Comment}]')
    if i == 0:
        print('Контактов не найдено')


# переменная контактов в памяти для работы словарь
contact_lst = {}
# Пусть к файлу с контактами
FileName = 'ContaktList.csv'

# Читаем файл контактов
DiskFile = open(FileName, 'r', encoding='utf-8')
reader = csv.DictReader(DiskFile, delimiter=';')
for row in reader:
    contact_lst[row['ID']] = [row['FIO'], row['PHONE'], row['COMMENT']]

# закрываем дескриптор
DiskFile.close()

# закончили импорт контактов
print(f'Колличество прочитанных контактов {len(contact_lst)}')

# создаем генератов ID + 1000 к максимальному коду
lstID = list(contact_lst.keys())
maxid = max(map(lambda x: int(x), lstID))
squenceID = (x for x in range(maxid + 1, maxid + 1000))

# Выводим меню
PrintMenu()
p_number = '0'

# цикл ожидания ввода
while p_number != '6':
    p_number = input('Укажите пункт меню?')

    match p_number:
        case '0':
            PrintMenu()
        case '1':
            ShowList()
        case '2':
            AddContact()
        case '3':
            ChangeContakt(
                input('Введите через запятую ID удаляемого контакта и новый номер телефона 25,+79852476365 ').split(
                    ','))
        case '4':
            DeleteContact(input('Введите ID удаляемого контакта'))
        case '5':
            FindContact(input('Введите ФИО контакта'))
        case _:
            continue


else:
    CloseApp(FileName)
    print('Контакты сохранены')


