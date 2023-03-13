import datetime
import time
from random import randint



while True:
    
    heute = datetime.datetime.today()
    sekunden = heute.second
    if sekunden % 2 == 0:
        print(sekunden, "ist eine gerade Sekunde")
    else:
        print(sekunden, "ist eine ungerade Sekunde")
    zufwartezeit = randint(1,3)
    time.sleep(zufwartezeit)
    