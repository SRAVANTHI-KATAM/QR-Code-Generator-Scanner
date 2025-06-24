import qrcode

def generate_qr(data, output_file="output_qr.png"):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
    print(f"[+] QR Code generated and saved as {output_file}")

if __name__ == "__main__":
    text = input("Enter text or URL to generate QR: ")
    generate_qr(text)
