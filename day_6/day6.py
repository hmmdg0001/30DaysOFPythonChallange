    # Level 1
    # Create an empty tuple

emptytuple = ()

    # Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)

brothers = ("John", "Lennard", "Evan")
sisters = ("Julia", "Olivia")

    # Join brothers and sisters tuples and assign it to siblings

siblings = brothers + sisters

    # How many siblings do you have?

print(len(siblings))

    # Modify the siblings tuple and add the name of your father and mother and assign it to family_members

family_members = siblings + ("Ahr",)
print(family_members)

    # Level 2
    # Unpack siblings and parents from family_members

(John, Lennard, Evan, Julia, Olivia, Ahr) = family_members
print(John)
print(Lennard)
print(Evan)
print(Julia)
print(Olivia)

    # Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruits = ("Peach", "Pear", "Apple")
vegetables = ("Cabbage", "Carrot")
animal_products = ("Wool", "Honey")

food_stuff_tp = fruits + vegetables + animal_products

    # Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

    # Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

mid_index = len(food_stuff_tp) // 2
slice = food_stuff_tp[:mid_index] + food_stuff_tp[mid_index +1:]
print(slice)

    # Slice out the first three items and the last three items from food_stuff_lt list

slicefirsthree = food_stuff_lt[0:3]
slicelasthree = food_stuff_lt[4:7]
print(slicefirsthree)
print(slicelasthree)

    # Delete the food_stuff_tp tuple completely

del food_stuff_tp

    # Check if an item exists in tuple:
    # Check if 'Estonia' is a nordic country
    # Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

checkone = 'Estonia' in nordic_countries
print(checkone)

checktwo = 'Iceland' in nordic_countries
print(checktwo)