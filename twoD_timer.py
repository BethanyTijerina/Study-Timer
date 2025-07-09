import tkinter as tk #tkinter is used to create the pop up window for the timer
from tkinter import messagebox #creates popup windows for when time is up
import time  #time used for time functions
from task import Task
import winsound #creates a unique sound for the pop up window
from tkinter import simpledialog
from tkinter import ttk


class PomodoroTimer: 
    def __init__(self, display, task):
        self.display = display
        self.task = task # this will link to task object

        # Get the screen width to calculate top right position 
        screen_width = display.winfo_screenwidth()
        window_width = 400 
        x = screen_width - window_width
        y = 0  # top edge
        display.geometry(f"+{x}+{y}")
        display.attributes('-topmost', 1) # will keep window in front of everything!

        #Creating the name and size of the pop up window
        display.title("Pomodoro Alarm Clock")
        display.geometry("400x300")
        display.configure(bg="#FFFAF0") #like a light cream off white background

        #Initializing timer variables to zero
        self.running = False
        self.seconds_left = 25*60 # the countdown starting at 25 min, change to 25*60 later
        self.break_mode = False # to track if you're on break or working
        
        #DESIGN: creating a clock like frame to simulate a alarm clock
        self.clock_frame = tk.Frame(display, bg="#282c34", bd=10, relief="ridge")
        self.clock_frame.pack(pady=40)
        self.top_decor_frame = tk.Frame(self.clock_frame, bg="#282c34")
        self.top_decor_frame.place(relx=0.5, y=-3, anchor="s")
        
        self.light1 = tk.Label(self.top_decor_frame, text="🔴", font=("Arial", 14), bg="lightgrey", relief="raised", bd=2, padx=6, pady=3)
        self.light2 = tk.Label(self.top_decor_frame, text="🔵", font=("Arial", 14), bg="lightgrey", relief="raised", bd=2, padx=6, pady=3)
        self.light3 = tk.Label(self.top_decor_frame, text="🟢", font=("Arial", 14), bg="lightgrey", relief="raised", bd=2, padx=6, pady=3)
        
        #Placing on the left side of the pop up window
        self.light1.pack(side="left", padx=4)
        self.light2.pack(side="left", padx=4)
        self.light3.pack(side="left", padx=4)
        
        #Creating text of the timer numbers and the start and stop buttons with the use of tkinter
        self.time_label = tk.Label(self.clock_frame, text="25:00", font=("Courier",48, "bold"), fg="#39FF14", bg="#282c34") #"tk.label" is a tkinter widget that displays the text
        self.time_label.pack()  # ".pack()"" is used for Tkinter to know where and how to put your widgets. 
        
        self.status_label = tk.Label(display, text="Ready to Work!", font=("Comic Sans MS", 14), bg="#FFFAF0")
        self.status_label.pack(pady=10)

        self.start_button = tk.Button(display, text="Start", command=self.start) #"tk.Button" is a widget in the tkinter library that creates a clickable button in your GUI.
        self.stop_button = tk.Button(display, text="Stop", command=self.stop) #"command=self.start" tells the button what function to run when it is clicked, in this case it is the "start" function
        self.reset_button = tk.Button(display, text="Reset", command=self.reset) # will reset the timer button
        
        #Placing the buttons on the left side of the pop up window
        self.start_button.pack(side="left", padx=10)
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
                    self.time_label.config(text="Break Time!", font=("Courier", 38, "bold"))
                    self.status_label.config(text="Break Time!")
                    self.display.lift()
                    self.display.attributes("-topmost", 1) # always on top
                    self.display.focus_force()
                    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                    messagebox.showinfo("Break Time!", "Take a 5-minute break and relax!",parent=self.display)
                    self.break_mode = True
                    self.seconds_left = 5*60  # starts the break timer, change to 5*60 later
                    self.running = True
                    self.display.after(1000, self.update_display) # continue the loop
                else: # return to work
                    self.break_mode = False
                    self.seconds_left = 25*60 # will reset work time, change to 25*60 later
                    self.time_label.config(text="Back to Work!", font=("Courier", 32, "bold"))
                    self.status_label.config(text="Ready to Work!")
                    self.display.lift()
                    self.display.attributes("-topmost", 1) # always on top
                    self.display.focus_force()
                    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                    messagebox.showinfo("Back to Work!", "Break’s over! Time to focus again.",parent=self.display)
                    ####
            #Equation to update time, using time.time function (Displays the current time) minus the time the user pressed "start" 
            #self.elapsed_time = time.time() - self.start_time #self.elapsed_time stores the time that has passed while time.time() - self.start_time counts how many seconds have passed

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
        self.seconds_left = 25*60 # change to 25*60 later
        self.update_display() #update the screen
def launch_timer():
    root_form = tk.Tk()
    root_form.withdraw() # hid the small root window
    task_name = simpledialog.askstring("Task Name", "Hey! What are we working on today? ")
    if not task_name:
        return
    
    due=simpledialog.askstring("Due Date", "When is it due? (MM/DD/YYYY)")
    if not due:
        return
    while True:
        try:
            goal = simpledialog.askinteger("Weekly Goal", "How many Pomodoro sections for this task? ")
            if goal is None:
                return
            break
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            
    task = Task(task_name,due,goal)

    messagebox.showinfo("Task Info", f"Let's get started on:\n{task.task_name}\nDue Date: {task.due_date}\nWeekly Goal: {task.weekly_goal}") #AM: Added due date string variable mm/dd/yyyy
    def on_closing():
        root.destroy()
        progress_bar(task)
    root = tk.Tk()  # Create the main tkinter window
    program = PomodoroTimer(root, task)  # Creates an instance (object) of the Timer class
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop() # Keeps output window display and running
    messagebox.showinfo("Progress Summary",f"You completed {task.task_amount} Pomodoro sessions for {task.task_name}. \nWeek Goal: {task.weekly_goal}")


def progress_bar(task):
    progress = tk.Tk()
    progress.title("Pomodoro Progress")
    progress.geometry("350x150")
    progress.configure(bg="#FFFAF0")
    
    label = tk.Label(progress, text=f"{task.task_name} Progress", font=("Arial", 12, "bold"), bg="#FFFAF0")
    label.pack(pady=10)
    progress_tk = ttk.Progressbar(progress, length=250, mode='determinate')
    progress_tk.pack(pady=10)
    
    max_value = task.weekly_goal
    current_value = min(task.task_amount, max_value)
    progress_tk["maximum"]= max_value
    progress_tk["value"] = current_value
    
    percentage = (current_value / max_value)*100 if max_value else 0
    sum = tk.Label(progress, text=f"{current_value}/{max_value} Pomodoros complete ({percentage:.1f}%)", bg="#FFFAF0")
    sum.pack(pady=5)
    progress.mainloop()

if __name__ == "__main__":
    launch_timer()
