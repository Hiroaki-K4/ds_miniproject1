def print_default_message():
    print("To-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")


def add_task():
    print("aaa")

def remove_task(tasks):
    task_to_remove = input("Enter the task to remove:")
    if task_to_remove in tasks:
        tasks.remove(task_to_remove)
        print(task_to_remove, "has been removed from the list")
        return tasks
    else:
        print("There no", task_to_remove, "task")
        return tasks


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
            tasks = add_task()
        elif user_input == 2:
            tasks = remove_task(tasks)
        elif user_input == 3:
            view_tasks(tasks)
        elif user_input == 4:
            print("Exiting the application. Goodbye!")
            break


if __name__ == '__main__':
    main()
