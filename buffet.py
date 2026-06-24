foods = ( 'burger', 'pizza', 'shrimp', 'mussels', 'clams')
for food in foods:
    print(food)
    print("\n")
foods = ('noodles', 'burger' , 'pizza', 'pasta')
print("\nThis is the updated menu for the restaurant.\n")
for food in foods:
    print(food)
    print("\n")
print("*********************----------------********************")
print("\n")

nepali_foods = ['momo', 'chowmein', 'chatpate', 'gundruk']
for nepali_food in nepali_foods:
    if nepali_food == 'gundruk':
        print(nepali_food.upper() + " is my favourite nepali food\n")
    else:
        print(nepali_food.lower() + " is not my favourtie food \n")

requested_toppings = ['mushrooms', 'onions', 'pineapple']

print('mushrooms' in requested_toppings)
print("\n")

favorite_topping = 'pepper'

if favorite_topping not in requested_toppings:
    print(favorite_topping.upper() + " we need to add this ingredient next"
    "time in the future \n")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms ', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print ("Adding " + requested_topping + " .")
    else:
        print ("Sorry , we don't have " + requested_topping + " .")

print("\nFinished making your pizza!")

