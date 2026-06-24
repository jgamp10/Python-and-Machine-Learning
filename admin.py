usernames = ['sujan', 'admin', 'ram', 'safal', 'ankit']

for username in usernames:
    if username == 'admin':
        print("Hello " + username + "." + " Would you like to see a status report?")
    else:
        print("Hello " + username + "." + " Thank you for logging in agian.")

for username in usernames:
    usernames.remove(username)
    print(usernames)

if usernames:
    print(" We need to find some users!\n")

current_users = ['ankit', 'bijay', 'dinesh', 'hemant', 'samip'] 
new_users = ['samip', 'rajan', 'sujan', 'rijan', 'ankit'] 

for new_user in new_users:
    if new_user in current_users:
        print("\n"+ new_user + " You need to have a different username")
    else:
        print("\nThis username is available to use right now.")

for value in range(1,10):
    if value == 1:
        print(str(value) + "st ")
    elif value == 2:
         print(str(value) + "nd ")
    elif value == 3:
         print(str(value) + "rd ")
    else:
        print(str(value) + "th ")
        
