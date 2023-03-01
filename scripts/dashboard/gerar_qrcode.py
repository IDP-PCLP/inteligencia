import qrcode

url = "https://forms.gle/ohpmefifNTnrn78x6"
img = qrcode.make(url)

img.save("qrcode.png")
