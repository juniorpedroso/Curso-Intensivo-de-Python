# Extraindo dados de um arquivo CSV e exibindo com Matplotlib
import csv
from matplotlib import pyplot as plt
from exe1600_country_codes import get_country_code

# Obtém as datas e as temperaturas máximas e mínimas do arquivo
# filename  = 'sitka_weather_07-2014.csv'
# filename  = 'sitka_weather_2014.csv'
filename = 'data/taxa_natalidade.csv'


with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    header_row = next(reader)
    header_row = next(reader)
    header_row = next(reader)
    header_row = next(reader)
    # print(header_row)

    dicts_paises = []
    dict_paises = {}
    for row in reader:
        dict_paises['Country Name'] = row[0]
        dict_paises['Code'] = get_country_code(row[0])
        dicts_paises.append((dict_paises))

    # for pais in dicts_paises:
    #     print(f'Country name: {pais["Country Name"]} Code: {pais["Code"]}')
    print(dicts_paises)

# for country, code in dict_paises.items():
#     print(country, code)

    # for produto, preco in lanchonete.items():
    #     print(produto, preco)
