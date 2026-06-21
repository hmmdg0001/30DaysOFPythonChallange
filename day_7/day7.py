    # sets

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
    
    # Level 1
    # Find the length of the set it_companies

print(len(it_companies))

    # Add 'Twitter' to it_companies

it_companies.add('Twitter')
print(it_companies)

    # Insert multiple IT companies at once to the set it_companies

it_companies.update(["Nvidia", "Dell", "Intel", "Cisco"])
print(it_companies)

    # Remove one of the companies from the set it_companies

it_companies.remove("Nvidia")
print(it_companies)

    # What is the difference between remove and discard

it_companies.remove("Dell") # If Dell doesn't exist it will show a error.
print(it_companies)
it_companies.discard("Dell") # If Dell doesn't exist it won't show a error.
print(it_companies)

    # Level 2
    # Join A and B

joinab = A.union(B)
print(joinab)

    # Find A intersection B

intersection = A.intersection(B)
print(intersection)

    # Is A subset of B

subset = A.issubset(B)
print(subset)

    # Are A and B disjoint sets

disjoint = A.isdisjoint(B)
print(disjoint)

    # Join A with B and B with A

joinabt = A.union(B)
joinba = B.union(A)
print(joinabt)
print(joinba)

    # What is the symmetric difference between A and B

symmetric = A.symmetric_difference(B)
print(symmetric)

    # Delete the sets completely

del A
del B

    # Level 3
    # Convert the ages to a set and compare the length of the list and the set, which one is bigger?

convertsetlist = set(age)
print(len(convertsetlist))
print(len(age))

    # Explain the difference between the following data types: string, list, tuple and set

print("String are ordered sequences of characters that are immutable")
print("Lists are ordered mutable collections that allow duplicates")
print("Tuples are ordered immutable collections that allow duplicates")
print("Sets are unordered mutable collections that store only unique elements")

    # I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

sentence = "I am a teacher and I love to inspire and teach people"
splitsentence = sentence.split()
unique_words = set(splitsentence)
unique_count = len(unique_words)

print(unique_count)