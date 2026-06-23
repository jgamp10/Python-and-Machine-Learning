age = 12
if age < 4:
    print("Your admission cost is 0.")
elif age > 18:
    print("Your admission cost is 5.")
else:
    print("Your admission cost is 10.")

if age < 4:
    fine = 0
elif age < 18:
    fine = 5
else:
    fine = 10
print("Your fine is " + str(fine) + ".")

#don't forget the elif statement is only run when the first if statement runs 
#the second elif statement runs only after failing the first elif statement


