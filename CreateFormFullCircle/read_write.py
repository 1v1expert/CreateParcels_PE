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
		self.table =  '<tr>' \
					  '<th>PULSE-EXPRESS</th>' \
					  '<th>order_id(code128)</th>' \
					  '<th>order_id(code39)</th>' \
					  '<th>order_id(Data_Matrix)</th>' \
					  '<th>order_id(EAN128)</th>' \
					  '<th>barcode(EAN13)</th>' \
					  '<th>barcode(code128)</th>' \
					  '<th>Sign(QR-code)</th>' \
					  '</tr>'

	def save_in(self):
		self.countainer = self.style + '<table class="table_dark">' + self.table + '</table>'
		with open("index.html", 'w') as f_html:
			f_html.write(self.countainer)
			
	def csv_dict_reader(self, file_obj):
		reader = csv.DictReader(file_obj, delimiter=';')
		for line in reader:
			barcode = line["barcode"]
			order_id = line['order_id']
			pincode = line['pincode']
			telephone = line['telephone']
			code128 = '<img alt="Barcoded value' + order_id + '"src="http://bwipjs-api.metafloor.com/?bcid=code128&text=' + order_id + '&includetext">'
			code39 = '<img src="https://barcode.tec-it.com/barcode.ashx?data=' + order_id + '&code=Code39&multiplebarcodes=false&translate-esc=false&unit=Fit&dpi=96&imagetype=Gif&rotation=0&color=%23000000&bgcolor=%23ffffff&qunit=Mm&quiet=0&dmsize=Default" alt="Barcoded value"/>'
			#KOIR = 
			Data_Matrix = '<img src="https://barcode.tec-it.com/barcode.ashx?data=' + order_id + '&code=DataMatrix&multiplebarcodes=false&translate-esc=false&authentication=None&ssid=%D0%98%D0%BC%D1%8F+%D1%81%D0%B5%D1%82%D0%B8+(SSID)&password=&unit=Fit&dpi=96&imagetype=Gif&rotation=0&color=%23000000&bgcolor=%23ffffff&qunit=Mm&quiet=0&dmsize=Default" alt="Barcoded value"/>'
			EAN128 = '<img src="https://barcode.tec-it.com/barcode.ashx?data=' + order_id + '&code=EANUCC128&multiplebarcodes=false&translate-esc=false&authentication=None&ssid=%D0%98%D0%BC%D1%8F+%D1%81%D0%B5%D1%82%D0%B8+(SSID)&password=&unit=Fit&dpi=96&imagetype=Gif&rotation=0&color=%23000000&bgcolor=%23ffffff&qunit=Mm&quiet=0&dmsize=Default" alt="Barcoded value"/>'
			EAN13 =  '<img src="https://barcode.tec-it.com/barcode.ashx?data=' + barcode + '&code=EAN13&multiplebarcodes=false&translate-esc=false&authentication=None&ssid=%D0%98%D0%BC%D1%8F+%D1%81%D0%B5%D1%82%D0%B8+(SSID)&password=&unit=Fit&dpi=96&imagetype=Gif&rotation=0&color=%23000000&bgcolor=%23ffffff&qunit=Mm&quiet=0&dmsize=Default" alt="Barcoded value"/>'
			con_sign = 'A2' + telephone + '%26' + pincode
			qrcode = '<img alt="Barcoded value' + con_sign + '"src="https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=' + con_sign + '"'
			
			self.table = self.table + '<tr><td>Order_id = ' + order_id + ',<br>Barcode = ' + barcode + ',<br>PinCode = ' + pincode + ',\nSign = ' + con_sign + '</td><td>' + code128 + '</td><td>' + code39 + '</td><td>' + Data_Matrix + '</td><td>' + EAN128 + '</td><td>' + EAN13 + '</td><td>' + '<img alt="Barcoded value' + barcode + '"src="http://bwipjs-api.metafloor.com/?' \
			'bcid=code128&text=' + barcode + '&includetext"></td><td>' + qrcode +'</td></tr>'
			print('Succes')
 
if __name__ == "__main__":
	g = gen_html()
	with open("List_gen_next.csv") as f_obj:
		g.csv_dict_reader(f_obj)
	g.save_in()