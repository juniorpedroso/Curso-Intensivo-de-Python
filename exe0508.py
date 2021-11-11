current_users = ['admin', 'john', 'pedro', 'carlos']
new_users = ['célio', 'Vanda', 'john', 'hugo', 'carlos']

if not current_users:
    print('Precisamos encontrar alguns usuários!')
for current_user in new_users:
    if current_user in current_users:
        print(f'{current_user.title()} já foi usado, forneça outro!')
    else:
        print(f'{current_user.title()} está disponível.')
