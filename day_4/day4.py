    # Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
tstr = "Thirty "
dstr = "Days "
ostr = "Of "
pstr = "Python"

complete = tstr + dstr + ostr + pstr

print(complete)

    # Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

cstr = "Coding "
fstr = "For "
astr = "All"

complete2= cstr + fstr +astr

print(complete2)

    # Declare a variable named company and assign it to an initial value "Coding For All".

company = complete2

print(company)

    # Print the variable company using print().

print(company)

    # Print the length of the company string using len() method and print().

print(len(company))

    # Change all the characters to uppercase letters using upper() method.

print(company.upper())

    # Change all the characters to lowercase letters using lower() method.

print(company.lower())

    # Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

print(company.capitalize())
print(company.title())
print(company.swapcase())

    # Cut(slice) out the first word of Coding For All string.

cutslice = company[-6:18]
print("cutslice " + cutslice)

    # Check if Coding For All string contains a word Coding using the method index, find or other methods.

print("Check")

if "Coding" in company:
    print("Exists")
else:
    print("Doesn't exist")

    # Replace the word coding in the string 'Coding For All' to Python.

print(company.replace('Coding', 'Python'))

    # Change "Python for Everyone" to "Python for All" using the replace method or other methods.

pfe = "Python for Everyone"
print("------")
print(pfe.replace("Python for Everyone", "Python for All"))

    # Split the string 'Coding For All' using space as the separator (split()) .

print(company.split())

    # "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

splitcompanys = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(splitcompanys.split())

    # What is the character at index 0 in the string Coding For All.

print("----")
print(company[0])

    # What character is at index 10 in "Coding For All" string.

print(" ... ")
print("Index 10 is: " + company[10])

    # Create an acronym or an abbreviation for the name 'Python For Everyone'.

splitpfe = pfe.split()
lpfe = [word[0].upper() for word in splitpfe]
acr = ''.join(lpfe)
print(acr)

    # Create an acronym or an abbreviation for the name 'Coding For All'.

splitcompany = company.split()
lspc = [word[0].upper() for word in splitcompany]
acrlspc = ''.join(lspc)
print(acrlspc)

    # Use index to determine the position of the first occurrence of C in Coding For All.

print(" ... ")
print(company.index("C"))

    # Use index to determine the position of the first occurrence of F in Coding For All.

print(" --- ")
print(company.index("F"))

    # Use rfind to determine the position of the last occurrence of l in Coding For All People.

cfa = "Coding For All People"
print(cfa.rfind("l"))

    # Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print(" --- ")
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index("because"))

    # Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print(sentence.rfind("because"))

    # Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

print(" --- ")
slicesentence =  slice(30,54)
print(sentence[slicesentence])

    # Does 'Coding For All' start with a substring Coding?

companyC = company.startswith("Coding")
print(companyC)

    # Does 'Coding For All' end with a substring coding?

endcompany = company.endswith("coding")
print(endcompany)

    # '   Coding For All      '  , remove the left and right trailing spaces in the given string.

spaces = '   Coding For All      '
#print(spaces)
print(spaces.strip())

    # Which one of the following variables return True when we use the method isidentifier():
    # 30DaysOfPython
    # thirty_days_of_python

print(" --- ")
i1 = "30DaysOfPython"
i2 = "thirty_days_of_python"
print(i1.isidentifier())
print(i2.isidentifier())

    # The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.

print(" --- ")
pylibraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '# '.join(pylibraries)
print(result)

    # Use the new line escape sequence to separate the following sentences
    # I am enjoying this challenge. I just wonder what is next.

print(" --- ")
print("I am enjoying this challenge.\nI just wonder what is next.")

    # Use a tab escape sequence to write the following lines
    # Name      Age     Country   City
    # Asabeneh  250     Finland   Helsinki

print(" --- ")
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

    # Use the string formatting method to display the following:

radius = 10
area = 3.14 * radius ** 2
print("The are of the circle with raidus " + str(10) + " is " + str(area) + " meters square.")

    # Make the following using string formatting methods:

print("8 + 6 = 14\n8 - 6 = 2\n8 * 6 = 48\n8 / 6 = 1.33\n8 % 6 = 2\n8 // 6 = 1\n8 ** 6 = 262144")