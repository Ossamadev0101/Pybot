import pywhatkit as kit

def generate_qr_code():
    phone_number = input("Enter WhatsApp phone number (with country code): ")
    kit.sendwhatmsg_instantly(phone_number, "This message is to trigger QR code generation.")
    print("QR code generation triggered. Please scan the QR code in the received message.")

if __name__ == "__main__":
    generate_qr_code()
