#!/usr/bin/env python3
"""
QR code generator for the wedding menu/carta
Creates a QR code that links to the PDF hosted on GitHub Pages
"""

import qrcode
import os

def main():
    # Configuration
    GITHUB_USERNAME = "pagaliv"
    REPO_NAME = "carta_boda_charly"
    PDF_NAME = "carta-boda-charly.pdf"

    url = f"https://{GITHUB_USERNAME}.github.io/{REPO_NAME}/{PDF_NAME}"

    # Create directory for QR codes
    os.makedirs('qr-codes', exist_ok=True)

    print("🚀 Generating QR code for the wedding carta...")
    print(f"🔗 URL: {url}")
    print("-" * 50)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    nombre_archivo = "qr-codes/qr_carta_boda_charly.png"
    img.save(nombre_archivo)
    print(f"✅ QR created: {nombre_archivo}")

if __name__ == "__main__":
    main()
