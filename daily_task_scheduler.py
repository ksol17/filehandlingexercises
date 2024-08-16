import datetime

def read_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = []
            for line in file:
                description, due_date, status = line. strip().split(',')
                tasks.append({'description': description, 'due date': due_date, 'status': status})
            return tasks
    except FileNotFoundError:
        return []
    
def write_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task['decription']},{task['due_date']}\n")


def add_new_task(tasks, filename):
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    # Validate due_date format and logic here (optional)
    new_task = {'descripton': description, 'due_date': due_date, 'status': 'Pending'}
    tasks.append(new_task)
    with open(filename, 'a') as file:
        file.write(f"{description}, {due_date},Pending\n")
    print("Task added successfully.")

def mark_task_completed(tasks):
    for i, task in enumerate(tasks): 
        print(f"{i + 1}. {task['description']} - Due: {task['due_date']} - Status: {task['status']}")
    task_number = int(input("Enter task number to mark as completed: "))
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['status'] = 'Completed'
    else:
        print("Invalid task number.")


def view_overdue_tasks(tasks):
    today = datetime.date.today().isoformat()
    overdue_tasks = [task for task in tasks if task['due_date'] < today and task['status'] == 'Pending']
    print("Overdue Tasks: ")
    for task in overdue_tasks:
        print(f"- {task['description']} - Due: {task['due_date']}")


def display_tasks_by_date(tasks):
    specific_date = input("Enter date (YYYY-MM-DD) to view tasks: ")
    tasks_for_date = [task for task in tasks if task['due_date'] == specific_date]
    print(f"Tasks for {specific_date}:")
    for task in tasks_for_date:
        print(f"- {task['description']} - Status: {task['status']}")



def main():
    tasks = read_tasks('daily_tasks.txt')

    while True:
        print("\n1. Add a New Task\n2. Mark Task as Completed\n3. View Overdue Tasks\n4. Display Tasks by Date\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_new_task(tasks, 'daily_tasks.txt')
        elif choice == '2':
            mark_task_completed(tasks)
            write_tasks('daily_tasks.txt', tasks)
        elif choice == '3':
            view_overdue_tasks(tasks)
        elif choice == '4':
            display_tasks_by_date(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()