# Minutes to Hours & Minutes
# Take total minutes and convert it into hours and remaining minutes.

a = int(input("Enter minutes to convert into Hour and min."))

hour = a//60

minutes = a%60

print(f"{hour} hour and {minutes} min")