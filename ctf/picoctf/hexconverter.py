hexinput = input("enter a hex value > ")
def hexconv(hexparam):
	split = list(hexparam)
	count = 0
	acc = 0
	while(len(split) > 0):
		length = len(split)
		val = split[length-1]
		num = 0
		if(type(val) is str):
			num = ord(val)
			if(num>47 and num <87):
				num = num - 48
			elif(num > 86 and num < 93):
				num = num - 87
			else:
				num = 0
		
		split.pop(length-1)
		acc = acc + (16 ** count * num)
		count = count + 1

	print(acc)

hexconv(hexinput)





		