#Print all values between 2000 and 3000 that are 
# divisible by 7 but are not a multiple of 5
for x in range(2000,3200,1):
    if x % 7 == 0 and x % 5 != 0:
        print(x)
