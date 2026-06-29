    # Create an empty dictionary called dog

dog = {}

    # Add name, color, breed, legs, age to the dog dictionary

dog['name'] = 'Luna'
dog['color'] = 'white'
dog['breed'] = 'Akita'
dog['age'] = '2'
print(dog)

    # Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary


student = {'first_name':'John', 'last_name':'Doe', 'gender':'male','age':'20','martial_status':'married','skills':'cooking','country':'Sweden','city':'Stockholm'}
print(student)

    # Get the length of the student dictionary

print(len(student))

    # Get the value of skills and check the data type, it should be a list

print(student['skills'])
print(type(student['skills']))

    # Modify the skills values by adding one or two skills

student['skills'] = 'cooking, programming, swimming'
print(student['skills'])

    # Get the dictionary keys as a list

diclist = student.keys()
print(diclist)

    # Get the dictionary values as a list

values = student.values()
print(values)

    # Change the dictionary to a list of tuples using items() method

print(student.items())

    # Delete one of the items in the dictionary

del student['gender']
print(student)

    # Delete one of the dictionaries

del student