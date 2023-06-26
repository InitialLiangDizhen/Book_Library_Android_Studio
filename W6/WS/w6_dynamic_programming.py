
from math import inf

#bottom up
def coin_change(self, n, coin=[1,5,9]): #m for coin
    self.memo = [inf] * [n+1]
    m = len(coin)

    #base case, bottom-up
    self.memo[0] = 0 #initial memozation value

    for value in range(1, n+1):
        for j in range(m): #for each value in list, loop through each coin
            if coin[j] <= value:
                balance = value - coin[j]
                count = 1 + self.memo[balance] #
                if count < 1 + self.memo[balance]: #count equals the 1 + previous optimal solution
                    if count < self.memo[value]: #new optimal solution
                        self.memo[value] = count
    return self.memo[n]
