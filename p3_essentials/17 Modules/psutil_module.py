import psutil
import os
import sys
import time


pid = os.getpid() # Gets the process ID, in this case for Python 3.4
print(pid)

p = psutil.Process(pid)
print('Process info:')
print('   name: ', p.name())
print('   exe: ', p.exe())


data = []
while True:
    data += list(range(100000))
    info = p.memory_full_info()
    # Convert to MB
    memory = info.uss / 1024 / 1024
    print('Memory used: {:.2f} MB'.format(memory))
    if memory > 40:
        print('Memory too big! Exiting.')
        sys.exit()
    time.sleep(1)
