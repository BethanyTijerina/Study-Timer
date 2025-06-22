import time

#("Start timer...")
#time.sleep(5)
#print("1 second passed!")
class PomodoroTimer:
    def work_time(self):
         #run a countdown for 25 munutes (for now)
         #call self.countdown(25)
         #notify user that work session is stating
         pass
         
    def break_time(self):
        #run a countdown for 5 minutes
        #call self.countdown(5)
        #notify user that break time is starting
        pass
    def start_session(self):
        while self.break_time:#I just put something there to stop the red but this will be the loop like start the timer yes or no
            #ask the user if they want to start or quit
            #if yes:
            #  call self.work_time()
            #  call self.break_time()
            #repeat until user says no
            while self.work_time:#this will run the 25 minites and the 5 minutes
                pass
    def countdown(self, minutes):
        time.sleep(1)
        #thid will handal conversions and do MM:SS format
        #converts minutes to seconds.
        # Uses a loop to subtract 1 second at a time
        #print time each second
        #end when countdown is over
        pass