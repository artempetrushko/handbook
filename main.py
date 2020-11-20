import os.path
from Handbook import Handbook


def main():
    result = 0
    while True:
        result = choose_action()
        if result == -1:
            break


def choose_action():
    print('Список действий:', end='\n')
    print('Создать справочник - нажмите 1', end='\n')
    print('Выбрать справочник - нажмите 2', end='\n')
    print('Показать имеющиеся справочники - нажмите 3', end='\n')
    print('Добавить запись - нажмите 4', end='\n')
    print('Изменить запись - нажмите 5', end='\n')
    print('Найти запись - нажмите 6', end='\n')
    print('Удалить запись - нажмите 7', end='\n')
    print('Завершить работу - нажмите 0', end='\n')
    digit = int(input())
    if digit == 1:
        create_handbook()
    elif digit == 2:
        change_handbook()
    elif digit == 3:
        show_handbooks()
    elif digit == 4:
        currentHandbook.add_record()
    elif digit == 5:
        currentHandbook.change_record()
    elif digit == 6:
        currentHandbook.search_record()
    elif digit == 7:
        currentHandbook.delete_record()
    elif digit == 0:
        return -1
    return 1


def create_handbook():
    global currentHandbook
    handbookName = input("Введите имя справочника: ")
    if os.path.exists(os.path.abspath(handbookName + '.txt')):
        print('Справочник с таким именем уже существует.', end='\n')
        return
    currentHandbook = Handbook(handbookName)
    handBooks[handbookName] = currentHandbook
    handbook = open(handbookName + ".txt", "a")
    handbook.close()
    print('Справочник создан.', end='\n')


def change_handbook():
    global currentHandbook
    handbookName = input("Введите имя нужного справочника: ")
    if os.path.exists(os.path.abspath(handbookName + '.txt')):
        currentHandbook = handBooks[handbookName]
        print('Текущий справочник изменён.', end='\n')
    else:
        print('Справочника с таким именем не существует. Создать его? (y/n)', end='\n')
        answer = input()
        if answer == 'y':
            currentHandbook = Handbook(handbookName)
            handBooks[handbookName] = currentHandbook
            handbook = open(handbookName + ".txt", "a")
            handbook.close()
            print('Справочник создан.', end='\n')
        if answer == 'n':
            return


def show_handbooks():
    for key in handBooks.keys():
        print(key, end='\n')


handBooks = dict()
currentHandbook = Handbook('')
handBooks[''] = currentHandbook
for file in os.listdir(os.getcwd()):
    if file.endswith('.txt'):
        handBooks[file[:-4]] = Handbook(file[:-4])
main()
