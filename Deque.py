#   Created by Godstime Edet on 8/04/2024.
#   Copyright © 2024 . All rights reserved.

# How to use collections.deque as a FIFO queue:

from collections import deque

customQueue = deque(maxlen=3)
print(customQueue)

customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
customQueue.append(4)
print(customQueue)
print(customQueue.clear())
print(customQueue)
