'''
Iterator : An object that returns elements one at a time from a sequence (or data stream) and remembers its position between calls
A py object is iterator is it has:
1. iter method: returns the iterator object itself
2. next method: returns the next item in the sequence ( raise StopIteration exception when  no more items are available)
'''

import random
class Dice:
    def __init__(self, rolls):
        self.rolls = rolls
        self.count =0

    def __iter__(self):
        return self

    def __next__(self):
        if(self.count <  self.rolls):
            self.count+=1
            return random.randint(1,6)
        else:
            raise StopIteration


dice = Dice(3)

for die in dice:
    print(die)

# under the hood implementation of above
# dice = Dice(4)
# iterator = iter(dice)
# while True:
#     try:
#         die = next(iterator)
#         print(die)
#     except StopIteration:
#         break


# list comprehension way:
# dice = [die for die in Dice(3)]
# print(dice)


gen = (n for n in range(4,11))
print(gen.__next__())

for g in gen:
    print(g)

print("\n")
def Gen(num):
    a,b=0,1
    for i in range(num):
        yield a
        a,b =b, a+b

G = Gen(11)
for g in G:
    print(g)