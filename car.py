cars = ['honda', 'subaru', 'toyato', 'gmc', 'cheverolet']
for car in cars:
    print("Is car == 'subaru'? I predict Ture.")
    print(car == 'subaru')

new_car = 'ford'
if new_car not in cars:
    print("\n" + new_car.upper() + " should be imported from US")
