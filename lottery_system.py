import random as r
u_name =  str(input("Please enter your name:"))
u_con_number = int(input("Please enter your phone number:"))
u_age = int(input("Please enter your age:"))
if u_age < 18:
    print(f"Sorry! minimum age allowed is 18 years. Come again after {18-u_age} years")
else:
    r.seed(r.shuffle(list(u_name)))
    token = r.randrange(1,1000)
    #print(token)

    if token in range(1,21):
        print("Congrats, you won  $10M")
    elif token in range(21,41):
        print("Congrats, you won  $5M")
    elif token in range(41,61):
        print("Congrats, you won $3M")
    elif token in range(61,91):
        print("Congrats, you won $1M")
    elif token in range(91,111):
        print("Congrats, you won  $1000")
    elif token in range(111,990):
        print("Congrats, you won  $100")
    elif token in range(990,1001):
        print("Congrats, you won $10")
    else:
        print("Sorry better luck next time!")