import random

def gen_random(num_count, begin, end):
    for i in range(num_count):
        yield random.randrange(begin, end + 1)

f = gen_random(5, 1, 3)

#for i in f:
#    print(i)