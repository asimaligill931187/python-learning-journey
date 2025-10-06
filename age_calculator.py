print("Age Calculator how many days,months,weaks left for our lives if we live until 90years")
Days_in_a_year=365
weaks_in_year=52.14
months_in_year=12
# caculate for 90 years
Days_in_90y=Days_in_a_year * 90
weaks_in_90y=weaks_in_year * 90
months_in_90y=months_in_year * 90

age=int(input("Enter your age:"))
days=Days_in_a_year *age
weaks=weaks_in_year*age
months=months_in_year*age

# Now calculate how much time left
Days_left=Days_in_90y-days
weaks_left=weaks_in_90y-weaks
months_left=months_in_90y-months
print(f"Days Left: {Days_left} \n Weaks Left: {weaks_left} \n Months left: {months_left}")
