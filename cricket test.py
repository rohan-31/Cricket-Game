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
        f=3
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
if UserRuns > 0:
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
if UserRuns > 0 and ComputerRuns > 0:
    if ComputerRuns == 0 and UserRuns == 0:
        if y%2 != 0:
            print("User chose : " , x)
            print("Computer chose : " , r1)
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
elif ComputerRuns > UserRuns:
    print("Computer wins by " , ComputerRuns - UserRuns , " Runs " )

d=0
UserR=0
UserW=0
ComputerR=0
ComputerW=0
e=0
temp = e
if b == "ODD":
    e=int(input("Enter a number for toss : "))
    r6=random.randint(0,6)
    d = e+r6
    if d%2 == 0:
        print("User chose : " ,e)
        print("Computer chose : " ,r6)
        print("Computer wins the toss")
        print("Computer to bat for 3 wickets ")
        r3 = 3
        while ComputerW <  r3:
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
                                    ComputerW+=1
                                    print("Score : " , ComputerR , ComputerW)
                                else:
                                    ComputerR+=r5
                                    print("Score : " , ComputerR , ComputerW)
                                if h == 2:
                                    if h == r5:
                                        print("OUT")
                                        ComputerW+=1
                                        print("Score : " , ComputerR , ComputerW)
                                    else:
                                        ComputerR+=r5
                                        print("Score : " , ComputerR , ComputerW)
                    else:
                        ComputerR+=r4
                        print("Score : " , ComputerR , ComputerW)
                if g == 1:
                    if g == r4:
                        print("OUT")
                        ComputerW+=1
                        print("Score : " , ComputerR , ComputerW)
                    else:
                        ComputerR+=r4
                        print("Score : " , ComputerR , ComputerW)
                if g == 2:
                    if g == r4:
                        print("OUT")
                        ComputerW+=1
                        print("Score : " , ComputerR , ComputerW)
                    else:
                        ComputerR+=r4
                        print("Score : " , ComputerR , ComputerW)
                if g == 3:
                    if g == r4:
                        print("OUT")
                        ComputerW+=1
                        print("Score : " , ComputerR , ComputerW)
                    else:
                        ComputerR+=r4
                        print("Score : " , ComputerR , ComputerW)
                if g == 4:
                    if g == r4:
                        print("OUT")
                        ComputerW+=1
                        print("Score : " , ComputerR , ComputerW)
                    else:
                        ComputerR+=r4
                        print("Score : " , ComputerR , ComputerW)
                if g == 5:
                    if g == r4:
                        print("OUT")
                        ComputerW+=1
                        print("Score : " , ComputerR , ComputerW)
                    else:
                        ComputerR+=r4
                        print("Score : " , ComputerR , ComputerW)
                if g == 6:
                    if g == r4:
                        print("OUT")
                        ComputerW+=1
                        print("Score : " , ComputerR , ComputerW)
                    else:
                        ComputerR+=r4
                        print("Score : " , ComputerR , ComputerW)
if ComputerR > 0:
    print("Computer Score : " , ComputerR , "Runs" , ComputerW , "Wickets")
if UserR==0:
    print("User's Target = " , ComputerR + 1)
while UserW < ComputerW:
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
                                                    UserW+=1
                                                    print("Score : " , UserR , UserW)
                                            else:
                                                    UserR+=1
                                                    print("Score : " , UserR , UserW)
                                            if h == 2:
                                                    if h == r5:
                                                            print("OUT")
                                                            UserW+=1
                                                            print("Score : " , UserR , UserW)
                                                    else:
                                                            UserR+=2
                                                            print("Score : " , UserR , UserW)
                        else:
                            UserR+=r4
                            print("Score : " , UserR , UserW)
                if g == 1:
                        if g == r4:
                            print("OUT")
                            UserW+=1
                            print("Score : " , UserR , UserW)
                        else:
                            UserR+=1
                            print("Score : " , UserR , UserW)
                if g == 2:
                        if g == r4:
                            print("OUT")
                            UserW+=1
                            print("Score : " , UserR , UserW)
                        else:
                            UserR+=2
                            print("Score : " , UserR , UserW)
                if g == 3:
                        if g == r4:
                            print("OUT")
                            UserW+=1
                            print("Score : " , UserR , UserW)
                        else:
                            UserR+=3
                            print("Score : " , UserR , UserW)
                if g == 4:
                        if g == r4:
                            print("OUT")
                            UserW+=1
                        else:
                            UserR+=4
                            print("Score : " , UserR , UserW)
                if g == 5:
                        if g == r4:
                            print("OUT")
                            UserW+=1
                            print("Score : " , UserR , UserW)
                        else:
                            UserRuns+=5
                            print("Score : " , UserR , UserW)
                if g == 6:
                        if g == r4:
                            print("OUT")
                            UserW+=1
                            print("Score : " , UserR , UserW)
                        else:
                            UserR+=6
                            print("Score : " , UserR , UserW)
                if UserW == ComputerW or UserR > ComputerR:
                        break
                        print("User Score : " , UserR , "Runs" , UserW , "Wickets")
