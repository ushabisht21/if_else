import <phonenumbers>
from <phonenumbers> import carrier, geocoder, timezone

mobileNO = input ("Enter Mobile Number with Country code: ")
mobileNO = phonenumbers.parse(mobileNO)

# get time zone a phone number
print(timezone.time_zones_for_number(mobileNO))

#getting carrier of a phone number 
print(carrier.name_for_number(mobileNO, "en"))

#geting region informaation
print(geocoder.description_for_number(mobileNO, "en"))

# validating a phone number 
print("valid mobile number:",phonenumbers.is_valid_number(mobileNO))

#checking possibility of a number 
print("checking possibity of number :",phonenumbers.is_possible_number(mobileNO))