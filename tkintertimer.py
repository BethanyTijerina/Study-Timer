import tkinter as tk #tkinter is used to create the pop up window for the timer
import time  #time used for time functions

class Timer: 
    def __init__(self, display):
        self.display = display

        #Creating the name and size of the pop up window
        display.title("Study Timer")
        display.geometry("400x300")

        #Initializing timer variables to zero
        self.running = False
        self.start_time = None
        self.elapsed_time = 0
        
        #Creating text of the timer numbers and the start and stop buttons with the use of tkinter
        self.time_label = tk.Label(display, text="00:00:00", font=("Arial", 36)) #"tk.label" is a tkinter widget that displays the text; ".pack()"" is used for Tkinter to know where and how to put your widgets. 
        self.time_label.pack(pady=10) #Adds the time_label widget to the window and puts some space (10 pixels) above and below it so it doesn’t look cramped

        self.start_button = tk.Button(display, text="Start", command=self.start) #"tk.Button" is a widget in the tkinter library that creates a clickable button in your GUI.
        self.stop_button = tk.Button(display, text="Stop", command=self.stop) #"command=self.start" tells the button what function to run when it is clicked, in this case it is the "start" function

        #Placing the buttons on the left side of the pop up window
        self.start_button.pack(side="left", padx=10, pady=5)
        self.stop_button.pack(side="left", padx=10)

        self.update_display() #Calls the update function
 
    def update_display(self):
        if self.running:
            #Equation to update time, using time.time function (Displays the current time) minus the time the user pressed "start" 
            self.elapsed_time = time.time() - self.start_time #self.elapsed_time stores the time that has passed while time.time() - self.start_time counts how many seconds have passed

        total_seconds = int(self.elapsed_time) #Initializing the current time to int seconds variable

        #returns the quotient and remainder of the hours, minutes, and seconds
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        hours = minutes // 60
        minutes = minutes % 60

        #Updates the text of the timer, the "02" means it's showing 2 digits for hours, minutes and seconds
        self.time_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
        self.display.after(500, self.update_display)

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time  # Resume timer from where it left off
            self.running = True

    def stop(self):
        self.running = False #Sets the running time to false when pressing stop to stop timer

root = tk.Tk()  # Create the main tkinter window
program = Timer(root)  # Creates an instance (object) of the Timer class
root.mainloop() # Keeps output window display and running