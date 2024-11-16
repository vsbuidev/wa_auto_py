import pywhatkit as kit
import pandas as pd
import time

contacts = pd.read_csv("contacts.csv")
image_path = "image.png"
message = "Hello, this image is shared with automation."

for index, contact in contacts.iterrows():
    phone_number = str(contact['Phone Number']).strip()
    
    if not phone_number.startswith("+"):
        phone_number = "+91" + phone_number  # Replace with your country code

    try:
        kit.sendwhats_image(phone_number, image_path, message, wait_time=10)
        print(f"Image sent to {phone_number}")
        time.sleep(10)
    except Exception as e:
        print(f"Failed to send to {phone_number}: {e}")
