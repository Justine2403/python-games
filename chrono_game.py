import time 
import random 

def countdown(t):
    while t>0:
        (mins, secs) = divmod(t, 60) # transforms sec into min and sec using modulo 60
        timer='{:02d}:{:02d}'.format(mins, secs) # min, sec format
        print(timer, end='\r') #'\r' writes on the same line
        time.sleep(1)
        t-=1
    print("Start now !")

def chrono_game(t):
    print(f"Stop at {t} seconds")
    time_start_int = 3 # intervalle of time to let player time to prepare for game
    countdown(time_start_int)
    time_start = time.time()
    input()
    time_end = time.time()
    result = float(time_end-time_start)
    print("You have stopped at:")
    print("%.2f" % result)
        

t = random.randint(10,20)
chrono_game(t)

        

