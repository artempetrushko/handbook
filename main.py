import os.path


def main():
    result = 0
    while True:
        result = choose_action()
        if result == -1:
            break


def choose_action():
    print('Список действий:', end='\n')
    print('Создать справочник - нажмите 1', end='\n')
    print('Сменить справочник - нажмите 2', end='\n')
    print('Добавить запись - нажмите 3', end='\n')
    print('Изменить запись - нажмите 4', end='\n')
    print('Найти запись - нажмите 5', end='\n')
    print('Удалить запись - нажмите 6', end='\n')
    print('Завершить работу - нажмите 0', end='\n')
    digit = int(input())
    if digit == 1:
        create_handbook()
    elif digit == 2:
        change_handbook()
    elif digit == 3:
        add_record()
    elif digit == 4:
        change_record()
    elif digit == 5:
        search_record()
    elif digit == 6:
        delete_record()
    elif digit == 0:
        return -1
    return 1


def create_handbook():
    global currentHandbook
    handbookName = input("Введите имя справочника: ")
    if os.path.exists(os.path.abspath(handbookName + '.txt')):
        print('Справочник с таким именем уже существует.', end='\n')
        return
    currentHandbook = handbookName
    handbook = open(handbookName + ".txt", "a")
    handbook.close()
    print('Справочник создан.', end='\n')


def change_handbook():
    global currentHandbook
    handbookName = input("Введите имя нужного справочника: ")
    if os.path.exists(os.path.abspath(handbookName + '.txt')):
        currentHandbook = handbookName
        print('Текущий справочник изменён.', end='\n')
    else:
        print('Справочника с таким именем не существует. Создать его? (y/n)', end='\n')
        answer = input()
        if answer == 'y':
            currentHandbook = handbookName
            handbook = open(handbookName + ".txt", "a")
            handbook.close()
            print('Справочник создан.', end='\n')
        if answer == 'n':
            return


def add_record():
    global currentHandbook
    print('Введите через пробел имя, фамилию, номер телефона, город и e-mail:', end='\n')
    record = input()
    if is_correct_record(record):
        handbook = open(currentHandbook + '.txt', 'r')
        records = handbook.read()
        handbook.close()
        if record in records:
            print('Такая запись уже существует.', end='\n')
            return
        if record.split(' ')[4] in records:
            print('Запись с таким e-mail уже существует.', end='\n')
            return
        handbook = open(currentHandbook + '.txt', 'a')
        handbook.write(record + '\n')
        handbook.close()
        print('Запись добавлена.', end='\n')
    else:
        print('Неверный ввод. Повторите попытку.')


def change_record():
    print('Введите e-mail изменяемой записи:', end='\n')
    email = input()
    handbook = open(currentHandbook + '.txt', 'r')
    records = handbook.read()
    handbook.seek(0)
    if email in records:
        print('Введите новое значение:', end='\n')
        changedRecord = input()
        if is_correct_record(changedRecord):
            records = handbook.readlines()
            handbook.close()
            handbook = open(currentHandbook + '.txt', 'w')
            for record in records:
                if email in record:
                    handbook.write(changedRecord + '\n')
                else:
                    handbook.write(record + '\n')
            print('Значение изменено.', end='\n')
        else:
            print('Неверный ввод. Повторите попытку.', end='\n')
        return
    print('Такой записи не существует.', end='\b')


def search_record():
    global currentHandbook
    print('Введите один из параметров для поиска:', end='\n')
    searchingParam = input()
    foundRecordsCount = 0
    handbook = open(currentHandbook + '.txt', 'r')
    records = handbook.readlines()
    for record in records:
        if searchingParam in record:
            print(record)
            foundRecordsCount += 1
    handbook.close()
    print('Найдено записей: ', foundRecordsCount, end='\n')


def delete_record():
    global currentHandbook
    print('Введите e-mail удаляемой записи:', end='\n')
    email = input()
    handbook = open(currentHandbook + '.txt', 'r')
    records = handbook.readlines()
    handbook.close()
    handbook = open(currentHandbook + '.txt', 'w')
    isDeleted = False
    for record in records:
        if email not in record:
            handbook.write(record)
        else:
            isDeleted = True
    handbook.close()
    if isDeleted:
        print('Запись удалена.', end='\n')
    else:
        print('Записи с таким e-mail не существует.', end='\n')


def is_correct_record(record):
    fields = record.split(' ')
    if len(fields) != 5:
        return False
    isFirstNameCorrect = all(map(str.isalpha, fields[0])) and fields[0][0].isupper()
    isLastNameCorrect = all(map(str.isalpha, fields[1])) and fields[1][0].isupper()
    isPhoneNumberCorrect = all(map(str.isdigit, fields[2])) and fields[2][0] == '8' and len(fields[2]) == 11
    isCityCorrect = all(map(str.isalpha, fields[3])) and fields[3][0].isupper()
    isEmailCorrect = '@' in fields[4]
    return isFirstNameCorrect and isLastNameCorrect and isPhoneNumberCorrect and isCityCorrect and isEmailCorrect


currentHandbook = ''
main()
