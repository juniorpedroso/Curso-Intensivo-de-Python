# Note: I run > set PYTHONIOENCODING=utf-8 before executing python
import requests

# URL with wunderground weather information for a specific date:
date = '2021-11-27'
# url = 'https://www.wunderground.com/history/daily/sd/khartoum/HSSS/date/' + date
url = 'https://www.wunderground.com/history/daily/br/bauru/SBBU' + date
# https://www.wunderground.com/history/daily/br/bauru/SBBU
r = requests.get(url)

# Write a file to check if the tables ar being retrieved:
with open('test.html', 'wb') as testfile:
    testfile.write(r.text.encode('utf-8'))