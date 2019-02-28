from math import *

def inv_cantor(z):
	w = floor((sqrt(8*z + 1) - 1)/2)
	t = (w*w + w)/2
	y = z-t
	x = w-y
	return (int(x), int(y))
