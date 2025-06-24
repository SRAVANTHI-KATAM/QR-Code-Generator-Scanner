import cv2

def scan_qr_from_image(image_path):
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, _, _ = detector.detectAndDecode(img)

    if data:
        print(f"[+] QR Code Data: {data}")
    else:
        print("[-] No QR Code found in the image.")

if __name__ == "__main__":
    path = input("Enter path to QR Code image: ")
    scan_qr_from_image(path)
