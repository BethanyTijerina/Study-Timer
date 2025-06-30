import time
from task import Task

class PomodoroTimer:
    def __init__(self, task):
        self.task = task
        
    def work_time(self):
        print("Work Time!!")
        self.countdown(1) # to run a 25 minute timer. change to 25 later
        print("You did it! It's time for a break!")
        self.task.new_task()  # updates the counter for task by 1
        print(f"\nYou've completed {self.task.task_amount} session for {self.task.task_name}\n")
         #run a countdown for 25 munutes (for now)
         #call self.countdown(25)
         #notify user that work session is stating
         
    def break_time(self):
        print("Let's take a 5 minute break.")
        self.countdown(1) #to run a 5 minute timer. change to 5 later
        print("Break is over!! Let's get back to work!")
        #run a countdown for 5 minutes
        #call self.countdown(5)
        #notify user that break time is starting
        
    def start_session(self):
        start = input("\nWould you like to start a Pomodoro study session?(yes/no): ").lower()
        while start == "yes":#this will be the loop like start the timer yes or no
            self.work_time() #study cycle 25 minutes of working
            self.break_time() # study cycle 5 minutes of break
            start = input("\nWould you like to continue the Pomodoro study session?(yes/no): ").lower()
        print("Great work! See you next time!")
        #ask the user if they want to start or quit
        #if yes:
        #  call self.work_time()
        #  call self.break_time()
        #repeat until user says no
        
    def countdown(self, minutes):
        seconds = minutes * 60
        while seconds > 0: #once the timer hits 0 the loop ends and the timer is done.
            min_left = seconds //60 #get the minutes
            sec_left = seconds % 60 #get the remaining seconds
            #example: 145 seconds will be 2 minutes and 25 seconds
            print(f"{min_left:02d}:{sec_left:02d}", end="\r", flush=True) # :02d means show 2 digits example: 5 will be 05. end="\r", flush=True will overwrite the same line every second.
            time.sleep(1) # helps slow the timer. wait 1 second before it continues.
            seconds -= 1 #decreases the counter.
        print(" " * 20, end="\r") #clears the countdown
        print("Time's up!!!")
        #thid will handal conversions and do MM:SS format
        #converts minutes to seconds.
        # Uses a loop to subtract 1 second at a time
        #print time each second
        #end when countdown is over