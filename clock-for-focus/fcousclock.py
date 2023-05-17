import time

def pomodoro_timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        m, s = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(m, s)
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("Time's up!")
