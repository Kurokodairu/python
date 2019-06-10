import random

x = 0
y = 0

while(x<1):
    try:
        y = int(input("Enter number of flips: "))
        x += 1
    except:
        print("Enter a number")

totalH = 0
totalT = 0
ran = 0

for i in range(y):
    ran = random.randint(1,2)

    if(ran == 1):
        totalT += 1
    
    elif(ran == 2):
        totalH += 1
    i += 1

print("Rolled: " + str(totalT) + " Tails\n" + "Rolled: " + str(totalH) + " Heads\n")

totalSum = totalH + totalT

Tpercent = totalT / totalSum * 100
Hpercent = totalH / totalSum * 100

print(str(Tpercent)+"% Tails"+ "\t"+str(Hpercent) + "% Heads")

input("Press ENTER to continue...")
