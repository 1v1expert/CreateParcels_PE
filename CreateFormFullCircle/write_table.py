import csv


class gen_html():
    def __init__(self):
        self.style = '<style>' \
                     '.table_dark {' \
                     'font-family: ' '"Lucida Sans Unicode", "Lucida Grande", Sans-Serif;' \
                     'font-size: 14px;' \
                     'font-color: black;' \
                     'width: 640px;' \
                     'text-align: left;' \
                     'border-collapse: collapse;' \
                     'background: white;' \
                     'margin: 10px;' \
                     '}' \
                     '.table_dark th {' \
                     'color: black;' \
                     'border-bottom: 1px solid black;' \
                     'padding: 12px 17px;' \
                     'text-align: center;'\
                     '}' \
                     '.table_dark td {' \
                     'color: dark;' \
                     'border-bottom: 1px solid black;' \
                     'border-right:1px solid black;' \
                     'padding: 7px 17px;' \
                     '}' \
                     '.table_dark tr:last-child td {' \
                     'border-bottom: none;' \
                     '}' \
                     '.table_dark td:last-child {' \
                     'border-right: none;' \
                     '}' \
                     '.table_dark tr:hover td {' \
                     'text-decoration: underline;' \
                     '}' \
                     '</style>'
        self.table = '<head><meta charset="UTF-8"></head>' \
                     '<tr>' \
                     '<th>PULSE-EXPRESS</th>' \
                     '<th>order_id</th>' \
                     '<th>barcode</th>' \
                     '<th>Sign(QR-code)</th>' \
                     '<th>Комментарий</th>' \
                     '</tr>'
    
    def save_in(self):
        self.countainer = self.style + '<table class="table_dark">' + self.table + '</table>'
        with open("Phase.html", 'w') as f_html:
            f_html.write(self.countainer)
    
    def csv_dict_reader(self, file_obj):
        reader = csv.DictReader(file_obj, delimiter=';')
        for line in reader:
            barcode = line["barcode"]
            order_id = line['order_id']
            pincode = line['pincode']
            telephone = line['telephone']
            code128 = '<img alt="Barcoded value' + order_id + '"src="http://bwipjs-api.metafloor.com/?bcid=code128&text=' + order_id + '&includetext">'
            con_sign = 'A2' + telephone + '%26' + pincode
            qrcode = '<img alt="Barcoded value' + con_sign + '"src="https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=' + con_sign + '"'
            
            self.table = self.table + '<tr><td>Order_id = ' + order_id + ',<br>Barcode = ' + barcode + ',<br>PinCode = ' + pincode + ',\nSign = ' + con_sign + '</td><td>' + code128 + '</td><td>' + '<img alt="Barcoded value' + barcode + '"src="http://bwipjs-api.metafloor.com/?bcid=code128&text=' + barcode + '&includetext"></td><td>' + qrcode + '</td><td></td></tr>'
            print('Succes')

if __name__ == "__main__":
    g = gen_html()
    with open("List_gen_field_test.csv") as f_obj:
        g.csv_dict_reader(f_obj)
    g.save_in()