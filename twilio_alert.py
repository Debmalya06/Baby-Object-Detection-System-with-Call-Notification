from twilio.rest import Client

# Twilio Credentials
TWILIO_ACCOUNT_SID = "ssid"
TWILIO_AUTH_TOKEN = "Auth"
TWILIO_PHONE_NUMBER = "twilio number"
YOUR_PHONE_NUMBER = "your mobile number"

def make_phone_call():
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        call = client.calls.create(
            to=YOUR_PHONE_NUMBER,
            from_=TWILIO_PHONE_NUMBER,
            twiml="<Response><Say>Alert! Alert! Remove the object from your baby immediately.</Say></Response>"
        )
        print("Call initiated:", call.sid)
    except Exception as e:
        print("Error making phone call:", e)
