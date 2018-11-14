tasks_list = []

class Task(object):
    """Creates a task object."""
    
    def __init__(self, number=0, description="", status="incomplete"):
        self.number = number
        self.description = description
        self.status = status


def show_help():
    """Displays a help menu."""
    print("""
    Type '!QUIT' to exit the program.
    Type '!SHOW' to show current tasks.
    Type '!COMPLETE' and the number of a task to change it's status to complete.
    Type '!HELP' to display this message.
    """)


def add_to_tasks(task):
    """
    Adds a task to the task_list and displays a
    confirmation messsage.

    :param task: Task object
    """
    tasks_list.append(Task(len(tasks_list)+1,task))
    print('Task number {} has been added!\n'.format(len(tasks_list)))


def show_tasks():
    """Prints all tasks to the console."""
    col_width = (max(len(task.description) for task in tasks_list))
    print('\nTODO:\n')
    for task in tasks_list:
        print("{}. {} | STATUS: {}".format(task.number,task.description.ljust(col_width),task.status))
    print('\nDONE!\n')


def complete_task(number):
    """Marks a task as complete."""
    for task in tasks_list:
        if task.number == number:
            task.status = 'COMPLETE'
            print("Task '{}' has been completed".format(task.description))


while True:

    response = input("> ")

    if response == '!QUIT':
        break
    elif response == '!HELP':
        show_help()
        continue
    elif response == '!SHOW':
        show_tasks()
        continue
    elif '!COMPLETE' in response:
        task = response.split(' ')
        complete_task(int(task[1]))
        continue
    else:
        add_to_tasks(response)
        continue
