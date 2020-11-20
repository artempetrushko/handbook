from Record import Record


class Handbook:

    def __init__(self, name):
        self.name = name


    def add_record(self):
        print('Введите через пробел имя, фамилию, номер телефона, город и e-mail:', end='\n')
        newRecord = Record(input())
        if newRecord.is_valid():
            handbook = open(self.name + '.txt', 'r')
            records = handbook.read()
            handbook.close()
            if newRecord.get_record_in_one_row() in records:
                print('Такая запись уже существует.', end='\n')
                return
            if newRecord.email in records:
                print('Запись с таким e-mail уже существует.', end='\n')
                return
            handbook = open(self.name + '.txt', 'a')
            handbook.write(newRecord.get_record_in_one_row() + '\n')
            handbook.close()
            print('Запись добавлена.', end='\n')
        else:
            print('Неверный ввод. Повторите попытку.')


    def change_record(self):
        print('Введите e-mail изменяемой записи:', end='\n')
        email = input()
        handbook = open(self.name + '.txt', 'r')
        records = handbook.read()
        handbook.seek(0)
        if '@' not in email:
            print('Неверный ввод. Повторите попытку.', end='\n')
            return
        if email in records:
            print('Введите новое значение:', end='\n')
            changedRecord = Record(input())
            if changedRecord.is_valid():
                records = handbook.readlines()
                handbook.close()
                handbook = open(self.name + '.txt', 'w')
                for record in records:
                    if email in record:
                        handbook.write(changedRecord.get_record_in_one_row() + '\n')
                    else:
                        handbook.write(record + '\n')
                print('Значение изменено.', end='\n')
            else:
                print('Неверный ввод. Повторите попытку.', end='\n')
            return
        print('Такой записи не существует.', end='\n')


    def search_record(self):
        print('Введите один из параметров для поиска:', end='\n')
        searchingParam = input()
        foundRecordsCount = 0
        handbook = open(self.name + '.txt', 'r')
        records = handbook.readlines()
        for record in records:
            if searchingParam in record:
                print(record)
                foundRecordsCount += 1
        handbook.close()
        print('Найдено записей: ', foundRecordsCount, end='\n')


    def delete_record(self):
        print('Введите e-mail удаляемой записи:', end='\n')
        email = input()
        handbook = open(self.name + '.txt', 'r')
        records = handbook.readlines()
        handbook.close()
        handbook = open(self.name + '.txt', 'w')
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