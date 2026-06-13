tasks = []

print("===== DAILY TASK MANAGER =====")

while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Clear All Tasks")
    print("5. Exit")

    option = input("Choose an option: ")

    if option == '1':
        new_task = input("Enter task: ")
        tasks.append(new_task)
        print("Task Added Successfully!")

    elif option == '2':
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for index, item in enumerate(tasks, start=1):
                print(f"{index}. {item}")

    elif option == '3':
        remove_task = int(input("Enter task number to delete: "))

        if 0 < remove_task <= len(tasks):
            deleted = tasks.pop(remove_task - 1)
            print("Deleted Task:", deleted)
        else:
            print("Invalid task number.")

    elif option == '4':
        tasks.clear()
        print("All tasks cleared!")

    elif option == '5':
        print("Exiting Program...")
        break

    else:
        print("Invalid option")