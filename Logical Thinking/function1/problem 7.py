"""

"""

def random():
    import random
    random_no = random.randint(0, 6)
    return random_no


point = 0
while True:
    inp = input("press any key to roll the dice")
    random_no = random()
    print(random_no)
    if point < 50:
        if random_no == 0:
            print("Your Total Points :", point)
            print("Game ends ! ")
            print("You Lose ! ")
            break
        elif random_no % 2 == 0:
            point += 2
            print("Your Points :", point)
            continue
        elif random_no % 2 == 1:
            if (random_no == 1) or (random_no == 3):
                print("Jump")
                continue
            elif random_no == 5:
                point += 3
                print("Your Points :", point)
    else:
        print("Your Points :", point)
        print('You won ! ')
