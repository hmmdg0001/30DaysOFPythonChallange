age = int(21)
height = float(True)
complex = 32 + 2j

print("Enter base: ")
base = input()
print("Enter height: ")
height = input()
area_triangle = 0.5 * int(base) * int(height)
print("The area of the triangle is: " + str(area_triangle))

print(type((age)))
print(type(height))
print(type(complex))

print("Enter side a: ")
side_a = input()
print("Enter side b: ")
side_b = input()
print("Enter side c: ")
side_c = input()

perimeter = int(side_a) + int(side_b) + int(side_c)
print("The perimeter of the triangle is: " + str(perimeter))

print("Enter lenght of a rectangle: ")
lenght_r = input()
print("Enter width of a rectangle: ")
width_r = input()

area_r = int(lenght_r) * int(width_r)
print("The area is: " + str(area_r))

perimeter_r = 2 * (int(lenght_r) + int(width_r))
print("The perimeter is: " + str(perimeter_r))

m = 2
b = -2

slope = m
y_intercept = b
x_intercept = -b / m

print("Slope: " + str(m))
print("y-intercept: " + str(y_intercept))
print("x-intercept: " + str(x_intercept))

import math

x1, y1 = 2, 2
x2, y2 = 6, 10

slope2 = (y2 - y1) / (x2 - x1)

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"Point 1: ({x1}, {y1})")
print(f"Point 2: ({x2}, {y2})")
print(f"Slope (m): {slope2}")
print(f"Euclidean Distance (d): {distance:.4f} (or exactly sqrt({(x2-x1)**2 + (y2-y1)**2}))")

slopes_compare = slope == slope2
print(slopes_compare)

x1 = -3
y = x1**2 + 6 * x1 + 9

print(y)

lenp = len('python')
lend = len('dragon')
comp = lenp > lend
print(comp)

print('I hope this crouse is not full of jargon.', 'p' in 'jargon' )


ppython = 'python'
pdragon = 'dragon'
text = 'on'

print(text not in ppython and pdragon)

ppython = 'python'
f = float(len(ppython))
s = str(len(ppython))

print('Float :' + str(f) + ' String: ' + str(s))

numeven = int(input("Enter a number: "))

if numeven % 2 == 0:
    print("Even")
else: 
    print("not even")

fd = 7 // 3

if fd == 2.7:
    print('equal')
else:
    print('not equal')

if '10' == 10:  
    print('equal')
else:
    print('not equal')


nint = int(9.8)

if nint == 10:
    print('equal')
else:
    print('not equal')

hours = int(input('Enter hours: '))
rphours = int(input('Enter rate per hour: '))

weekly = hours * rphours

print('Your weekly income is: ' + str(weekly))


agelived = int(input('Enter numbers of years you have lived: '))
secondconversion =  3.15576e+7

print('You lived for ' + str(secondconversion) + 'seconds.')


for n in range(1, 6):
    val1 = n
    val2 = n ** 0
    val3 = n ** 1
    val4 = n ** 2
    val5 = n ** 3
    
    print(f"{val1:<5}{val2:<5}{val3:<5}{val4:<5}{val5:<5}")