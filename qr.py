import cloudinary
import cloudinary.uploader
import qrcode
import uuid

# ===== CLOUDINARY CONFIG =====
cloudinary.config(
    cloud_name="dtrjlm28x",
    api_key="271969628577941",
    api_secret="cFcpfEyBUVGMLkRUBw3sPymycOE"
)

# ===== FOTO PAD =====
foto_pad = r"C:\Users\Brian Goethals\OneDrive - vlot\Afbeeldingen\Jeugdfoto's\camera\2026\100_0393.JPG"

# ===== GITHUB PAGE =====
base_site = "http://www.photoboothvlottest.be/"

try:

    # uniek ID maken
    unique_id = str(uuid.uuid4())

    # foto uploaden
    result = cloudinary.uploader.upload(
        foto_pad,
        public_id=unique_id,
        folder="uploads"
    )

    image_url = result["secure_url"]

    print("Foto geupload:")
    print(image_url)

    # URL voor website maken
    website_url = f"{base_site}?img={image_url}"

    print("QR link:")
    print(website_url)

    # QR code maken
    qr_bestand = f"qr-{unique_id}.png"

    img = qrcode.make(website_url)
    img.save(qr_bestand)

    print("QR code opgeslagen als:")
    print(qr_bestand)

except Exception as e:
    print("Fout:", e)
