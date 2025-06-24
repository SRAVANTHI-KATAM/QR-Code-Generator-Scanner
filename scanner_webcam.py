import cv2

def scan_qr_from_webcam():
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    print("[*] Scanning... Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        data, bbox, _ = detector.detectAndDecode(frame)
        if data:
            print(f"[+] QR Code Detected: {data}")
            break

        cv2.imshow("QR Scanner - Press q to quit", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    scan_qr_from_webcam()
