from threading import Thread
import time
from datetime import datetime


def get_thread(thread_name):
    time.sleep(1)
    print(thread_name)


for i in range(5):
    get_thread(i + 1)

t1 = datetime.now()
threads = [Thread(target=get_thread(i + 1), args=(i + 1)) for i in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print('time ', (datetime.now() - t1).microseconds)
