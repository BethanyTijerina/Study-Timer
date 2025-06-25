from timer import PomodoroTimer
from task import Task

def main():
    work=input('Hey what are we working on Today? ')#Am:not sure about this yet
    a=Task(work)
    study_timer = PomodoroTimer()
    study_timer.start_session()
if __name__ =="__main__": # only run the code below if this file is run direclty 
    main()