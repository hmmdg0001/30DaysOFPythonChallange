    # Declare an empty list

empylist = []

    # Declare a list with more than 5 items

list5 = ['item1', 'item2', 'item3', 'item4', 'item5']

    # Find the length of your list

print(len(list5))

    # Get the first item, the middle item and the last item of the list

firsitem = list5[0]
middleitem = list5[2]
lastitem = list5[4]

print(firsitem + middleitem + lastitem)

    # Declare a list called mixed_data_types, put your(name, age, height, marital status, address)

mixed_data_types = ['John', '21', '1,86', 'single', 'Real address nº20']

    # Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

    # Print the list using print()

print(it_companies)

    # Print the number of companies in the list

print(len(it_companies))

    # Print the first, middle and last company

print(" --- ")
companyone, companytwo, companythree, companyfour, companyfive, companysix, companyseven = it_companies
print(companyone + companyfour + companyseven)

    # Print the list after modifying one of the companies

print(" --- ")
it_companies.remove('Facebook')
print(it_companies)

    # Add an IT company to it_companies

print(" --- ")
it_companies.insert(0, 'Github')
print(it_companies)

    # Insert an IT company in the middle of the companies list

print(" --- ")
it_companies.insert(4, "Twistag")
print(it_companies)

    # Change one of the it_companies names to uppercase (IBM excluded!)

print(" --- ")
it_companies[0] = "Github".upper()
print(it_companies)

    # Join the it_companies with a string '#;  '

it_cstring = ["#; "]
joincompanies = it_companies + it_cstring
print(joincompanies)

    # Check if a certain company exists in the it_companies list.

print(" --- ")
does_exist = "IBM" in it_companies
print(does_exist)

    # Sort the list using sort() method

print(" --- ")
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)

    # Reverse the list in descending order using reverse() method

print(" --- ")
it_companies.reverse()
print(it_companies)

    # Slice out the first 3 companies from the list

print(" --- ")
sliceoneandtree = it_companies[0:3]
print(sliceoneandtree)

    # Slice out the last 3 companies from the list

print(" --- ")
slicelastree = it_companies[5:8]
print(slicelastree)

    # Slice out the middle IT company or companies from the list

print(" --- ")
slicemiddle = it_companies[4]
print(slicemiddle)

    # Remove the first IT company from the list

print(" --- ")
del it_companies[1]
print(it_companies)

    # Remove the middle IT company or companies from the list

print(" --- ")
del it_companies[3]
print(it_companies)

    # Remove the last IT company from the list

print(" --- ")
del it_companies[5]
print(it_companies)

    # Remove all IT companies from the list

print(" --- ")
del it_companies[0:5]
print(it_companies)

    # Destroy the IT companies list

print(" --- ")
del it_companies[:]
print(it_companies)

    # Join the following lists:

print(" --- ")
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
joinlists = front_end + back_end
print(joinlists)

    # After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

print(" --- ")
full_stack = joinlists.copy()
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, "Python")
full_stack.insert(redux_index + 2, "SQL")
print(full_stack)

    # Exercises: Level 2
    # The following is a list of 10 students ages:

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

    # Sort the list and find the min and max age

ages.sort()
age_min = min(ages)
age_max = max(ages)
print(age_min)
print(age_max)

    # Add the min age and the max age again to the list

mininsert = ages.insert(0, age_min)
maxinsert = ages.insert(10, age_max)
print(ages)

    # Find the median age (one middle item or two middle items divided by two)

ages.sort()
m = len(ages)

if m % 2 == 0:
    res = (ages[m//2 - 1] + ages[m//2])  /2
else: 
    res = ages[m//2]

print(res)

    # Find the average age (sum of all items divided by their number )

avg = sum(ages) / len(ages)
print(avg)

    # Find the range of the ages (max minus min)

max_age = max(ages)
min_age = min(ages)
age_range = max_age - min_age

print(age_range)

    # Compare the value of (min - average) and (max - average), use abs() method

min_distance = abs(min_age - avg)
max_distance = abs(max_age - avg)

print("min to avg: " + str(min_distance))
print("min to avg: " + str(max_distance))

    # Find the middle country(ies) in the countries list

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];

middlecountrie = len(countries) //2
print(countries[middlecountrie])

    # Divide the countries list into two equal lists if it is even if not one more country for the first half.

split = (len(countries) + 1) // 2

first_half = countries[:split]
second_half = countries[split:]

print(first_half)
print(second_half)

    # ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

countriestwo = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

china, russia, usa, *scandic_countries = countriestwo
print(" --------------- ")
print(china)
print(russia)
print(usa)
print(scandic_countries)