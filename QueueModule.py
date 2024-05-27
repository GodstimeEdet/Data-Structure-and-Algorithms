#   Created by Godstime Edet on 8/04/2024.
#   Copyright © 2024 . All rights reserved.

import queue as q

customQueue = q.Queue(maxsize=3)
print(customQueue.empty())
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)
print(customQueue.full())
print(customQueue.get())
print(customQueue.qsize())
