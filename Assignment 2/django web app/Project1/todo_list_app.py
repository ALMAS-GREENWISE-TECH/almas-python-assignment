# Functions to add, mark as completed, display, and delete tasks
def add_task(tasks, new_task):
    tasks.append(new_task)

def mark_completed(tasks, task_index):
    tasks[task_index] = tasks[task_index] + " (Completed)"

def display_tasks(tasks):
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")

def delete_task(tasks, task_index):
    del tasks[task_index]
# Functions to save and load tasks from a text file
def save_tasks_to_file(tasks, file_path):
    with open(file_path, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def load_tasks_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            tasks = [line.strip() for line in file]
        return tasks
    except FileNotFoundError:
        return []
# Test the Todo List functions
tasks_file_path = 'tasks.txt'
tasks = load_tasks_from_file(tasks_file_path)

add_task(tasks, 'Buy groceries')
mark_completed(tasks, 0)
add_task(tasks, 'Write report')
display_tasks(tasks)
delete_task(tasks, 0)

save_tasks_to_file(tasks, tasks_file_path)
