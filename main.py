def print_default_message():
    print("To-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")


def add_task():
    print("aaa")

def remove_task():
    print("bbb")


def view_tasks():
    print("ccc")


def main():
    tasks = []
    while True:
        print_default_message()
        user_input = input("Enter your choice: ")
        if user_input == 1:
            tasks = add_task()  
        elif user_input == 2:
            tasks = remove_task()
        elif user_input == 3:
            view_tasks()
        elif user_input == 4:
            break


if __name__ == '__main__':
    main()
