def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            print(f"Removed: {tasks[index]}")
            tasks.pop(index)
            save_tasks(tasks)
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add Task\n2. Remove Task\n3. View Tasks\n4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            remove_task(tasks)
        elif choice == '3':
            view_tasks(tasks)
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
