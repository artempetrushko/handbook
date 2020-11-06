def main():
    print('Список действий:', end='\n')
    print('Создать справочник - нажмите 1', end='\n')
    print('Добавить запись - нажмите 2', end='\n')
    print('Изменить запись - нажмите 3', end='\n')
    print('Найти запись - нажмите 4', end='\n')
    print('Удалить запись - нажмите 5', end='\n')
    print('Завершить работу - нажмите 0', end='\n')
    while True:
        digit = int(input())
        if digit == 1:
            create()
        elif digit == 2:
            add_record()
        elif digit == 3:
            change_record()
        elif digit == 4:
            search_record()
        elif digit == 5:
            delete_record()
        elif digit == 0:
            break


def create():
    directory['k1'] = list()
    print('Справочник создан.', end='\n')


def add_record():
    global recordsCount
    print('Введите через пробел имя, фамилию, номер телефона, город и e-mail:', end='\n')
    record = input().split(' ')
    if is_correct_record(record):
        if record in directory.values():
            print('Такая запись уже существует.', end='\n')
            return
        for value in directory.values():
            if record[4] in value:
                print('Запись с таким e-mail уже существует.', end='\n')
                return
        recordsCount += 1
        newKey = 'k' + str(recordsCount)
        directory[newKey] = record
        print('Запись добавлена.', end='\n')
    else:
        print('Неверный ввод. Повторите попытку.')


def change_record():
    print('Введите e-mail изменяемой записи:', end='\n')
    email = input()
    for key in directory.keys():
        if email in directory[key]:
            print('Введите новое значение:', end='\n')
            changedRecord = input().split(' ')
            if is_correct_record(changedRecord):
                directory[key] = changedRecord
                print('Значение изменено.', end='\n')
            else:
                print('Неверный ввод. Повторите попытку.', end='\n')
            return
    print('Такой записи не существует.', end='\b')


def search_record():
    print('Введите один из параметров для поиска:', end='\n')
    foundRecordsCount = 0
    record = input()
    for value in directory.values():
        if record in value:
            print(" ".join(value), end='\n')
            foundRecordsCount += 1
    print('Найдено записей: ', foundRecordsCount, end='\n')


def delete_record():
    print('Введите e-mail удаляемой записи:', end='\n')
    email = input()
    isDeleted = False
    for key in directory.keys():
        if email in directory[key]:
            del directory[key]
            isDeleted = True
            break
    if isDeleted:
        print('Запись удалена', end='\n')
    else:
        print('Такой записи не существует.', end='\n')


def is_correct_record(record):
    isFieldsCountCorrect = len(record) == 5
    isFirstNameCorrect = all(map(str.isalpha, record[0])) and record[0][0].isupper()
    isLastNameCorrect = all(map(str.isalpha, record[1])) and record[1][0].isupper()
    isPhoneNumberCorrect = all(map(str.isdigit, record[2])) and record[2][0] == '8' and len(record[2]) == 11
    isCityCorrect = all(map(str.isalpha, record[3])) and record[3][0].isupper()
    isEmailCorrect = '@' in record[4]
    return isFieldsCountCorrect and isFirstNameCorrect and isLastNameCorrect and isPhoneNumberCorrect and isCityCorrect and isEmailCorrect


directory = {}
recordsCount = 0
main()
