import random
print(''' Odd or Even
Enter numbers from 1 to 6
Winner of toss to bat ''')
a=input("Odd or Even? ")
b=a.upper()
y=0
UserRuns=0
UserWickets=0
ComputerRuns=0
ComputerWickets=0

if b == "EVEN":
    x=int(input("Enter a number for toss : "))
    r1=random.randint(0,6)
    y = x+r1
    print("Computer chose : " ,r1)
    if y%2 == 0:
        print("User wins the toss ")
        print("User to bat for 3 wickets")
        
        while UserWickets < f:
                g=int(input("Enter your move "))
                r4=random.randint(0,6)
                if g>6:
                    print("Please enter a valid move ")
                else:
                    if g == 0:
                        if g == r4:
                            print("One or Two")
                            h=int(input("Enter your move"))
                            r5=random.randint(1,2)
                            if h >2:
                                print("Please enter a valid move")
                            else:
                                if h == 1:
                                    if h == r5:
                                        print("OUT")
                                        UserWickets+=1
                                        print("Score : " , UserRuns , UserWickets)
                                    else:
                                        UserRuns+=1
                                        print("Score : " , UserRuns , UserWickets)
                                if h == 2:
                                    if h == r5:
                                        print("OUT")
                                        UserWickets+=1
                                        print("Score : " , UserRuns , UserWickets)
                                    else:
                                        UserRuns+=2
                                        print("Score : " , UserRuns , UserWickets)
                        else:
                            UserRuns+=r4
                            print("Score : " , UserRuns , UserWickets)
                                    
                    if g == 1:
                        if g == r4:
                            print("OUT")
                            UserWickets+=1
                            print("Score : " , UserRuns , UserWickets)
                        else:
                            UserRuns+=1
                            print("Score : " , UserRuns , UserWickets)
                    if g == 2:
                        if g == r4:
                            print("OUT")
                            UserWickets+=1
                            print("Score : " , UserRuns , UserWickets)
                        else:
                            UserRuns+=2
                            print("Score : " , UserRuns , UserWickets)
                    if g == 3:
                        if g == r4:
                            print("OUT")
                            UserWickets+=1
                            print("Score : " , UserRuns , UserWickets)
                        else:
                            UserRuns+=3
                            print("Score : " , UserRuns , UserWickets)
                    if g == 4:
                        if g == r4:
                            print("OUT")
                            UserWickets+=1
                            print("Score : " , UserRuns , UserWickets)
                        else:
                            UserRuns+=4
                            print("Score : " , UserRuns , UserWickets)
                    if g == 5:
                        if g == r4:
                            print("OUT")
                            UserWickets+=1
                            print("Score : " , UserRuns , UserWickets)
                        else:
                            UserRuns+=5
                            print("Score : " , UserRuns , UserWickets)
                    if g == 6:
                        if g == r4:
                            print("OUT")
                            UserWickets+=1
                            print("Score : " , UserRuns , UserWickets)
                        else:
                            UserRuns+=6
                            print("Score : " , UserRuns , UserWickets)
