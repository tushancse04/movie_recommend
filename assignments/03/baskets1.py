# Generate random baskets used to study the Market-Basket model
import random
N = 10
B = 20


#-----------------------------------------------------------------------
def a_random_basket(min_size, max_size):
	size = random.randint(min_size, max_size)
	b = set()
	items = range(N)
	while len(b) < size:
		item = random.choice(items)
		if item not in b:
			b.add(item)
	return b

#-----------------------------------------------------------------------
def random_baskets(min_size, max_size):
	baskets = []
	for i in range(B):
		baskets.append(a_random_basket(min_size, max_size))
	return baskets

#-----------------------------------------------------------------------
def init(n, b):
	global N, B
	N, B = n, b
#-----------------------------------------------------------------------

if __name__ == '__main__':
	init(100, 5)
	for i in range(B):
		print(a_random_basket(4,10))

