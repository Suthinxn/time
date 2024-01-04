import time

if __name__ == '__main__':
    sec = 0
    minute = 0
    hour = 0
    while True :
        time.sleep(0.1)
        # print(f" {hour:02d} : {minute:02d} : {sec:02d}")
        print(f" {hour:02d} : {minute:02d}")
        sec += 1
        if sec == 60:
            sec -= 60
            minute += 1
        if minute == 60:
            hour += 1
            minute -= 60 
        if hour == 24 :
            hour -= 24
