# import math
# a = math.ceil(4.3)
# print(a)
# b = math.floor(4.9)
# print(b)

# a = math.fabs(-100)
# b = math.fabs(100)
# print(int(a))
# print(int(b))

# a = math.sqrt(256)
# b = math.sqrt(330)
# print(a)
# print(int(b))
# str = "here I am"
# a = str.count("e")
# a = str.capitalize()
# a = str.count("e")
# a = str.find("r")
# str = " "
# iter = ( "I", "am", "awesome")
# a = str.join(iter)
# print(a)


file = open("countries_and_capitals.txt", "w+")
countries_and_capitals = {"Poland":"Warsaw", "Germany":"Berlin", "Ireland":"Dublin"}

for country, capital in countries_and_capitals.items():
    file.write(country + "-" + capital + "\n" )
file.close()
#######################
file = open("countries_and_capitals.txt")
for line in file.readlines():
    print(line.strip())