print("User Score : " , UserRuns , "Runs" , UserWickets , "Wickets")
print("Computer's Target = " , UserRuns + 1)
f = UserWickets
while ComputerWickets < f :
    g=int(input("Enter your move "))
    r4=random.randint(0,6)
    if g>6:
        print("Please enter a valid move ")
    if g == 0:
        if g == r4:
            print("One or Two")
            h=int(input("Enter your move"))
            r5=random.randint(1,2)
            if h >2:
                print("Please enter a valid move")
            else:
                if h == 1:
                    if h == r5:
                        print("OUT")
                        ComputerWickets+=1
                        print("Score : " , ComputerRuns , ComputerWickets)
                    else:
                        ComputerRuns+=r5
                        print("Score : " , ComputerRuns , ComputerWickets)
                if h == 2:
                    if h == r5:
                        print("OUT")
                        ComputerWickets+=1
                        print("Score : " , ComputerRuns , ComputerWickets)
                    else:
                        ComputerRuns+=r5
                        print("Score : " , ComputerRuns , ComputerWickets)
        elif g!=r4:
            ComputerRuns+=r4
            print("Score : " , ComputerRuns , ComputerWickets)
    if g == 1:
        if g == r4:
            print("OUT")
            ComputerWickets+=1
            print("Score : " , ComputerRuns , ComputerWickets)
        else:
            ComputerRuns+=r4
            print("Score : " , ComputerRuns , ComputerWickets)
    if g == 2:
        if g == r4:
            print("OUT")
            ComputerWickets+=1
            print("Score : " , ComputerRuns , ComputerWickets)
        else:
            ComputerRuns+=r4
            print("Score : " , ComputerRuns , ComputerWickets)
    if g == 3:
        if g == r4:
            print("OUT")
            ComputerWickets+=1
            print("Score : " , ComputerRuns , ComputerWickets)
        else:
            ComputerRuns+=r4
            print("Score : " , ComputerRuns , ComputerWickets)
    if g == 4:
        if g == r4:
            print("OUT")
            ComputerWickets+=1
            print("Score : " , ComputerRuns , ComputerWickets)
        else:
            ComputerRuns+=r4
            print("Score : " , ComputerRuns , ComputerWickets)
    if g == 5:
        if g == r4:
            print("OUT")
            ComputerWickets+=1
            print("Score : " , ComputerRuns , ComputerWickets)
        else:
            ComputerRuns+=r4
            print("Score : " , ComputerRuns , ComputerWickets)
    if g == 6:
        if g == r4:
            print("OUT")
            ComputerWickets+=1
            print("Score : " , ComputerRuns , ComputerWickets)
        else:
            ComputerRuns+=r4
            print("Score : " , ComputerRuns , ComputerWickets)
    if ComputerRuns>UserRuns or ComputerWickets==UserWickets:
        break
        print("Computer Score : " , ComputerRuns , "Runs" , ComputerWickets , "Wickets")
if UserRuns > ComputerRuns:
    print("User wins by " , UserRuns - ComputerRuns , "Runs")
elif ComputerRuns > UserRuns:
    print("Computer wins by " , UserWickets - ComputerWickets , " Wickets " )
if ComputerRuns == 0 and UserRuns == 0:
    if y%2 != 0:
            print(y)
            print("Computer wins the toss")
            print("Computer to bat for 3 wickets ")
            r3 = 3
            while ComputerWickets <  r3:
                            g=int(input("Enter your move "))
                            r4=random.randint(0,6)
                            if g>6:
                                    print("Please enter a valid move ")
                            else:
                                    if g == 0:
                                            if g == r4:
                                                    print("One or Two")
                                                    h=int(input("Enter your move"))
                                                    r5=random.randint(1,2)
                                                    if h >2:
                                                            print("Please enter a valid move")
                                                    else:
                                                            if h == 1:
                                                                    if h == r5:
                                                                            print("OUT")
                                                                            ComputerWickets+=1
                                                                            print("Score : " , ComputerRuns , ComputerWickets)
                                                                    else:
                                                                            ComputerRuns+=r5
                                                                            print("Score : " , ComputerRuns , ComputerWickets)
                                                            if h == 2:
                                                                    if h == r5:
                                                                            print("OUT")
                                                                            ComputerWickets+=1
                                                                            print("Score : " , ComputerRuns , ComputerWickets)
                                                                    else:
                                                                            ComputerRuns+=r5
                                                                            print("Score : " , ComputerRuns , ComputerWickets)
                                            else:
                                                    ComputerRuns+=r4
                                                    print("Score : " , ComputerRuns , ComputerWickets)
                                    if g == 1:
                                            if g == r4:
                                                    print("OUT")
                                                    ComputerWickets+=1
                                                    print("Score : " , ComputerRuns , ComputerWickets)
                                            else:
                                                    ComputerRuns+=r4
                                                    print("Score : " , ComputerRuns , ComputerWickets)
                                    if g == 2:
                                            if g == r4:
                                                    print("OUT")
                                                    ComputerWickets+=1
                                                    print("Score : " , ComputerRuns , ComputerWickets)
                                            else:
                                                    ComputerRuns+=r4
                                                    print("Score : " , ComputerRuns , ComputerWickets)
                                    if g == 3:
                                            if g == r4:
                                                    print("OUT")
                                                    ComputerWickets+=1
                                                    print("Score : " , ComputerRuns , ComputerWickets)
                                            else:
                                                    ComputerRuns+=r4
                                                    print("Score : " , ComputerRuns , ComputerWickets)
                                    if g == 4:
                                            if g == r4:
                                                    print("OUT")
                                                    ComputerWickets+=1
                                                    print("Score : " , ComputerRuns , ComputerWickets)
                                            else:
                                                    ComputerRuns+=r4
                                                    print("Score : " , ComputerRuns , ComputerWickets)
                                    if g == 5:
                                            if g == r4:
                                                    print("OUT")
                                                    ComputerWickets+=1
                                                    print("Score : " , ComputerRuns , ComputerWickets)
                                            else:
                                                    ComputerRuns+=r4
                                                    print("Score : " , ComputerRuns , ComputerWickets)
                                    if g == 6:
                                            if g == r4:
                                                    print("OUT")
                                                    ComputerWickets+=1
                                                    print("Score : " , ComputerRuns , ComputerWickets)
                                            else:
                                                    ComputerRuns+=r4
                                                    print("Score : " , ComputerRuns , ComputerWickets)
