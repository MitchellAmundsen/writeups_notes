
#i = 0
#numbers = []
#
#while i < 6:
#	print "At the top i is %d" % i
#	numbers.append(i)
#
#	i = i + 1
#	print "Numbers now: ", numbers
#	print "At the bottom i is %d" % i
#
#print "The numbers: "
#
#for num in numbers:
#	print num

def numfunc(amount, increment):
	i = 0
	numbers = []

	while i < amount:
		print "At the top i is %d" % i
		numbers.append(i)

		i = i + increment
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num

numfunc(6, 1)
input = raw_input()
inputnum = int(input)
incinput = int(raw_input())
numfunc(inputnum, incinput)