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



	f = open("last_name.txt", "r")
	i = 1

	for y in f:
	    if i == ran_last:
	        last_name = y
	        break
	    i = i + 1

	f.close()
	first_name = first_name.replace('\n', '')

	last_name = last_name.replace('\n', '')

	name = f"{first_name} {last_name}"
	print(name)
	return name

def random_first_name():
	ran_first = random.randint(1, 18239)

	f = open("./Random-Name-Generator/first_name.txt", "r")
	i = 1;

	for x in f:
	    if i == ran_first :
	        first_name = x
	        break

	    i = i + 1

	f.close()
	first_name = first_name.replace('\n', '')
	print(first_name)
	return first_name

def random_last_name():
	f = open("./Random-Name-Generator/last_name.txt", "r")
	i = 1
	ran_last = random.randint(1, 78475)


	for y in f:
	    if i == ran_last:
	        last_name = y
	        break
	    i = i + 1

	f.close()

	last_name = last_name.replace('\n', '')
	print(last_name)
	return last_name



# random_first_name()
# random_last_name()
# name = randomName()





