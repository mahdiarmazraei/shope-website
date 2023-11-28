import time
import random

target = random.randint(2, 4)

input(f'please inter by target begin: {target}')
start = time.time()

input(f'please inter by target end: {target}')
end = time.time()

print (end - start)
