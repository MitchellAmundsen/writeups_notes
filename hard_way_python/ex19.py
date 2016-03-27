def cheese_and_crackers(cheese, crackers):
	print "You have %d cheeses!" % cheese
	print "You have %d boxes of creackers!" % crackers
	print "That's enough for a party!"
	print "Too bad cheese and crackers is bad party food..."
	
print "We can just give the numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script"
amount_cheese = 10
amount_crackers = 15

cheese_and_crackers(amount_cheese, amount_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_cheese + 50, amount_crackers + 35)

def personal(var):
	print "I'm printing your %r variable" % var
	print "Cool, I'm not feeling creative soooooo I'm just going to output the variable: %r" % var
	
personal("Mitchell")
personal(10)