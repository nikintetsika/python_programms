import random

randoms_numbers = random.sample(xrange(-30,30),30)
i=len(randoms_numbers) 

def num(randoms_numbers, i):
	for a in range(0,i-2):
		for b in range(a+1,i-1):
			for c in range(b+1,i):
				if (randoms_numbers[a] + randoms_numbers[b] + randoms_numbers[c] == 0 ):
					print (randoms_numbers[a], randoms_numbers[b] , randoms_numbers[c] )
				else:
					print "There aren't numbers"
num(randoms_numbers,i)
