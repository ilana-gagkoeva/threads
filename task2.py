import threading
def worker(num):
    print(f"Поток {num} работает.")
threads = []
for num in range(3):
    thread = threading.Thread(target=worker, args=(num,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()