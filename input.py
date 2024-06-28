prompt = "Tell me something. Tap 'quit' to finish. "
active = True
while active:
    message = input(prompt).strip().lower()  # Handle case sensitivity and whitespace
    if message == 'quit':
        active = False
        #print("Debug: Exiting loop")
    else:
        print(message)


unconfirmed_users = ['alice', 'bob', 'brandi-love']
confirmed_users = []
while unconfirmed_users:
    curr_users = unconfirmed_users.pop()
    print("Verifying User: " + curr_users.title())
    confirmed_users.append(curr_users)
print("\nThe following users have been verified.")
for con_user in confirmed_users:
    print(con_user.title())
