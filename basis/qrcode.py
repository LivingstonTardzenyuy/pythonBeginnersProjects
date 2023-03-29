# converted a text in QR code

#steps
#install libraries needed i.e qrcode and Image
#create a function that collects text and convert it to a qr code
#save the qr code as image
#run function

import qrcode

def genarate_QRCode(text):
    qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")

url=input("enter your own url")
genarate_QRCode(url)
