#first project: QR Code Maker

#install a library called qrcode

import qrcode

#data that we want
data = 'https://www.youtube.com/watch?v=eimgRedLkkU'

#the code below encodes our message to qrcode

img = qrcode.make(data)

#save the img to file we created above in our computer
img.save('myqrcode.jpg')

