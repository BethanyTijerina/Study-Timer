#from timer import PomodoroTimer

import pickle
import os

class Task:
    def __init__(self, task_name, due_date, weekly_goal):
        self.task_name = task_name
        self.task_amount = 0
        self.due_date = due_date
        self.weekly_goal = weekly_goal

    def new_task(self):
        self.task_amount += 1
        if self.goal_reached():
            print(f"Goal reached for {self.task_name}! {self.task_amount}/{self.weekly_goal} Pomodoros done!")

    def goal_reached(self):
        return self.task_amount >= self.weekly_goal

    def save_to_file(self, filename):
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    def load_from_file(filename):
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                task = pickle.load(f)
                # Adjust the weekly goal and reset amount
                print(f"⏳ Loading previous progress: {task.task_amount}/{task.weekly_goal}")
                task.weekly_goal = max(1, task.weekly_goal - task.task_amount)
                task.task_amount = 0
                print(f"🔁 Adjusted weekly goal: {task.weekly_goal}")
                return task
        else:
            print(f"No saved task found at {filename}.")
            return None