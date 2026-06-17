# day_2 : 30 Days of python programming  -- Exercise: Level 1

first_name = "Henrique"
last_name =  "Marinho"
full_name = "Henrique Marinho"
country = "Sweden"
city = "Stockholm"
age = "21"
year = "2001"
is_married = False
is_true = True
is_light_on = True


f_name, l_name, c, a, is_m = 'John', 'Dee', 'London', '40', False

print(first_name)
print(last_name)
print(full_name)
print(country)
print(city)
print(age)
print(year)
print(is_married)
print(is_true)
print(is_light_on)
print(f_name, l_name, c, a, is_m)

## Level 2

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print(len(first_name))
print(len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(total)
print(diff)
print(product)
print(remainder)
print(exp)
print(floor_division)

import math

radius = 30

area_of_circle = math.pi * radius ** 2
circum_of_circle =  2 * math.pi * radius


print(area_of_circle)
print(circum_of_circle)

print("What is the radius of your circle?")
answer = input()
area_user = math.pi * int(answer) ** 2
print("The radius is: " + str(area_user))


print("What is your first name?")
fn = input()
print("What is your last name?")
ln = input()
print("What is your country?")
cy = input()
print("What is your age?")
ae = input()

print(fn + ln + cy + ae)

print(help('keywords'))