if UserR > ComputerR:
    print("User wins by " , ComputerW - UserW , "Wickets")
elif ComputerR > UserR:
    print("Computer wins by " , ComputerR - UserR , " Runs " )
if UserR > 0 and ComputerR>0:
    quit()
if ComputerR == 0 and UserR == 0:
    if d%2 != 0:
        print("User chose : " , e)
        print("Computer chose : " , r6)
        print("User wins the toss ")
        print("User to bat for 3 wickets")
        f=3
        while UserW < f:
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
                                        UserW+=1
                                        print("Score : " , UserR , UserW)
                                    else:
                                        UserR+=1
                                        print("Score : " , UserR , UserW)
                                if h == 2:
                                    if h == r5:
                                        print("OUT")
                                        UserW+=1
                                        print("Score : " , UserR , UserW)
                                    else:
                                        UserR+=2
                                        print("Score : " , UserR , UserW)
                        else:
                            UserR+=r4
                            print("Score : " , UserR , UserW)
                                    
                    if g == 1:
                        if g == r4:
                            print("OUT")
                            UserW+=1
                            print("Score : " , UserR , UserW)
                        else:
                            UserR+=1
                            print("Score : " , UserR , UserW)
                    if g == 2:
                        if g == r4:
                            print("OUT")
                            UserW+=1
                            print("Score : " , UserR , UserW)
                        else:
                            UserR+=2
                            print("Score : " , UserR , UserW)
                    if g == 3:
                        if g == r4:
                            print("OUT")
                            UserW+=1
                            print("Score : " , UserR , UserW)
                        else:
                            UserR+=3
                            print("Score : " , UserR , UserW)
                    if g == 4:
                        if g == r4:
                            print("OUT")
                            UserW+=1
                            print("Score : " , UserR , UserW)
                        else:
                            UserR+=4
                            print("Score : " , UserR , UserW)
                    if g == 5:
                        if g == r4:
                            print("OUT")
                            UserW+=1
                            print("Score : " , UserR , UserW)
                        else:
                            UserR+=5
                            print("Score : " , UserR , UserW)
                    if g == 6:
                        if g == r4:
                            print("OUT")
                            UserW+=1
                            print("Score : " , UserR , UserW)
                        else:
                            UserR+=6
                            print("Score : " , UserR , UserW)
print("User Score : " , UserR , "Runs" , UserW , "Wickets")
print("Computer's Target = " , UserR + 1)
f = UserW
while ComputerW < f :
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
                        ComputerW+=1
                        print("Score : " , ComputerR , ComputerW)
                    else:
                        ComputerR+=r5
                        print("Score : " , ComputerR , ComputerW)
                if h == 2:
                    if h == r5:
                        print("OUT")
                        ComputerW+=1
                        print("Score : " , ComputerR , ComputerW)
                    else:
                        ComputerR+=r5
                        print("Score : " , ComputerR , ComputerW)
        elif g!=r4:
            ComputerR+=r4
            print("Score : " , ComputerR , ComputerW)
    if g == 1:
        if g == r4:
            print("OUT")
            ComputerW+=1
            print("Score : " , ComputerR , ComputerW)
        else:
            ComputerR+=r4
            print("Score : " , ComputerR , ComputerW)
    if g == 2:
        if g == r4:
            print("OUT")
            ComputerW+=1
            print("Score : " , ComputerR , ComputerW)
        else:
            ComputerR+=r4
            print("Score : " , ComputerR , ComputerW)
    if g == 3:
        if g == r4:
            print("OUT")
            ComputerW+=1
            print("Score : " , ComputerR , ComputerW)
        else:
            ComputerR+=r4
            print("Score : " , ComputerR , ComputerW)
    if g == 4:
        if g == r4:
            print("OUT")
            ComputerW+=1
            print("Score : " , ComputerR , ComputerW)
        else:
            ComputerR+=r4
            print("Score : " , ComputerR , ComputerW)
    if g == 5:
        if g == r4:
            print("OUT")
            ComputerW+=1
            print("Score : " , ComputerR , ComputerW)
        else:
            ComputerR+=r4
            print("Score : " , ComputerR , ComputerW)
    if g == 6:
        if g == r4:
            print("OUT")
            ComputerW+=1
            print("Score : " , ComputerR , ComputerW)
        else:
            ComputerR+=r4
            print("Score : " , ComputerR , ComputerW)
    if ComputerR>UserR or ComputerW==UserW:
        break
        print("Computer Score : " , ComputerR , "Runs" , ComputerW , "Wickets")
if UserR > ComputerR:
    print("User wins by " , ComputerR - UserR , "Runs")
elif ComputerR > UserR:
    print("Computer wins by " , ComputerW - UserW , " Runs " )
if UserR > 0 and ComputerR>0:
    quit()



        


                

                
                

                

                
                

        


