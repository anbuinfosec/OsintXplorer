import phonenumbers
from phonenumbers import geocoder, carrier

def scan_number(number):
    try:
        parsed = phonenumbers.parse(number, None)
        valid = phonenumbers.is_valid_number(parsed)
        region = geocoder.description_for_number(parsed, "en")
        service = carrier.name_for_number(parsed, "en")
        return {
            "Valid": valid,
            "Region": region,
            "Carrier": service
        }
    except Exception as e:
        return {"Error": str(e)}
