tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed successfully!")
    else:
        print("Task not found.")

def display_tasks():
    if tasks:
        print("Your To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
    else:
        print("Your To-Do List is empty.")

def main():
    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == '3':
            display_tasks()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
