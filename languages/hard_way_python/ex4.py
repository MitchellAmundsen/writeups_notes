teams = 32
field_capacity = 22
#the following are starting players in a single back set
linemen = 5
receivers = 4
quarterback = 1
running_back = 1
offense = linemen+receivers+quarterback+running_back
total_line = linemen * teams

print "There are", teams, "teams in the NFL."
print "Each team has", field_capacity, "starting players."
print "Half the team (", offense, " players) are on offense, the other on defense."
print "There is", teams * linemen, "starting offensive linemen in the NFL."



