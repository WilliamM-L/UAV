from random import randint                  #to generate random arrays

def getInput():
    return int(input('Enter your guess! '))          #input only returns a string!!! use int() to make it work!

def decompose(num):
    output = [9,9,9,9]
    output[3] = int(num%10)          #for some reason this expression becomes a double, probably related to how I don't specify data types
    output[2] = int(num%100/10)
    output[1] = int(num%1000/100)
    output[0] = int(num/1000)
    return output

def findCows(referenceList,testedList):
    cowsFound = 0;
    for index in range(4):
        if(referenceList[index]==testedList[index]):
            cowsFound+=1
            #cows++ doesn't work @SHOOKETH@
    return cowsFound

def rectifyList(referenceList,testedList, landfill):          #dummy! You had this problem for a java assignment back in college, you must create a new array!!!
    newReferenceList = [0,0,0,0] #new array that will be returned
    for index in range(4):
        if(referenceList[index]==testedList[index]):
            newReferenceList[index] = landfill
        else:
            newReferenceList[index] = referenceList[index]
            #this changes it so findBulls won't detect it.
    #print('The array returned is now: ')
    #print(newReferenceList)
    return newReferenceList    

def findBulls(referenceList,testedList):
    bullsFound = 0      #if the bull is found, replace referenceList[i] with some garbage so that we don't get extra bulls!
    for index in range(4):  #nested for loops
        for x in range(4):
            if(testedList[index] == referenceList[x]):
                bullsFound+=1
                referenceList[x] = -1
                testedList[index] = -2
                #print('While finding bulls, the array has become: ')
                #print(referenceList)
    return bullsFound


print("Let's plays a game! It's called Cows and Bulls!")

#generate a list which contains random four digit number
random = [0,0,0,0]
userList = [0,0,0,0] # instantiating list used later
for index in range(4):
    random[index] = randint(0,9)
    
print(random)
#until arrays are the same
while(True):
    userInput = getInput()
    userList = decompose(userInput)
    cows = findCows(random,userList)
    rectifiedRandom = rectifyList(random,userList,-1)
    rectifiedUserList = rectifyList(userList,random,-2)
    #print('rectifiedRandom is : ')
        #print(rectifiedRandom) #random has changed for some reason
    bulls = findBulls(rectifiedRandom, rectifiedUserList)
    print(str(cows) +" Cow(s)")
    print(str(bulls) + " Bull(s)")                #prints none if there are zero of them!
    if(cows==4):                                        #no do-while loops! @SHOOKETH@
        break


# in while loop, loop as long as it needs to have correct match
print('Bravo!')
