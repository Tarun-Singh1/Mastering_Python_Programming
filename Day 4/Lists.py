# Small Coding Challenge:
# Write a program that:
#
# Creates a list of 5 different cities.
#
# Adds one more city to the end of the list.
#
# Inserts another city at the beginning.
#
# Removes one city by name.
#
# Pops (removes) the last city from the list.
#
# Prints the final list and the length of the list.

cities = ["Dallas", "Austin", "Houston", "San Antonio", "Arlington"]

cities.append("Ohio")
print(cities)

cities.insert(0, 'Plano')
print(cities)

cities.remove('Arlington')
print(cities)

cities.pop(-1)
print(cities)

print(len(cities))
