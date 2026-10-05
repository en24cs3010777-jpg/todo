# To-Do List Application

tasks = []

def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")


while True:
    show_menu()

    choice = input("Enter your choice (1-6): ")

    # Add Task
    if choice == "1":
        task = input("Enter a new task: ")
        tasks.append({"name": task, "completed": False})
        print("Task added successfully!")

    # View Tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                status = "Done" if tasks[i]["completed"] else "Pending"
                print(f"{i+1}. {tasks[i]['name']} [{status}]")

    # Update Task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to update.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]['name']}")

            num = int(input("Enter task number to update: "))
            if 1 <= num <= len(tasks):
                new_name = input("Enter new task name: ")
                tasks[num-1]["name"] = new_name
                print("Task updated successfully!")
            else:
                print("Invalid task number.")

    # Delete Task
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]['name']}")

            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                deleted = tasks.pop(num-1)
                print(f"'{deleted['name']}' deleted successfully!")
            else:
                print("Invalid task number.")

    # Mark Completed
    elif choice == "5":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]['name']}")

            num = int(input("Enter task number to mark completed: "))
            if 1 <= num <= len(tasks):
                tasks[num-1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")

    # Exit
    elif choice == "6":
        print("Thank you for using To-Do List!")
        break

    else:
        print("Invalid choice. Please try again.")