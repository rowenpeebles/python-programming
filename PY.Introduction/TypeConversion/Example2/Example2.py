# Example2: Addition of string and integer using explicit conversion

num_string = "12"
num_integer = 23

print("Data type of string before Type Casting:", type(num_string))
num_string = int(num_string)
print("Data type of string after Type Casting:", type(num_string))

num_sum = num_integer + num_string
print("Sum:", num_sum)
print("Data type of num_sum:", type(num_sum))
