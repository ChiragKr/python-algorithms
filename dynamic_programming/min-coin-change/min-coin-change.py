import sys
import copy
import math
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

sys.stdout = open('out.txt', 'w')


def getMinChange(coins, MAXN = 100):

    combination = {k:0 for k in coins}

    min_change = [[0,combination] for i in range(MAXN)]
       
    for money in range(1,MAXN):    

        min_coins = math.inf;
        coin_added = 0;
        curr_min_coins = 0;

        for denomination in coins:
        
            if(money < denomination):
                continue

            curr_min_coins = min_change[money-denomination][0] + 1;
            if(curr_min_coins < min_coins):
                min_coins = curr_min_coins;
                coin_added = denomination;
            
        
        # print(min_coins);
        min_change[money][0] = min_coins;
        min_change[money][1] = copy.deepcopy(min_change[money-coin_added][1]);
        min_change[money][1][coin_added] += 1;

    return min_change

MAXN = 100
denomination = [1, 2, 5, 10, 20, 50, 100];
# denomination = [1, 11, 17, 20]
min_change = getMinChange(denomination, MAXN)

for money, x in enumerate(min_change,0):
    print(f"money: {money}", end=" ")
    print(f"min_coins: {x[0]}", end=" ")
    print(x[1])

coins = [min_change[i][0] for i in range(MAXN)]
money = np.arange(MAXN)

plt.bar(money, coins, align='center')
plt.xlabel('Money')
plt.ylabel('(minimum) Number of Coins')
plt.title("Money with Coins available "\
    "in denomination of {}".format(denomination))

plt.show()
