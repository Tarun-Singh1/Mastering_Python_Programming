# 🧩 Coding Challenge: Type Conversion
# 🎯 Problem:
# Write a program that takes these variables:
#
# temperature_celsius as a float (e.g., 37.5)
#
# city_name as a string
#
# is_hot as a boolean
#
# Then:
#
# Convert temperature_celsius to an integer and print it.
#
# Print a sentence using string concatenation like:
#
# vbnet
# Copy
# Edit
# It is 37°C in Delhi. Is it hot? True
# (Make sure you convert non-string types when needed!)
#
# Print the data type of all variables.



temperature_celsius = 37.5
city_name = "Hisar"
is_hot = True

integer_temperature = int(temperature_celsius)


print(integer_temperature)
print("It is " + str(integer_temperature) + "°C in " + city_name + ". Is it hot? " + str(is_hot))
print(f"It is {integer_temperature}°C in {city_name}. Is it hot? {is_hot}")
print(type(temperature_celsius))
print(type(city_name))
print(type(is_hot))







