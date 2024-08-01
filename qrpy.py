import qrcode as qr

img = qr.make("https://www.linkedin.com/in/rohan-tyagi-245155240/")
img.save("Linkedin.png")



# The given below code helps to customize the qrcode according to the user requirement.
'''
import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                    error_correction = qrcode.constants.ERROR_CORRECT_H,
                    box_size=20, border=4,)
qr.add_data("https://www.linkedin.com/in/rohan-tyagi-245155240/")
qr.make(fit=True)
img = qr.make_image(fill_color="red", back_color = "blue")
img.save("Linkedin_cust.png")
'''