tasks_list = []

class Task(object):
    def __init__(self, number=0, description="", status="incomplete"):
        self.number = number
        self.description = description
        self.status = status

def show_help():
    print("""
    Type 'QUIT' to exit the program.
    Type 'HELP' to display this message.
    """)

def add_to_tasks(task):
    tasks_list.append(Task(len(tasks_list)+1,task))
    print('ADDED!\n')

def show_tasks():
    col_width = (max(len(task.description) for task in tasks_list))
    print('\nTODO:\n')
    for task in tasks_list:
        print("{}. {} | STATUS: {}".format(task.number,task.description.ljust(col_width),task.status))
    print('\nDONE!\n')

def complete_task(task):
    # Change status of a task to 'COMPLETE'
    print("TODO")
    

while True:
    
    response = input("> ")
    
    if response == 'QUIT':
        break
    elif response == 'HELP':
        show_help()
        continue
    elif response == 'SHOW':
        show_tasks()
        continue
    else:
        add_to_tasks(response)
        continue