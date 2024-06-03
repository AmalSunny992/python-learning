import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier


phone_number=input("Enter a phone number")

pn=phonenumbers.parse(phone_number)

tz=timezone.time_zones_for_number(pn)
gc=geocoder.description_for_number(pn,'en')
gcc=geocoder.country_name_for_number(pn,'en')
sn=carrier.name_for_number(pn,'en')

print(tz,gc,gcc,sn)
