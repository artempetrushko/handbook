class Record:

    def __init__(self, row):
        record = row.split(' ')
        self.fieldsCount = len(record)
        self.firstName = record[0]
        self.lastName = record[1]
        self.phoneNumber = record[2]
        self.city = record[3]
        self.email = record[4]


    def is_valid(self):
        if self.fieldsCount != 5:
            return False
        isFirstNameCorrect = all(map(str.isalpha, self.firstName)) and self.firstName[0].isupper()
        isLastNameCorrect = all(map(str.isalpha, self.lastName)) and self.lastName[0].isupper()
        isPhoneNumberCorrect = all(map(str.isdigit, self.phoneNumber)) and self.phoneNumber[0] == '8' and len(self.phoneNumber) == 11
        isCityCorrect = all(map(str.isalpha, self.city)) and self.city[0].isupper()
        isEmailCorrect = '@' in self.email
        return isFirstNameCorrect and isLastNameCorrect and isPhoneNumberCorrect and isCityCorrect and isEmailCorrect


    def get_record_in_one_row(self):
        return '{} {} {} {} {}'.format(self.firstName, self.lastName, self.phoneNumber, self.city, self.email)
