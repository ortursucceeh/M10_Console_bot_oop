import functools
from entities import AdressBook, Record
from constants import HELLO_WORDS, EXIT_WORDS


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
def add_contact(name, number=None):
    """Func which adds new contact in contacts"""
    if number is None:
        raise IndexError
    elif name in contacts:
        return contacts[name].add_phone(number)

    record = Record(name, number)
    contacts.add_record(record)
    return f"Contact with name '{name}' and phone '{number}' was added."


@input_error
def find_contact(name, number=None):
    """Func which shows name's number"""
    return f"{name} -: {', '.join([phone.value for phone in contacts[name].phones])}"


@input_error
def change_contact(name, old_number=None, new_number=None):
    """Func which changes some contact"""
    if name in contacts:
        contacts[name].change_phone(old_number, new_number)
        return f"Contact's number with name '{name}' was changed to '{new_number}'."

    raise ValueError("Unknown name.")


@input_error
def show_all_contacts(*args):
    """Func which shows all contacts"""
    if contacts:
        return '\n'.join([f"{key} -:  {', '.join([phone.value for phone in value.phones])}" for key, value in contacts.items()])

    return "You don't have any contacts."


@input_error
def remove_contact(name, number=None):
    """Func which deletes contact"""
    del contacts[name]
    return f"Contact with name '{name}' was removed."


@input_error
def show_all_commands(name=None, number=None):
    """Func which shows all commands"""
    return " # ".join(handler.keys())


def remove_phone(name, phone=None):
    """Func which delete phone in record"""
    return contacts[name].remove_phone(phone)


def change_phone(name, old_phone, new_phone):
    """Func which change phone in record"""
    return contacts[name].change_phone(old_phone, new_phone)


handler = {
    "hello": lambda: "Hello! How can I help you?",
    "add": add_contact,
    "change": change_contact,
    "phone": find_contact,
    "show": show_all_contacts,
    "remove": remove_contact,
    "commands": show_all_commands,
    "remove_phone": remove_phone,
    "change_phone": change_phone
}


def main():
    while True:

        command = input("Enter command: ").lower().strip().split()

        if command[0] in EXIT_WORDS:
            print("See ya!")
            exit()
        elif command[0] in HELLO_WORDS:
            print(handler["hello"])

        elif command[0] in handler:
            print(handler[command[0]](*command[1:]))
        else:
            print("Incorrect command.\n(To see all commands enter 'commands')")


if __name__ == "__main__":
    contacts = AdressBook()
    main()
