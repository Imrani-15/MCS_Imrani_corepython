import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
'''
Decoding with pyzbar
decode() function returns a list of namedtuple called Decoded . 
Each of them contains the following fields: data — 
The decoded string in bytes. You need to decode it using utf8 to get a string. 
type — Only useful for barcodes as it outlines the barcode format
'''
data = 'Never give up'
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
# qr.make()
# img = qr.make_image(fill_color = 'blue', back_color= 'white')
# img.save('G:/Qrcode/myqrcode1.png')
# img = Image.open('G:/Qrcode/myqrcode1.png')
# result = decode(img)
# print(result)

img = qrcode.make(data)
img.save('G:/Qrcode/myqrcode.png')
