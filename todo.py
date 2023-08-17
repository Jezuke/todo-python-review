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

def clear():
    system("clear")

def create_task():
    task = input("Enter task: ")
    print(f"Creating task: \"{task}\"")
    return task

def list_tasks(tasks):
    for task in tasks:
        print("*", task)
    
def main():
    tasks = []

    print("----- TODOME -----")   
    print_options()
    choice = ""

    while choice != 5:
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                task = create_task()
                # print("Curr tasks:", tasks)
                tasks.append(task)
            elif choice == 2:
                print("Tasks:")
                list_tasks(tasks)
            elif choice == 3:
                print("ADD DELETE_TASKS FN")
            elif choice == 4:
                print_options()
            elif choice == 5:
                print("Quitting...")
            else:
                print("Invalid choice... Try again.")
        except Exception as e:
            print("Invalid choice... Must be a number. Try again.")
        print("\n")
    
    clear()

if __name__ == "__main__":
    main()

