# Processando uma resposta de API

import requests
import plotly.offline as py
import plotly.graph_objs as go

py.init_notebook_mode(connected=True)

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

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

trace = go.Scatter(x = names, 
                   y = stars,
                   mode='bars')

data = [trace]

py.iplot(data)
