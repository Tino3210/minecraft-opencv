import numpy as np

kernel = np.ones((7,7), np.uint8)

lower_range_diamond = np.array([75, 80, 50])
upper_range_diamond = np.array([90, 255, 255])
lower_range_lava = np.array([7, 216, 193])
upper_range_lava = np.array([23, 255, 255])

kernel = np.ones((5,5), np.uint8)