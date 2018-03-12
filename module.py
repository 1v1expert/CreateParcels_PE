# -*- coding: utf-8 -*-
import json
import requests

url = "https://dev.api.pulse.itcanfly.org/v1/requests/"
HDRS = {'Content-type': 'application/json',
        'Encoding': 'utf-8'}
headers = HDRS.copy()

payload = {
    "internal_number": "691",
    "rtype": "Последняя миля",
    "responsible_phone":"+79852296756",
    "responsible_email": "v.sazonov@pulseexpress.ru",
    "parcels": [{
        "order_id": "fintest346",
        "weight": 860,
        "length": 20,
        "width": 130,
        "height": 11,
        "barcodes": ["381110346"],
        "point": "a593bd26-52b4-40af-a4dc-88b0ee5d5355",
        "consignor": "Vax-Vax",
        "receiver": {
            "phone": "+79852296756",
            "email": "1v1expert@gmail.com"
        },
        "cod": 0,
        "declared_price": 0,
        "partner_service_fee": 0
    }]}
#headers['Authorization'] = 'Token a7e0f929-e6c8-4b46-adae-b5ab05fb5074'
headers['Authorization'] = 'Token 9ef69509-9373-4742-8c57-08dfdcbbf9dc'


response = requests.post(url, verify=False, data=json.dumps(payload), headers=headers)
print(response.json())
