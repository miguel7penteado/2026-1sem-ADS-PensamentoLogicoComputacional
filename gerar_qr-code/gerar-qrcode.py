import sys
import qrcode

if len(sys.argv) != 2:
    print("Uso: python gerar_qrcode.py <URL>")
    sys.exit(1)

url = sys.argv[1]

img = qrcode.make(url)
img.save("qrcode.png")

print("QR Code gerado com sucesso!")