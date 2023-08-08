
import phonenumbers
from phonenumbers import timezone, geocoder, carrier


def get_phone_info(phone_number):
    phone = phonenumbers.parse(phone_number, None)  #parse() is used to conver the number to make it understanable by phonenumbers library

    if not phonenumbers.is_valid_number(phone):    #checks validity of number
        return "Invalid phone number"

    time_zones = [tz.strip() for tz in timezone.time_zones_for_number(phone)]   #tz.strip() removes unwanted white spaces
    carrier_name = carrier.name_for_number(phone, "en")
    region_info = geocoder.description_for_number(phone, "en")

    return {
        "Number": phone_number,               # dictionary to map the key with values
        "Valid": True,
        "Timezones": time_zones,
        "Carrier": carrier_name,
        "Region": region_info
    }


def main():
    number = input("Enter the phone number to trace with +__: ")
    info = get_phone_info(number)

    for key, value in info.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
