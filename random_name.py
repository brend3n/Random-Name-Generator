import random
import time

def randomName():
	ran_first = random.randint(1, 18239)

	ran_last = random.randint(1, 78475)

	# print(f"ran_first: {ran_first} rand_last: {ran_last}")

	f = open("first_name.txt", "r")
	i = 1;

	for x in f:
	    if i == ran_first :
	        first_name = x
	        break

	    i = i + 1

	f.close()



	f = open("last_name_old.txt", "r")
	f2 = open("last_name.txt", "wt")

	for line in f:
		s = line.lower()
		s = s.capitalize()
		f2.write(s)

	f.close()
	f2.close()

	f = open("last_name.txt", "r")
	i = 1

	for y in f:
	    if i == ran_last:
	        last_name = y
	        break
	    i = i + 1

	f.close()
	first_name = first_name.replace('\n', ' ')

	last_name = last_name.replace('\n', ' ')

	print(first_name  + last_name)




for i in range(10000):
	time.sleep(.5)
	randomName()