print("Computer Score : " , ComputerRuns , "Runs" , ComputerWickets , "Wickets")
if UserRuns==0:
    print("User's Target = " , ComputerRuns + 1)
while UserWickets < ComputerWickets:
        g=int(input("Enter your move "))
        r4=random.randint(0,6)
        if g>6:
                print("Please enter a valid move ")
        else:
                if g == 0:
                        if g == r4:
                            print("One or Two")
                            h=int(input("Enter your move"))
                            r5=random.randint(1,2)
                            if h >2:
                                print("Please enter a valid move")
                            else:
                                    if h == 1:
                                            if h == r5:
                                                    print("OUT")
                                                    UserWickets+=1
                                                    print("Score : " , UserRuns , UserWickets)
                                            else:
                                                    UserRuns+=1
                                                    print("Score : " , UserRuns , UserWickets)
                                            if h == 2:
                                                    if h == r5:
                                                            print("OUT")
                                                            UserWickets+=1
                                                            print("Score : " , UserRuns , UserWickets)
                                                    else:
                                                            UserRuns+=2
                                                            print("Score : " , UserRuns , UserWickets)
                        else:
                            UserRuns+=r4
                            print("Score : " , UserRuns , UserWickets)
                if g == 1:
                        if g == r4:
                            print("OUT")
                            UserWickets+=1
                            print("Score : " , UserRuns , UserWickets)
                        else:
                            UserRuns+=1
                            print("Score : " , UserRuns , UserWickets)
                if g == 2:
                        if g == r4:
                            print("OUT")
                            UserWickets+=1
                            print("Score : " , UserRuns , UserWickets)
                        else:
                            UserRuns+=2
                            print("Score : " , UserRuns , UserWickets)
                if g == 3:
                        if g == r4:
                            print("OUT")
                            UserWickets+=1
                            print("Score : " , UserRuns , UserWickets)
                        else:
                            UserRuns+=3
                            print("Score : " , UserRuns , UserWickets)
                if g == 4:
                        if g == r4:
                            print("OUT")
                            UserWickets+=1
                        else:
                            UserRuns+=4
                            print("Score : " , UserRuns , UserWickets)
                if g == 5:
                        if g == r4:
                            print("OUT")
                            UserWickets+=1
                            print("Score : " , UserRuns , UserWickets)
                        else:
                            UserRuns+=5
                            print("Score : " , UserRuns , UserWickets)
                if g == 6:
                        if g == r4:
                            print("OUT")
                            UserWickets+=1
                            print("Score : " , UserRuns , UserWickets)
                        else:
                            UserRuns+=6
                            print("Score : " , UserRuns , UserWickets)
                if UserWickets == ComputerWickets or UserRuns > ComputerRuns:
                        break
                print("User Score : " , UserRuns , "Runs" , UserWickets , "Wickets")
if UserRuns > ComputerRuns:
    print("User wins by " , ComputerWickets - UserWickets , "Wickets")
    break
elif ComputerRuns > UserRuns:
    print("Computer wins by " , ComputerRuns - UserRuns , " Runs " )
    break

