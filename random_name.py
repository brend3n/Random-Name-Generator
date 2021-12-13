import random
import time

# ! Outdated
def randomName():
	ran_first = random.randint(1, 18239)
	ran_last = random.randint(1, 78475)

	# print(f"ran_first: {ran_first} rand_last: {ran_last}")

	f = open("first_name.txt", "r")
	i = 1;

	for x in f:
	    if i == ran_first:
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

# ! Outdated
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

# ! Outdated
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


# Takes a path to the root directory
def random_name_updated(path=""):
    last_names = []
    first_names = []
    
    first_name_file_path = f"{path}first_name.txt"
    last_name_file_path = f"{path}last_name.txt"
    
    with (open(first_name_file_path, "r")) as f:
        first_names = f.readlines()
    f.close()
    
    with (open(last_name_file_path, "r")) as f:
        last_names = f.readlines()
    f.close()
    
    first_name = random.choice(first_names).replace("\n", "") 
    last_name = random.choice(last_names).replace("\n", "")
    
    name = f"{first_name} {last_name}"
    return name
	

def random_first_name_updated(path):
    first_names = []
    first_name_file_path = f"{path}first_name.txt"
    with (open(first_name_file_path, "r")) as f:
        first_names = f.readlines()
    f.close()
    first_name = random.choice(first_names).replace("\n", "") 
    return first_name

def random_last_name_updated(path=""):
    last_names = []
    last_name_file_path = f"{path}last_name.txt"

    with (open(last_name_file_path, "r")) as f:
        last_names = f.readlines()
    f.close()
    last_name = random.choice(last_names).replace("\n", "")
    return last_name



# random_first_name()
# random_last_name()
# name = randomName()
# print("test")
# print(random_name_updated())





