# -*- coding: utf-8 -*-
import json
import requests
import settings

POINTS = {
    '9997': "d93a80ff-5407-49c4-b0bc-eafab8bac5d7",
    '9996': "a593bd26-52b4-40af-a4dc-88b0ee5d5355",
    '217': "7cc6effb-2347-457d-941d-aad91cdd461e",
    '219': "e11acf1e-a386-4c89-809c-48195ea84874",
    '229': "84d5cad7-3cf6-40ac-95a0-2619cfbed6f4",
    '230': "bce60339-cde8-4f80-b04e-ecfbd018bea3",
    '234': "7d3ae8be-7b37-4817-8ecf-1723d87f649e",
    '238': "e09298f0-a3ff-4dfc-a9a0-76dd1b6379e7",
    '239': "b5aa8a33-cca2-4d50-83e3-cd4a6aae5d62"
    
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
