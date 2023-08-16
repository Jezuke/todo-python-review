"""
Create a CLI TODO app with the following functions:

* Add task
* Delete task
* Edit task

Task:
 - complete -> bool
 - value -> string
 - id -> int
"""
from os import system

class Task:
    def __init__(self, value, id) -> None:
        self._complete = False
        self._value = value
        self._id = id

    def set_task(self, value):
        self._value = value
    
    def get_task(self):
        return self._value

    def set_complete(self):
        self._complete = True

    def set_incomplete(self):
        self._complete = False

def switch(choice) -> int:
    if choice == 1:
        print("ADD ADD_TASK FN")
    elif choice == 2:
        print("ADD LIST_TASKS FN")
    elif choice == 3:
        print("ADD DELETE_TASKS FN")
    elif choice == 4:
        print_options()
    elif choice == 5:
        print("Quitting...")
    else:
        print("Invalid choice... Try again.")
    return choice

def clear():
    system("clear")

def print_options():
    main_options = """\n**** OPTIONS ****
1) add task
2) list tasks
3) delete task
4) help
5) quit
*****************
    """
    print(main_options)

def main():
    tasks = {}

    print("----- TODOME -----")   
    print_options()
    choice = ""

    while choice != 5:
        try:
            option = int(input("Choose an option: "))
            choice = switch(option)
        except:
            print("Invalid choice... Must be a number. Try again.")
    
    clear()

if __name__ == "__main__":
    main()

