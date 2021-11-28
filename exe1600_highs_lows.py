# Extraindo dados de um arquivo CSV e exibindo com Matplotlib

import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Obtém as datas e as temperaturas máximas e mínimas do arquivo
# filename  = 'sitka_weather_07-2014.csv'
# filename  = 'sitka_weather_2014.csv'
filename  = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Obtém as datas e as temperaturas máximas e mínimas do arquivo
    dates, highs_f, lows_f = [], [], []
    for row in reader:
        try:
            # current_date = datetime.strptime(row[0], "%Y-%m-%d")
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high_f = int(row[1])
            low_f = int(row[3])

        except ValueError:
            print(current_date, 'missing data')
        
        else:
            dates.append(current_date)
            highs_f.append(high_f)
            lows_f.append(low_f)
            


    # Converte as temperaturas para Celsius
    highs_c = [int(((f - 32) / 1.8)) for f in highs_f]
    lows_c = [int(((f - 32) / 1.8)) for f in lows_f]

    
    # Faz a plotagem dos dados em Fahrenheit
    fig = plt.figure(dpi=128, figsize=(10,6))
    plt.plot(dates, highs_f, c='red', alpha=0.5)
    plt.plot(dates, lows_f, c='blue', alpha=0.5)

    # Sombreando um gráfico
    plt.fill_between(dates, highs_f, lows_f, facecolor='blue', alpha=0.1)

    # Temperaturas em Celsius
    plt.plot(dates, highs_c, c='green')
    plt.plot(dates, lows_c, c='black')
    # Sombreando um gráfico
    plt.fill_between(dates, highs_c, lows_c, facecolor='yellow', alpha=0.1)

    # Formata o gráfico
    title = 'Daily high and low temperatures - 2014\nDeath Valley, CA'
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()
