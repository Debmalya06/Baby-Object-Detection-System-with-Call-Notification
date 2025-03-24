from twilio.rest import Client

# Twilio Credentials
TWILIO_ACCOUNT_SID = "AC90a47e34b33500ecce021f6308462182"
TWILIO_AUTH_TOKEN = "5718922b0952aee8eeb9c147e903e480"
TWILIO_PHONE_NUMBER = "+16575306863"
YOUR_PHONE_NUMBER = "+917439033371"

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
