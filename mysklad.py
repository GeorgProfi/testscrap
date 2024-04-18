import json

import requests


headers = {'Content-Type': 'application/json','Authorization': 'Bearer 4cb41a30b5b7435e68e4ffd0667c20d3e59ef6e2'}

url_categories = 'https://api.moysklad.ru/api/remap/1.2/entity/productfolder'
url_products = 'https://api.moysklad.ru/api/remap/1.2/entity/product'


def get_categories(url):
    response = requests.get(url, headers=headers).json(),
    for category in response[0]['rows']:
        print('категория:',category['id'],category['name'])
        get_products(category['meta']['href'])
    #return json.dumps(response, indent=2)


def get_products( folder):
    response = requests.get(f'https://api.moysklad.ru/api/remap/1.2/entity/product', headers=headers).json(),
    for product in response[0]['rows']:
        if product['productFolder']['meta']['href'] == folder:
            print('товар',product['name'], product['id'])
get_categories(url_categories)