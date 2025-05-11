tasks = []
completed_tasks = []

while True:
    print("\n1. Add task\n2. View tasks\n3. Complete task\n4. Exit\n5. Completed tasks")
    choice = input("Enter choice: ")
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        if tasks:
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks!")
    elif choice == "3":
        if len(tasks) != 0:
            print("Your tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            index = int(input("Enter task number to complete: ")) - 1
            if 0 <= index < len(tasks):
                completed_tasks.append(tasks.pop(index))
                print("Task completed!")
            else:
                print("Invalid task number!")
        else:
            print("No tasks!")
    elif choice == "4":
        break
    elif choice == "5":
        if completed_tasks:
            print("Your completed tasks:")
            for i, task in enumerate(completed_tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No completed tasks!")
    else:
        print("Invalid choice!")



