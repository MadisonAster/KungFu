#Standard Imports#################################
import operator
from functools import reduce
##################################################

#Code#############################################
def find_it_a(xs):
    current = 0
    for i in range(len(xs)):
        current = operator.xor(xs[i], current)
        yield current
def find_it_b(xs):
    current = 0
    for i in range(len(xs)):
        current = operator.xor(xs[i], current)
        print(current)
    return current
    
def find_it_c(xs):
    return reduce(operator.xor, xs)
##################################################

#Test#############################################
'''
def c_function(fnc, xs):
    #long ret
    
    for i in range(len(xs)-1):
        a = xs[i]
        b = xs[i+1]
        ret ^^= fnc(a,b)
    
    0b 0 0 0 0 0 0 0 0 = 
    8  > 0b 0 0 0 0 1 0 0 0 > 8
    16 > 0b 0 0 0 1 1 0 0 0 > 24
    32 > 0b 0 0 1 1 1 0 0 0 > 56
    64 > 0b 0 1 1 1 1 0 0 0 > 120
    32 > 0b 0 1 0 1 1 0 0 0 > 88
    64 > 0b 0 0 0 1 1 0 0 0 > 24
    8  > 0b 0 0 0 1 0 0 0 0 > 16
    
[a, b, c, d, e, f]
xor(xor(xor(xor(a, b), c), d), e), f)
'''
##################################################

#Main#############################################
if __name__ == '__main__':
    KungFu.main(__file__)
##################################################
