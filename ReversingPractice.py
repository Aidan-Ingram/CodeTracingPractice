name = input("Enter your name: ")
length = len(name)
n = length
var = ''

#What is this type of indexing doing, and what is it called?
print(name[::-1])

#Does this function output the same thing as the one above?
namelist = []
namelist.append(name)
namelist.reverse()
print(namelist)

#Do you know why it outputs the way it does?
