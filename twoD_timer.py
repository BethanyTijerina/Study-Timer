import tkinter as tk #tkinter is used to create the pop up window for the timer
import time  #time used for time functions
from task import Task

class PomodoroTimer: 
    def __init__(self, display, task):
        self.display = display
        self.task = task # this will link to task object

        #Creating the name and size of the pop up window
        display.title("Study Timer")
        display.geometry("400x300")

        #Initializing timer variables to zero
        self.running = False
        self.seconds_left = 60 # the countdown starting at 25 min, change to 25*60 later
        self.break_mode = False # to track if you're on break or working
        
        #Creating text of the timer numbers and the start and stop buttons with the use of tkinter
        self.time_label = tk.Label(display, text="1:00", font=("Arial", 100)) #"tk.label" is a tkinter widget that displays the text; ".pack()"" is used for Tkinter to know where and how to put your widgets. 
        self.time_label.pack(pady=10) #Adds the time_label widget to the window and puts some space (10 pixels) above and below it so it doesn’t look cramped

        self.start_button = tk.Button(display, text="Start", command=self.start) #"tk.Button" is a widget in the tkinter library that creates a clickable button in your GUI.
        self.stop_button = tk.Button(display, text="Stop", command=self.stop) #"command=self.start" tells the button what function to run when it is clicked, in this case it is the "start" function
        self.reset_button = tk.Button(display, text="Reset", command=self.reset) # will reset the timer button
        
        #Placing the buttons on the left side of the pop up window
        self.start_button.pack(side="left", padx=10, pady=5)
        self.stop_button.pack(side="left", padx=10)
        self.reset_button.pack(side="left", padx=10)

        self.update_display() #Calls the update function
 
    def update_display(self):
        # will convert remaining seconds to the MM:SS
        minutes = self.seconds_left // 60
        seconds = self.seconds_left % 60
        self.time_label.config(text=f"{minutes:02}:{seconds:02}") # updates the label text
        
        if self.running: # only run countdown if timer is running
            if self.seconds_left > 0:
                self.seconds_left -= 1 # decrese time by 1 sec
                self.display.after(1000, self.update_display) # this will call the function again in 1 sec
            else:
                self.running = False # will stop timer when it hits 0
                if not self.break_mode:
                    self.task.new_task() # increments count for task
                    print(f"Completed 1 Pomodoro for {self.task.task_name}")
                    self.time_label.config(text="Break Time!")
                    self.break_mode = True
                    self.seconds_left = 60  # starts the break timer, change to 5*60 later
                    self.running = True
                    self.display.after(1000, self.update_display) # continue the loop
                else: # return to work
                    self.break_mode = False
                    self.seconds_left = 60 # will reset work time, change to 25*60 later
                    self.time_label.config(text="Back to Work!")
                    ####
            #Equation to update time, using time.time function (Displays the current time) minus the time the user pressed "start" 
            #self.elapsed_time = time.time() - self.start_time #self.elapsed_time stores the time that has passed while time.time() - self.start_time counts how many seconds have passed

        #total_seconds = int(self.elapsed_time) #Initializing the current time to int seconds variable

        #returns the quotientand remainder of the hours, minutes, and seconds
    def start(self):
        if not self.running:
            self.running = True # start the countdown 
            self.update_display()
    def stop(self):
        self.running = False # will stop cd without reseting it
    def reset(self):
        self.running = False
        self.break_mode = False # new cycle
        self.seconds_left = 60 # change to 25*60 later
        self.update_display() #update the screen
def launch_timer():
    task_name = input("Hey! What are we working on today? ")
    due=input('When is it due? ')
    task = Task(task_name,due)

    print(f"Let's get started on: {task.task_name} Due Date: {task.due_date}") #AM: Added due date string variable mm/dd/yyyy
    
    root = tk.Tk()  # Create the main tkinter window
    program = PomodoroTimer(root, task)  # Creates an instance (object) of the Timer class
    root.mainloop() # Keeps output window display and running
    print(f"\nYou completed {task.task_amount} Pomodoro sessions for {task.task_name}")
if __name__ == "__main__":
    launch_timer()
