responses= {}
poll = True
while poll:
    mess= input("What is your name? ")
    res = input("Which girl would you like to marry, " + mess.title() + "? ")
    responses[mess] = res
    
    repeat = input("Would you like to let another person in? (yes/no) ")
    if repeat == 'no':
        poll = False
    

#Showing Results of the poll
print("\n----Poll Results----")
for mess, res in responses.items():
    print(mess.title()+" would like to marry "+res.title())                                