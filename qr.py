import qrcode
img_name = "medium.png"
def generate(data="https://scrapbook.hackclub.com", img_name="hackclub.png"):
     img = qrcode.make(data) #generate QRcode
     img.save(img_name)
     return img
generate()# in command line
