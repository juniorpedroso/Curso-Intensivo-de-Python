filename = 'exe1001.txt'

with open(filename) as file_object:
    texto = file_object.read()
    print(texto)

print()
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

print()
meu_texto = ''
for line in lines:
    meu_texto += line.strip()
print(meu_texto)
