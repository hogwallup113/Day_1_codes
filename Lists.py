# Create the list of epic programmers
epic_programmer_list = ["Tim Berners-Lee",
                         "Guido van Rossum",
                         "Linus Torvalds",
                         "Larry Page",
                         "Sergery Brin",]
# Print to console
print "Epic Programmers: " + epic_programmer_list[0]
print "Epic Programmers: " + epic_programmer_list[1]
print "Epic Programmers: " + epic_programmer_list[2]
print "Epic Programmers: " + epic_programmer_list[3]
print "Epic Programmers: " + epic_programmer_list[4]
# Add myself to the end of the list
epic_programmer_list.append("Josiah Fitch")
# Add this line to show myself in the console
print "An epic programmer: " + epic_programmer_list[5]

# Looping through each item in epic_programmer_list
for programmer in epic_programmer_list:
    #print the programmers name to console
    print "An epic programmer: " + programmer
