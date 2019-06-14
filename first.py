import threading
import time


def test():
    while True:
        print('haha')
        time.sleep(1)

t = threading.Thread(target=test)
t.start()
print('marsk threading end')

