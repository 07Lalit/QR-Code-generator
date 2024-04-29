import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("This is confidential data can't access ")
qr.make(fit=True)

img = qr.make_image(fill_color=(255,215,0), back_color=(192,192,192))
img.save("dd.png")