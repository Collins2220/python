
weight=float(input("enter your weight"))
unit=input("kilograms or pounds? (K or L):")

if unit=="k":
    weight= weight * 2.304
    unit = "Lbs."
elif unit=="L":
    weight = weight / 2.205
    unit = "kgs."
else:
   print(f"{unit}was not valid")

print(f"your weight is:{round(weight,1)}{unit}")

