#imports argv module
from sys import argv

#take filename as an argument then assigns it to the txt variable
script, filename = argv
txt = open(filename)

#prints the text document
print "Here's your file %r:" % filename
print txt.read()
txt.close()

#takes the filename again as an input, assigns the file to a variable, then prints again
print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
txt_again.close()