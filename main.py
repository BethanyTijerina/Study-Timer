from timer import PomodoroTimer
from task import Task

def main():
    work=input('Hey! What are we working on Today? ')#Am:not sure about this yet
    task=Task(work)
    print(f"Let's get started on: {task.task_name}")
    study_timer = PomodoroTimer(task)
    study_timer.start_session()
    print(f"\nYou've worked on {task.task_name}, {task.task_amount} time!")
if __name__ =="__main__": # only run the code below if this file is run direclty 
    main()