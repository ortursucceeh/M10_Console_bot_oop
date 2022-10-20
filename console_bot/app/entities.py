from collections import UserDict


class AdressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record


class Record:

    def __init__(self, name, phone=None):
        self.name = Name(name)
        if phone:
            self.phones = [Phone(phone)]
        else:
            self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        return f"New phone '{phone}' was added to contact '{self.name.value.capitalize()}'."

    def remove_phone(self, removed_phone):
        for phone in self.phones:
            if phone.value == removed_phone:
                self.phones.remove(phone)
                return f"Phone '{removed_phone}' was removed"

    def change_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                self.add_phone(new_phone)
                self.phones.remove(phone)
                return f"Phone '{old_phone}' was changed to '{new_phone}'"


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass
