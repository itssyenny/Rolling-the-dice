import random

#def main() :
smallest_number = 1
largest_number = 6

re_rolling = "YES"

while re_rolling == "YES" or re_rolling == "Y":
	print "Rolling the dices ..."
	print "The values are ..."
	print random.randint(smallest_number, largest_number)
	print random.randint(smallest_number, largest_number)

	re_rolling = raw_input("Do you want to roll the dices again?")

#if __name__ == '__main__':
#	main()