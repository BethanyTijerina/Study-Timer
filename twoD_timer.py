import tkinter as tk #tkinter is used to create the pop up window for the timer
from tkinter import messagebox #creates popup windows for when time is up
import time  #time used for time functions
from task import Task
import winsound #creates a unique sound for the pop up window
from tkinter import simpledialog
from tkinter import ttk

class PomodoroTimer: 
    def __init__(self, display, task) :
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
        self.user_time = 25*60    # default user-set time for reset
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
        self.time_label = tk.Label(self.clock_frame, text="Set Time", font=("Courier",48, "bold"), fg="#39FF14", bg="#282c34")
        self.time_label.pack()  
        self.time_label.bind("<Button-1>", self.make_time_editable)

        self.status_label = tk.Label(display, text="Ready to Work!", font=("Comic Sans MS", 14), bg="#FFFAF0")
        self.status_label.pack(pady=10)

        self.start_button = tk.Button(display, text="Start", command=self.start) 
        self.stop_button = tk.Button(display, text="Stop", command=self.stop) 
        self.reset_button = tk.Button(display, text="Reset", command=self.reset) 
        
        #Placing the buttons on the left side of the pop up window
        self.start_button.pack(side="left", padx=10)
        self.stop_button.pack(side="left", padx=10)
        self.reset_button.pack(side="left", padx=10)

    def make_time_editable(self, event):
        self.time_label.pack_forget()
        self.edit_entry = tk.Entry(self.clock_frame, font=("Courier", 48, "bold"), justify="center", fg="#39FF14", bg="#282c34", bd=0)
        self.edit_entry.insert(0, self.time_label.cget("text"))
        self.edit_entry.pack()
        self.edit_entry.focus()
        self.edit_entry.bind("<Return>", self.set_time_from_entry)

    def set_time_from_entry(self, event):
        time_str = self.edit_entry.get()
        try:
            parts = list(map(int, time_str.split(":")))
            if len(parts) == 2:
                minutes, seconds = parts
                total_seconds = minutes * 60 + seconds
            elif len(parts) == 3:
                hours, minutes, seconds = parts
                total_seconds = hours * 3600 + minutes * 60 + seconds
            else:
                raise ValueError

            self.seconds_left = total_seconds
            self.user_time = total_seconds
            self.edit_entry.destroy()
            self.time_label.pack()
            self.update_display()
        except ValueError:
            messagebox.showerror("Invalid Time", "Enter time as MM:SS or HH:MM:SS", parent=self.display)

        self.update_display()  

    def update_display(self):
        minutes = self.seconds_left // 60
        seconds = self.seconds_left % 60
        self.time_label.config(text=f"{minutes:02}:{seconds:02}") 
        
        if self.running:
            if self.seconds_left > 0:
                self.seconds_left -= 1 
                self.display.after(1000, self.update_display)
            else:
                self.running = False
                if not self.break_mode:
                    self.task.new_task()  # increments Pomodoro sessions completed
                    print(f"Completed 1 Pomodoro for {self.task.task_name}")
                    self.time_label.config(text="Break Time!", font=("Courier", 38, "bold"))
                    self.status_label.config(text="Break Time!")
                    self.display.lift()
                    self.display.attributes("-topmost", 1)
                    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                    messagebox.showinfo("Break Time!", "Take a 5-minute break and relax!", parent=self.display)
                    self.break_mode = True
                    self.seconds_left = 5*60  
                    self.running = True
                    self.display.after(1000, self.update_display)
                else:
                    self.break_mode = False
                    self.seconds_left = self.user_time  # reset to user-set time
                    self.time_label.config(text="Back to Work!", font=("Courier", 32, "bold"))
                    self.status_label.config(text="Ready to Work!")
                    self.display.lift()
                    self.display.attributes("-topmost", 1)
                    winsound.PlaySound("SystemExclamation", winsound.SND_ALIAS)
                    messagebox.showinfo("Back to Work!", "Break’s over! Time to focus again.", parent=self.display)

    def start(self):
        if not self.running:
            self.running = True
            self.update_display()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.break_mode = False
        self.seconds_left = self.user_time  # reset to user-set time
        self.update_display()

def launch_timer():
    root_form = tk.Tk()
    root_form.withdraw() # hide the small root window
    task_name = simpledialog.askstring("Task Name", "Hey! What are we working on today? ")
    if not task_name:
        return
    
    due = simpledialog.askstring("Due Date", "When is it due? (MM/DD/YYYY)")
    if not due:
        return

    while True:
        try:
            goal = simpledialog.askinteger("Weekly Goal", "How many Pomodoro sections for this task? ")
            if goal is None:
                return
            break
        except ValueError:
            print("Please enter a valid number.")
            
    task = Task(task_name, due, goal)

    messagebox.showinfo("Task Info", f"Let's get started on:\n{task.task_name}\nDue Date: {task.due_date}\nWeekly Goal: {task.weekly_goal}")
    
    def on_closing():
        root.destroy()
        progress_bar(task)

    root = tk.Tk()  
    program = PomodoroTimer(root, task)  
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop() 
    
    print(f"\nYou completed {task.task_amount} Pomodoro sessions for {task.task_name}")
    if task.goal_reached():
        print("\nYou Completed Your Weekly Goal! Awesome!")
    else:
        print(f"\n You Have {task.weekly_goal - task.task_amount} sessions left for {task.task_name}!")

    
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
