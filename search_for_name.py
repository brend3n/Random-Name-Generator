import sys, argparse

desired_first_name = sys.argv[1].capitalize()
desired_last_name = sys.argv[2].capitalize()


# print(desired_first_name + " " +desired_last_name)
flag_f = flag_l = False

ff = open("first_name.txt", "r")

for line in ff:
	if line.strip() == (desired_first_name):
		# print("Found: " + desired_first_name)
		flag_f = True
		break
ff.close()



fl = open("last_name.txt", "r")
for line in fl:
	if line.strip() == (desired_last_name):
		# print("Found: " + desired_last_name)
		flag_l = True
		break
fl.close()

if flag_f and flag_l:
	print("Found: " + desired_first_name + " " + desired_last_name)
elif flag_f:
	print("Only Found: " + desired_first_name)
elif flag_l:
	print("Only Found: " + desired_last_name)
else:
	print("Not Found")
