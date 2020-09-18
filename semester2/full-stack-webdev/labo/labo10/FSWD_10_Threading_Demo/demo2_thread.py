import time
import threading

def zeg_hello():
    #zeg 6 maal hello maar wacht 2 seconden tussen elke boodschap
    for i in range(6):
        print(f"Hello student {i}")
        time.sleep(2)

mijn_ander_proces = threading.Thread(target=zeg_hello)
mijn_ander_proces.start()

print('veeg het bord af')
print('start de pc op')
print('start de beamer op')
print('ga naar leho')





