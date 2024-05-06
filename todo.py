class Todo:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{status} {self.title}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title):
        self.tasks.append(Todo(title))

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True

    def get_tasks(self):
        return self.tasks


def print_tasks(tasks):
    if tasks:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")
    else:
        print("No tasks.")


def main():
    task_manager = TaskManager()

    while True:
        print("\n1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. View Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            task_manager.add_task(title)
        elif choice == "2":
            print_tasks(task_manager.get_tasks())
            index = int(input("Enter task index to delete: ")) - 1
            task_manager.delete_task(index)
        elif choice == "3":
            print_tasks(task_manager.get_tasks())
            index = int(input("Enter task index to mark as completed: ")) - 1
            task_manager.mark_task_completed(index)
        elif choice == "4":
            print_tasks(task_manager.get_tasks())
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
