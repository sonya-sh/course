import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import sys

sys.stdout.reconfigure(encoding='utf-8')


def dr(rates_list):
    rates = [float(str(rates_list[i-1])[4: -5]) for i in range(len(rates_list)-1, 3, -3)]
    dates = [str(rates_list[i-2])[6: -5] for i in range(len(rates_list)-1, 3, -3)]
    return dates, rates


def main():

    page = requests.get('http://mfd.ru/currency/?currency=USD')
    soup = BeautifulSoup(page.text, 'html.parser')
    rates = soup.find('table', {'class': 'mfd-table mfd-currency-table'})
    rates_list = rates.find_all('td')
    print(rates_list)
    dates, rates = dr(rates_list)
    print(dr(rates_list))

    x, ax = plt.subplots()
    ax.xaxis.set_major_locator(MaxNLocator(8))
    ax.grid(True)

    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Rate', fontsize=12)
    ax.plot(dates, rates)

    plt.show()


main()
