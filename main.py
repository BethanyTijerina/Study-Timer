from timer import PomodoroTimer
from task import Task

def run_text_version():
    filename = "saved_task.pkl"
    use_saved = input("Do you want to load your last saved task? (y/n): ").lower()

    if use_saved == 'y':
        task = Task.load_from_file(filename)
        if task is None:
            return  # Exit if loading failed
    else:
        work = input('Hey! What are we working on today? ')
        due = input('When is it due? ')
        while True:
            try:
                goal = int(input("How many Pomodoro sessions for this task? "))
                break
            except ValueError:
                print("Please enter a valid number.")
        task = Task(work, due, goal)

    print(f"Let's get started on: {task.task_name} (Due: {task.due_date}, Weekly Goal: {task.weekly_goal})")
    
    from timer import PomodoroTimer
    study_timer = PomodoroTimer(task)
    study_timer.start_session()

    print(f"\nYou've worked on {task.task_name}, {task.task_amount} time(s)!")
    if task.goal_reached():
        print("\nYou completed your weekly goal! Awesome!")
    else:
        print(f"\nYou have {task.weekly_goal - task.task_amount} sessions left for {task.task_name}!")

    # Save updated task
    task.save_to_file(filename)
    print(f"Progress saved to {filename}.")

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