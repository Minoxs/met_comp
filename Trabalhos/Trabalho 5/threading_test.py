#!/usr/bin/env python3
import threading
from queue import Queue
import time

print_lock = threading.Lock()

def exampleJob(worker):
	time.sleep(0.5)
	with print_lock:
		print(threading.current_thread().name, worker)

def threader():
	while True:
		worker = q.get()
		exampleJob(worker)
		q.task_done()

q = Queue()

for x in range(200):
	t = threading.Thread(target=threader)
	t.daemon = True
	t.start()

start = time.time()

for worker in range(200):
	q.put(worker)
print(q)
q.join()

print("job took:",time.time()-start)