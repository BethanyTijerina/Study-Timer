#from timer import PomodoroTimer

class Task:
    def __init__(self,task_name):# AM: defines the task name and when object is made amount can be set to zero
        self.task_name=task_name
        self.task_amount= 1 #the default starting point
    def new_task(self):# AM: creates a new task and keeps track of task amounts
        self.task_amount+=1
        
#think about maybe adding due dates??

