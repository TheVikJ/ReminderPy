import datetime
import time
from win10toast import ToastNotifier

n = ToastNotifier()

event = input("Set reminder time (hours:minutes): ")
eventname = input("Set reminder name: ")

while True:
    if datetime.datetime.now().strftime('%H:%M') == event:
        n.show_toast("Reminder App", eventname, duration = 100)
        break
    else:
        time.sleep(5)
