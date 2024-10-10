def print_default_message():
    print("To-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")


def add_task(tasks):
    new_task = input("Enter your task:")
    tasks.append(new_task)
    print(f"'{new_task}' has been added to the list.")
    return tasks

def remove_task():
    print("bbb")


def view_tasks(tasks):
    print("To-Do List:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}.{task}")


def main():
    tasks = []
    while True:
        print_default_message()
        user_input = int(input("Enter your choice: "))
        if user_input == 1:
            tasks = add_task(tasks)
        elif user_input == 2:
            tasks = remove_task()
        elif user_input == 3:
            view_tasks(tasks)
        elif user_input == 4:
            print("Exiting the application. Goodbye!")
            break


if __name__ == '__main__':
    main()
