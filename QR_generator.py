#to edit this code you need: pip3 install qrcode Image (on MacOS)
import qrcode

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version= 1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("QRimg.png") #name of the image
    #the image will be generetad and saved in root directory 


#once you run the code, you receive prompt here you enter the link you want to make QR code of
url = input("Enter your url: ")
generate_qrcode(url)    

