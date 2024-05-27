#   Created by Godstime Edet on 8/04/2024.
#   Copyright © 2024 . All rights reserved.

# How to use multiprocessing.Queue as a FIFO queue:

from multiprocessing import Queue

customQueue = Queue(maxsize= 3)
customQueue.put(1)
print(customQueue.get())
