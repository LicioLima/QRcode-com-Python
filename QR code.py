import qrcode

dado = 'https://github.com/LicioLima'
img = qrcode.make(dado)
img.show()