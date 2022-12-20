import pandas as pd
import numpy as np
from transliterate import translit

def make_urls():
    data = pd.read_csv('/Users/user/Desktop/Work/Parsing/selenium_python_scraper_reviews_yandexmap/b.csv', sep = ";")
    reg = pd.read_csv('/Users/user/Desktop/Work/Parsing/selenium_python_scraper_reviews_yandexmap/Book1.csv', sep = ";")
    data = data[['Город / Нас.пункт', 'GPS. Широта', 'GPS. Долгота']]
    data = pd.merge(data, reg, how ='left', left_on = 'Город / Нас.пункт', right_on = 'город')
    print(data.info())
    data.dropna(inplace=True)
    data = data.reset_index()
    data['номер'] = data['номер'].apply(np.int64)
    data['Город / Нас.пункт'] = data['Город / Нас.пункт'].str.replace('-', '_')
    data['Город / Нас.пункт'] = data['Город / Нас.пункт'].str.lower()
    store_names = ["DNS", "m_video", "megafon", "mts", "svyaznoy"]
    data['links'] = np.nan
    for i in range(len(data)):
        city = translit(data['Город / Нас.пункт'][i], language_code='ru', reversed=True)
        print(city)
        longitude = data['GPS. Широта'][i]
        latitude = data['GPS. Долгота'][i]
        number = data['номер'][i]
        link_list = []
        for store_name in store_names:
            link_list.append(f'https://yandex.ru/maps/{number}/{city}/search/{store_name}/?ll={latitude},{longitude}&rspn=1&spn=0.003,0.003')

        data['links'][i]=link_list
        
    data.to_csv('final.csv')
    return data


print(make_urls())