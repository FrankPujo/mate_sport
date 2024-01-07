import matplotlib.pyplot as plt
import matplotlib.colors as cls
import numpy as np
import math

colours = ["green", "lawngreen", "gold", "orange", "red"]
clrs_map = cls.LinearSegmentedColormap.from_list("idk", colours)

def calc_prob(x, y):
	dp1_sq = y ** 2 + (x + 3.66) ** 2
	dp1 = math.sqrt(dp1_sq)
	dp2_sq = y ** 2 + (x - 3.66) ** 2
	dp2 = math.sqrt(dp2_sq)
	lp_sq = 7.32 ** 2
	#law of cosines
	ang_porta = math.acos((dp1_sq + dp2_sq - lp_sq)/(2 * dp1 * dp2))
	ang_porta_norm = math.sqrt( ang_porta / math.pi )
	
	dist = math.sqrt(x**2 + y**2)
	dist_norm = (75 - dist) / 75
	
	ang_ass = math.atan(abs(x)/abs(y))
	ang_ass_norm = (math.pi - ang_ass) / math.pi
	
	return ang_porta_norm

data = []
for i in range(10):
	line = []
	for j in range(14):
		x = -32.5 + 5 * j
		y = 2.5 + 5 * i
		prb = calc_prob(x, y)
		line.append(prb)
	data.append(line)

plt.imshow(data, cmap=clrs_map, interpolation="nearest")
plt.show()
