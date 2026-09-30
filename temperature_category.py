#James_Laroche
#CMP-131 
#Week_5
#Lab_1
#Temperature_Category 
#September_30th 
print("----TEMPERATURE CHECK----") #Title
print()
temperature=float(input("Enter Temperature in Fareheit: ")) #Input from the user.
print()
print("Temperature Entered: " , temperature , "°F") #Input from the user displayed.
print()
if temperature <=49.9: #Different outcomes below based on the number given by the user. 
    print("Temperature Category: Cold") 
elif temperature > 49.9:
    if temperature <=79.9:
        print("Temperature Category: Warm") 
if temperature >79.9: 
    print("Temperature Category: Hot")

