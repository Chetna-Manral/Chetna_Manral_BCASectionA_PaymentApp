
import cv2
from pyzbar.pyzbar import decode
import requests
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

API_BASE = "http://127.0.0.1:8000"

Builder.load_file("kv_design.kv")

class MainInterface(BoxLayout):
    def scan_barcode(self):
        cap = cv2.VideoCapture(0)
        barcode_data = None
        while True:
            _, frame = cap.read()
            for barcode in decode(frame):
                barcode_data = barcode.data.decode('utf-8')
                cap.release()
                cv2.destroyAllWindows()
                self.ids.status.text = f"Scanned: {barcode_data}"
                self.get_product(barcode_data)
                return

    def get_product(self, barcode):
        resp = requests.post(f"{API_BASE}/scan/", json={"barcode": barcode})
        if resp.status_code == 200:
            data = resp.json()
            self.ids.product_name.text = data["name"]
            self.ids.product_price.text = "$" + data["price"]
            self.price = data["price"]
        else:
            self.ids.status.text = "Product not found."

    def make_payment(self):
        resp = requests.post(f"{API_BASE}/pay/", json={"amount": self.price})
        if resp.status_code == 200:
            client_secret = resp.json()["client_secret"]
            self.ids.status.text = f"Payment initiated. Client Secret: {client_secret}"
        else:
            self.ids.status.text = "Payment failed."

class BarcodeApp(App):
    def build(self):
        return MainInterface()

if __name__ == '__main__':
    BarcodeApp().run()