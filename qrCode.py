import qrcode
from PIL import Image
qr = Qrfile.QRcode(version 1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size = 10 , border = 4,
                   )
qr.add_data("https://chatgpt.com/c/6829f56f-b968-800f-b9c3-52ff13918a2e")
qr.make(fit=True)
img = qr.make_image(fill_color = "red",back_color = "white")
img.save("chatgptweb.png")
