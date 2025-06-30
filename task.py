#from timer import PomodoroTimer

class Task:
    def __init__(self,task_name,due_date):# AM: defines the task name and when object is made amount can be set to zero
        self.task_name=task_name
        self.task_amount= 0 #the default starting point
        self.due_date=due_date
    def new_task(self):# AM: creates a new task and keeps track of task amounts
        self.task_amount+=1
        
#think about maybe adding due dates??

