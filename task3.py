# threads with pause
import threading
import time

def worker(num):
    print(f"Поток {num} начал работу")
    time.sleep(0.5)
    print(f"Поток {num} завершил работу")
threads = []
for num in range(3):
    thread = threading.Thread(target=worker, args=(num,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()