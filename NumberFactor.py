#   Created by Godstime Edet on 20/08/2024.
#   Copyright © 2024 . All rights reserved.

# Number Factor Problem  in Python

def numberFactor(n):
    if n in (0,1,2):
        return 1
    elif n == 3:
        return 2
    else:
        subP1 = numberFactor(n-1)
        subP2 = numberFactor(n-3)
        subP3 = numberFactor(n-4)
        return subP1+subP2+subP3

print(numberFactor(5))
