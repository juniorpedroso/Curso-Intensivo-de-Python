# Processando uma resposta de API

import requests

# Faz uma chamada de API e armazena a resposta
url = 'https://api.github.com/search/repositories?\
q=language:python&sorts=stars'
r = requests.get(url)
print('Status code:', r.status_code)

# Armazena a resposta da API em uma variável
response_dict = r.json()
print('Total repositories:', response_dict['total_count'])

# Explora informações sobre os repositórios
repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))

# Analisa vários repositórios
print('\nSelected information about each repository:')
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Reposistory:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])


