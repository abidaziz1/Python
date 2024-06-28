txt= "I have {an:.2f} Dollars!"
print(txt.format(an=500))

print("%10s"% ('Abid', ))
print("%-20s"% ('Abid', ))
print("%.5s"% ('jdhjehsjhfj',))
print("The {0} of 100 is {1:b}" .format("binary",100))
print("The {0} of 100 is {1:o}" .format("octal",100))

#Using a dictionary for string formatting
intro = "My name is {f_name} {m_name} {l_name} AKA the {aka}."
full_name = {
    'f_name': 'Abid',
    'm_name': 'Aziz',
    'l_name': 'Nihal',
    'aka': 'Iron man' 
}
print(intro.format(**full_name))

#with a list
input = [100.3743, 72.8378, 78.739823,67.2839]
output = ['{:.2f}'.format(elements) for elements in input]
print(output)