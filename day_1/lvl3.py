# day_1 -- Exercise: Level 3

import math


print("Int: " + str(type(30)))
print("Float: " + str(type(4.7)))
print("Complex: " + str(type(34 - 20j)))
print("String: " + str(type('Python')))
print("List: " + str(type([3, 10, 13])))
print("Boolean: " + str(type(3 == 4)))
print("Boolean: " + str(type( 4 == 4)))
print("Tuple: " + str(type((30.2, 10.3, 2.3))))
print("Set: " + str(type({30.2, 10.3, 2.3})))
print("Dictionary: " + str(type({'name:' : 'Python'})))

 # Finding a Euclidean Distance

euclidean1 = [2]
euclidean2 = [3]

euclidean3 = [10]
euclidean4 = [8]

distance1 = math.dist(euclidean1, euclidean2)
distance2 = math.dist(euclidean3, euclidean4)
print("Euclidean distance from vector 1 is: " + str(distance1))
print("Euclidean distance from vector 2 is: " + str(distance2))


