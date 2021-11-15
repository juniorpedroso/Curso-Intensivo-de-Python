file_name = 'exe1003_guest.txt'

guest = input('Nome do convidado: ')

with open(file_name, 'a') as file_object:
    file_object.write(f'{guest}\n')

with open(file_name) as file_object:
    print(file_object.read())

