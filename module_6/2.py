import requests
import time
from threading import Thread


def get_html(link):
    response = requests.get(link)
    print(link, len(response.text))


links = ['https://yandex.ru', 'https://github.com', 'https://www.google.ru',
             'https://rambler.ru', 'https://www.flaticon.com']
threads = [Thread(target=get_html, args=[links[i]]) for i in range(5)]

t_seq = time.time()
for i in range(5):
    print(get_html(links[i]))
print(f'Время последовательного выполнения: {time.time() - t_seq}')

t_par = time.time()
for start in threads:
    start.start()
for j in threads:
    j.join()
print(f'Время параллельного выполнения: {time.time() - t_par}')
