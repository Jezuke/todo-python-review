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
import uuid

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
class Task:
    def __init__(self, value, id) -> None:
        self._complete = False
        self._value = value
        self._id = id

    def set_task(self, value):
        self._value = value
    
    def get_task(self):
        return self._value

    def get_id(self):
        return self._id
    
    def set_complete(self):
        self._complete = True

    def set_incomplete(self):
        self._complete = False

def clear():
    system("clear")

# TODO fix bug. After add one task, performing a list task, then trying to add another task, error gets thrown
# Error: 'NoneType' object does not support item assignment
def create_task():
    task = input("Enter task: ")
    print(f"Creating task: \"{task}\"", task)
    task = Task(task, uuid.uuid1())
    return task

def list_tasks(tasks):
    for task in tasks:
        print("*", tasks[task].get_task())
    
def main():
    tasks = {}

    print("----- TODOME -----")   
    print_options()
    choice = ""

    while choice != 5:
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                task = create_task()
                tasks[task.get_id()] = task
            elif choice == 2:
                print("Tasks:")
                tasks = list_tasks(tasks)
            elif choice == 3:
                print("ADD DELETE_TASKS FN")
            elif choice == 4:
                print_options()
            elif choice == 5:
                print("Quitting...")
            else:
                print("Invalid choice... Try again.")
        except Exception as e:
            print(e)
            print("Invalid choice... Must be a number. Try again.")
    
    clear()

if __name__ == "__main__":
    main()

