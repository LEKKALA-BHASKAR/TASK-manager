import json

def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks, filename):
    with open(filename, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    for idx, task in enumerate(tasks):
        status = "Complete" if task['complete'] else "Incomplete"
        print(f"{idx + 1}. {task['description']} - {status}")

def add_task(tasks):
    description = input("Enter task description: ")
    tasks.append({"description": description, "complete": False})

def edit_task(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the number of the task to edit: ")) - 1
    if 0 <= task_num < len(tasks):
        new_description = input("Enter new task description: ")
        tasks[task_num]['description'] = new_description
    else:
        print("Invalid task number.")

def delete_task(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the number of the task to delete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks.pop(task_num)
    else:
        print("Invalid task number.")

def mark_task_complete(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the number of the task to mark as complete: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]['complete'] = True
    else:
        print("Invalid task number.")

def task_manager():
    filename = 'tasks.json'
    tasks = load_tasks(filename)

    while True:
        print("\nTask Manager")
        print("1. Display tasks")
        print("2. Add task")
        print("3. Edit task")
        print("4. Delete task")
        print("5. Mark task complete")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            edit_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            mark_task_complete(tasks)
        elif choice == '6':
            save_tasks(tasks, filename)
            break
        else:
            print("Invalid choice.")
task_manager()
