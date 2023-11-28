from random import randint
from collections import Counter

def dicee(*dice, trial=100):
        count = Counter()   
        for _ in range(trial):
                count[sum(randint(1,side) for side in dice)] += 1
        
        print('\noutcome\tprobability')
        for outcome in range(len(dice), sum(dice) + 1):
                print(f'{outcome}\t{count[outcome] *100 / trial :0.2f}%')
    
try:
    my_list = []
 
    while True:
        my_list.append(int(input()))
except:
      dicee(*my_list)