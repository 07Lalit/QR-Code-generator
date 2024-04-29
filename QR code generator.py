import pygame
from qrcode import *
import time
import qrcode

p = None
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# qr.add_data("This is confidential data can't access ")
# qr.make(fit=True)
#
# img = qr.make_image(fill_color=(255,215,0), back_color=(192,192,192))
# img.save("dd.png")
def Start():
    global p
    n= input("Enter what you want in your qrcode (text or link) mention: ")
    if n=='text' or n=='Text' or n=='T' or n=='t':
        i = input("Enter a text to make QR Code: ")
        j= input("Enter the name of Your QR_code: ")
    else:
        i = input("Enter a url to make QR Code: ")
        j = input("Enter the name of Your QR_code: ")
    qr = qrcode.QRCode(
        version=1,
        error_correction=constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    print("processing",end="")
    for k in range(5):
        print(".",end="")
        time.sleep(1)

    if n=='text' or n=='Text' or n=='T' or n=='t' :
        co = [int(x) for x in input("\nEnter color of qr_code in rgb(r,g,b) values sep by space:  ").split()]
        do = [int(x) for x in input("\nEnter backgroud color of qr_code in rgb(r,g,b) values sep by space:  ").split()]
        qr.add_data(i)
        qr.make(fit=True)
        #img = make(i)
        img = qr.make_image(fill_color=(co[0],co[1],co[2]), back_color=(do[0], do[1], do[2]))
        u = j+'.png'
        img.save(u)
    else:
        img= make(i)
        u = j + '.png'
        img.save(u)

    for k in range(5):
        print(".",end="")
        time.sleep(1)
    print("\nYour QR Code is ready to download ..")
    Image(u)

def Image(u):

    pygame.init()
    window = pygame.display.set_mode((400, 400))
    pygame.display.set_caption("QR Code Generator")
    bg_image = pygame.image.load(u)
    run= True
    window.fill((255,255,255))
    pygame.display.update()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        window.blit(bg_image,(0,0))
        pygame.display.update()
    pygame.quit()
    quit()

Start()