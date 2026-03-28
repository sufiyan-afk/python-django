import qrcode

# Data for the QR code
data = ("https://youtu.be/-4e3ewcTupM")

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box (pixels)
    border=4,  # Border size (boxes)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Generate the image
img = qr.make_image(fill="black", back_color="white")

# Save the image to a file
img.save("qrcode_example.png")

# You can also display the image directly using PIL
img.show()