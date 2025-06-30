from timer import PomodoroTimer
from task import Task

def run_text_version():
    work=input('Hey! What are we working on Today? ')#Am:not sure about this yet
    due=input('When is it due? ')
    task=Task(work,due)
    print(f"Let's get started on: {task.task_name} Due Date: {task.due_date}") #AM: Added due date string variable mm/dd/yyyy
    study_timer = PomodoroTimer(task)
    study_timer.start_session()
    print(f"\nYou've worked on {task.task_name}, {task.task_amount} time!")

def run_twoD_version():
    from twoD_timer import launch_timer
    launch_timer()

def main():
    print("Welcome to your Study Timer!")
    print("Please choose your version: ")
    print("1. Text-based Pomodoro (Terminal)")
    print("2. Popup Window Pomodoro\n")
    option = input("Enter 1 or 2: ")
    if option == "1":
        run_text_version()
    elif option == "2":
        run_twoD_version()
    else:
        print("Invalid choice")
    
if __name__ =="__main__": # only run the code below if this file is run direclty 
    main()