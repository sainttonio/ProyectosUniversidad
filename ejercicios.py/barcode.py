from barcode import EAN13
from barcode.writer import ImageWriter

# El código debe tener 12 dígitos (el 13° es el dígito de control)
codigo = "590123412345"

ean = EAN13(codigo, writer=ImageWriter())
filename = ean.save("ean13_barcode")