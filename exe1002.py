filename = 'exe1001.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

print()

for line in lines:
    print(line.replace('Python', 'C').strip())
    
