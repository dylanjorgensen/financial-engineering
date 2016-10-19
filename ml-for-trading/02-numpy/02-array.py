

import numpy as np


pirate = np.ndarray(shape=(10,10), dtype=float)
land_lubber = np.ndarray(shape=(3,3), dtype=float)


# returns just the top row and first column

pirate[0:1, 0:1] = land_lubber[0:1, 0:1]

pirate[0,0] = 69
pirate[1, :] = [1,2,3,4,5,6,7,8,9,0]


print pirate[0:4, 0:3]

index = np.array([1,2,1,2,1,2])
print pirate[index]



