import threading
def worker():
    print("Поток начал работу")
thread = threading.Thread(target=worker)
thread.start()
thread.join()