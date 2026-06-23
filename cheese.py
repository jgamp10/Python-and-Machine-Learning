cheeses = ['italian', 'mozarella','blue', 'parmesan']
for cheese in cheeses:
    print("This is the " + cheese.title() + " cheese." )
print("This is the time of my life where I had the most exciting food.")

pets = ['cat', 'dog', 'parrot', 'pig']
for pet in pets:
    print()
friend_pizzas = cheeses[:]
friend_pizzas.append('feta')
cheeses.append('swiss')
print("My favourite pizzas are : \n")
for cheese in cheeses:
    print(cheese)
    print ("\n")

print("My friend's favourite pizzas are: \n")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
    print ("\n")

requested_toppings = ['mushrooms' , 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' not in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\n Finished making your pizza.")
