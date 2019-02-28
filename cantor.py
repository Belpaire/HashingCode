from math import *

def inv_cantor(z):
	w = floor((sqrt(8*z + 1) - 1)/2)
	t = (w*w + w)/2
	y = z-t
	x = w-y
	return (int(x), int(y))

def lfsr(seed):
    for i in range(1,17):
        feedback_bit = seed[2] ^ seed[16]

        if feedback_bit == 1:
            feedback_bit = 0
        else:
            feedback_bit = 1

        for j in range(0, 16):
            seed[j] = seed[j+1]

        seed[16] = feedback_bit

        seed_string = ""

        #for j in seed:
        #    seed_string += str(j)

    seed_string = ''.join([str(j) for j in seed])

    return (int(seed_string, 2), seed)
