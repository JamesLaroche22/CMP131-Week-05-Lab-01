#James_Laroche
#CMP-131 
#Week_5
#Lab_1
#Even_or_Odd
#September_30th 
print("----EVEN OR ODD----") #Title
print()
num=int(input("Enter Integer: "))  #What we need from the user
print() 
print("Integer Entered: " , num ,) #Displaying the integer enetered by the user to the output. 
print()
if(num%2==0): #Based on the remainder from the divison, we know if the integer is even or odd.
    print("Number is even.") 
else:
    print("Number is odd.")