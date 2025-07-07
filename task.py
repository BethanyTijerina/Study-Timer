#from timer import PomodoroTimer

class Task:
    def __init__(self,task_name,due_date, weekly_goal):# AM: defines the task name and when object is made amount can be set to zero
        self.task_name=task_name
        self.task_amount= 0 #the default starting point
        self.due_date=due_date
        self.weekly_goal = weekly_goal
    def new_task(self):# AM: creates a new task and keeps track of task amounts
        self.task_amount+=1
        if self.goal_reached():
            print(f"Goal reached for {self.task_name}! {self.task_amount}/{self.weekly_goal} Pomodoros done!")
            
    def goal_reached(self):
        return self.task_amount >= self.weekly_goal
        
#think about maybe adding due dates??

