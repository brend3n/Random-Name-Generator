import sys, argparse

desired_first_name = sys.argv[1].capitalize()
desired_last_name = sys.argv[2].capitalize()


# print(desired_first_name + " " +desired_last_name)

ff = open("first_name.txt", "r")

for line in ff:
	if line.strip() == (desired_first_name):
		print("Found: " + desired_first_name)
		break
ff.close()



fl = open("last_name.txt", "r")
for line in fl:
	if line.strip() == (desired_last_name):
		print("Found: " + desired_last_name)
		break
fl.close()
