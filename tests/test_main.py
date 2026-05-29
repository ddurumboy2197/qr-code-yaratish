import pytest
from PIL import Image
from qrcode import QRCode

def create_qr_code(data):
    qr = QRCode(
        version=1,
        box_size=10,
        border=4,
        error_correction=0,
        enable_eci=False,
        encode_mode='byte',
        mask_pattern='H'
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

def test_create_qr_code():
    data = "https://www.example.com"
    img = create_qr_code(data)
    assert img.size == (21, 21)
    assert img.mode == "RGB"
    assert img.getpixel((10, 10)) == (0, 0, 0)

def test_create_qr_code_empty_data():
    data = ""
    img = create_qr_code(data)
    assert img.size == (21, 21)
    assert img.mode == "RGB"
    assert img.getpixel((10, 10)) == (255, 255, 255)

def test_create_qr_code_large_data():
    data = "a" * 1000
    img = create_qr_code(data)
    assert img.size == (21, 21)
    assert img.mode == "RGB"
    assert img.getpixel((10, 10)) == (0, 0, 0)
