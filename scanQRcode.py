import cv2
from pyzbar.pyzbar import decode

def scan_qr_code_from_camera():
    # Open the camera
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Decode QR codes
        qr_codes = decode(gray)

        # Process each QR code found
        for qr_code in qr_codes:
            data = qr_code.data.decode("utf-8")
            print(f"QR Code Data: {data}")

            # Draw a rectangle around the QR code
            points = qr_code.polygon
            if len(points) == 4:
                pts = [(point.x, point.y) for point in points]
                pts = [tuple(map(int, pt)) for pt in pts]
                cv2.polylines(frame, [pts], isClosed=True, color=(0, 255, 0), thickness=2)

        # Display the frame with QR code highlighted
        cv2.imshow("QR Code Scanner", frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Call the function to scan QR codes from the camera
scan_qr_code_from_camera()
