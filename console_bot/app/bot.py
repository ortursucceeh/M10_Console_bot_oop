import functools
from collections import UserDict


class AdressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record


class Record:

    def __init__(self, name=None, phone=None):
        self.name = Name(name)
        if phone:
            self.phones = [Phone(phone)]
        else:
            self.phones = []

    def add_phone(self, record, new_phone):
        record.phones = [record.phones] + [new_phone]
        return f"Phone was added to record"

    def remove_phone(self, name, removed_phone):
        # list of str phones from record.phones
        names_phones = [i.value for i in contacts[name].phones]

        if removed_phone in names_phones:
            for phone in contacts[name].phones:
                if removed_phone == phone.value:
                    contacts[name].phones.remove(phone)
                    return f"Phone was removed from record"
        else:
            raise KeyError("Removed phone isn't in phones")

    def edit_record(self, record, new_record):
        record.name.value = new_record.name.value
        record.phones = new_record.phones
        return f"Record was changed"


class Field:
    pass


class Name(Field):

    def __init__(self, value):
        self.value = value


class Phone(Field):

    def __init__(self, value=None):
        self.value = value


EXIT_WORDS = ["exit", "close", "good bye", "end"]

contacts = AdressBook()


def input_error(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Wrong name."
        except TypeError:
            return "Wrong command format."
        except IndexError:
            return "Wrong input data. Enter name and phone."
        except ValueError as e:
            return e.args[0]
        except Exception as e:
            return e.args
    return wrapper


@input_error
def add_contact(record=None):
    """Func which adds new contact in contacts"""
    if record.phones is None:
        raise IndexError
    elif record.name.value in contacts:
        raise ValueError(f"{record.name.value} is already in contacts")
    contacts.add_record(record)
    return f"Contact with name {record.name.value} and phones {[i.value for i in record.phones]} was added."


@input_error
def find_contact(record=None):
    """Func which shows name's number"""
    return contacts[record.name.value]


@input_error
def change_contact(record=None, new_number=None):
    """Func which changes some contact"""
    if record.name.value in contacts:
        contacts[record.name.value] = new_number
        return f"Contact's number with name {record.name.value} was changed to {new_number}."
    else:
        raise ValueError("Unknown name.")


@input_error
def show_all_contacts(*args, **kwargs):
    """Func which shows all contacts"""
    if contacts:
        return '\n'.join([f"{key} ---:  {[i.value for i in value.phones]}" for key, value in contacts.items()])
    else:
        return "You don't have any contacts."


@input_error
def remove_contact(record=None):
    """Func which deletes contact"""
    del contacts[record.name.value]
    return f"Contact with name {record.name.value} was removed."


@input_error
def show_all_commands(*args, **kwargs):
    """Func which shows all commands"""
    return " # ".join(handler.keys())


@input_error
def add_record_phone(record=None, new_phone=None):
    record.add_phone(record, new_phone)


@input_error
def remove_record_phone(record, removed_phone):
    record.remove_phone(record, removed_phone)


@input_error
def edit_record(record, new_record):
    record.edit_record(record, new_record)


handler = {
    "hello": lambda: "Hello! How can I help you?",
    "add": add_contact,
    "change": change_contact,
    "phone": find_contact,
    "show": show_all_contacts,
    "remove": remove_contact,
    "commands": show_all_commands,
    "add_record_phone": add_record_phone,
    "remove_record_phone": remove_record_phone,
    "edit_record": edit_record
}


def main():
    while True:

        in_command = input(
            "Enter command and record: ").lower().strip().split()
        command = in_command[0]
        record = Record(*in_command[1:])

        if command in EXIT_WORDS:
            print("See ya!")
            exit()

        elif command in handler:
            print(handler[command](record))
        else:
            print("Incorrect command. (To see all commands enter 'commands')")


if __name__ == "__main__":
    main()
