import json

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)

def show_tasks():
    tasks = load_tasks()
    for i, t in enumerate(tasks, 1):
        status = "✅" if t["done"] else "❌"
        print(f"{i}. {t['task']} - {status}")

def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)

def remove_task():
    tasks=load_tasks()
    show_tasks()
    try:
      task_no = int(input("Enter task number to remove: ")) 
      removed_task = tasks.pop(task_no - 1)
      save_tasks(tasks)
      print(f"Removed: {removed_task['task']}")
    except (ValueError, IndexError):
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\n TO-DO LIST MENU")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Exit")


        choice = input("Choose an option: ")
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            show_tasks()
            try:
                index = int(input("Enter task number to mark as done: ")) - 1
                mark_done(index)
            except ValueError:
                print("Invalid input.")
        elif choice == "4":
            remove_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
