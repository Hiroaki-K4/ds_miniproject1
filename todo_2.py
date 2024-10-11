import re
def print_default_message():
    print("Advanced To-Do List Application")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Suggest Tasks")
    print("5. Exit")


def add_task(tasks):
    Name = input("Enter your task:")
    while True:
        Priority = input("Enter the priority (high, medium, low):")
        list = ["high", "medium", "low"]
        if Priority.lower() in list :
            break
        else :
            print("Please enter high, medium or low!")
            continue

    while True:
        Deadline = input("Enter the deadline (YYYY-MM-DD):")
        pattern_Deadline = r'^\d{4}-\d{2}-\d{2}$'
        if re.match(pattern_Deadline, Deadline):
            break
        else:
            print("Please enter the right formate YYYY-MM-DD!")
            continue

    tasks_dic ={}
    tasks_dic["Name"] = Name
    tasks_dic["Priority"] = Priority
    tasks_dic["Deadline"] = Deadline
    tasks.append(tasks_dic)
    print(f"'{Name}' with priority {Priority} and deadline {Deadline} has been added to the list.")
    return tasks


def remove_task(tasks):
    task_to_remove = input("Enter the task to remove:")
    for task in tasks:
        if tasks["Name"] == task_to_remove:
            tasks.remove(task)
            print(task_to_remove, "has been removed from the priority list")
            return tasks
        else:
            print("There no", task_to_remove, "task")
            return tasks


def view_tasks(tasks):
    print("To-Do List:")
    for index, task in enumerate(tasks):
        print(
            "{0}. {1} - {2} - {3}".format(
                index + 1, task["Name"], task["Priority"], task["Deadline"]
            )
        )


def suggest_tasks(tasks):
    # Please write some code
    print("aaa")


def main():
    tasks = []
    while True:
        print_default_message()
        try:
            user_input = int(input("Enter your choice: "))
        except:
            print("Please enter a number between 1-4")
            print()
            continue
        if user_input == 1:
            tasks = add_task(tasks)
        elif user_input == 2:
            tasks = remove_task(tasks)
        elif user_input == 3:
            view_tasks(tasks)
        elif user_input == 4:
            suggest_tasks(tasks)
        elif user_input == 5:
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Please enter a number between 1-4")
        print()


if __name__ == '__main__':
    main()
