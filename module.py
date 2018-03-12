# -*- coding: utf-8 -*-
import json
import requests
import urllib3
import settings

urllib3.disable_warnings()

POINTS = {
    '9997': "",
    '9996': "a593bd26-52b4-40af-a4dc-88b0ee5d5355",
}

def create_range(count, number, test, point):
    for i in range(1, count + 1):
        order_id = 'field_test' + str(number + i)
        barcodes = str(number + 1000000 + i)
        
        if test == ('yes' or 'да'):
            token = settings.TOKEN_test
            url = settings.URL_test
        else:
            token = settings.TOKEN_live
            url = settings.URL_live
            
        phone = '+79852296756'
        email = '1v1expert@gmail.com'

        response = " \n" + str(create_parcel(order_id, barcodes, phone, email, point, token, url))
        line = '\nAnounce ' + order_id + ' ' + barcodes + ' ' + point + response + '\n'
        with open('record.log', 'a') as file:
            file.write(line)
            
def create_parcel(order_id, barcodes, phone, email, point, token, url):
    HDRS = {'Content-type': 'application/json',
            'Encoding': 'utf-8'}
    headers = HDRS.copy()

    payload = {
        "internal_number": "691",
        "rtype": "Последняя миля",
        "responsible_phone": phone,
        "responsible_email": "v.sazonov@pulseexpress.ru",
        "parcels": [{
            "order_id": order_id,
            "weight": 860,
            "length": 20,
            "width": 130,
            "height": 11,
            "barcodes": [barcodes],
            "point": POINTS[point],
            "consignor": "Vax-Vax",
            "receiver": {
                "phone": phone,
                "email": email
            },
            "cod": 0,
            "declared_price": 0,
            "partner_service_fee": 0
        }
        ]
    }
    headers['Authorization'] = token
    response = requests.post(url, verify=False, data=json.dumps(payload), headers=headers)
    return response.json()

if __name__=='__main__':
    point = ""
    while point != 'quit':
        point = input('quit/Точка №: ')
        if point != 'quit':
            count = input('Количество посылок: ')
            number = input('Номер прежней посылки: ')
            test = input('Тестовый ? Yes/No: ')
            create_range(int(count), int(number), test, point)
            print(point, count, test)
