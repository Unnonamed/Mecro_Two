#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ======= not used
import time
from threading import Thread, Event

class WorkThread(Thread):
    def __init__(self,  target = None, timer = 1, args : tuple = ()):     
        #super.__init__(self)
        Thread.__init__(self) 
        self.exit_event = Event()
        self.target = target
        self.args = args
        self.timer = timer
        
    def __del__(self):
        self.exit()

    def exit(self) -> None:
        self.exit_event.set()

    def sleep(self, wait_time : float):
        self.exit_event.wait(wait_time)
    
    def run(self) -> None:
        while not self.exit_event.is_set():
            print('run setting')

            if self.target:
                self.target(self.args, self.exit_event)

            self.sleep(self.timer * 1000)
            
        print("done")


def target(args : tuple, exit_event : Event):
    def sleep_(wait_time : float):
        exit_event.wait(wait_time)

    while not exit_event.is_set():
        print("target run! ...", args)
        sleep_(3)

    print("worker done")
    
    
def main():
    t = WorkThread(target=target,timer=5, args=(123,"test"))
    #t = WorkThread()
    t.start()
    try:
        while True:
            print("main work!")
            time.sleep(2)

    except KeyboardInterrupt:
        
        pass

    t.exit()
    t.join() #자식 스레드 종료 대기
    print("main done")

        

    
    
if __name__ == "__main__":
    main()