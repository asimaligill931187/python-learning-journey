print("Welcome to tip Calculator. ")
Total_bill=float(input("What wes the total bill?  $"))
tip_percentage=int(input("What percentage tip would you like to give? 10, 12, or 15?"))
Tip=(Total_bill*tip_percentage)/100
# bill after tip
Final_bill=Total_bill+Tip
split=int(input("How many person to split bill?"))
each_person=Final_bill/split
rounded=round(each_person ,2)
print(f"Each person should pay $:{rounded}")