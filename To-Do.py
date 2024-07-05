import os

# File to save tasks
TASKS_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for line in file:
                tasks.append(line.strip())
    return tasks

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append(task)
    print(f'Task "{task}" added.')

def delete_task(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the number of the task to delete: "))
    if 1 <= task_num <= len(tasks):
        task = tasks.pop(task_num - 1)
        print(f'Task "{task}" deleted.')
    else:
        print("Invalid task number.")

def mark_task_completed(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the number of the task to mark as completed: "))
    if 1 <= task_num <= len(tasks):
        tasks[task_num - 1] += " (completed)"
        print(f'Task "{tasks[task_num - 1]}" marked as completed.')
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    while True:
        print("\nTo-Do List:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Mark task as completed")
        print("5. Save and exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            mark_task_completed(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
