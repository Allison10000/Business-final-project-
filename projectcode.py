dominantfoot = "right"
dominanthand = "right"
footmark = 0
target = 0
outcome = " "

#function for all inputted data to run through the clean it
def cleandata(value):
    for i in ["$", ",", " "]:
        value = value.replace(i,"")
    return float(value)
#finction that deals with spares
def spareadjustment(remainingpinnumbers15):
    global footmark, target
    for i in range(len(remainingpinnumbers15)):
        if remainingpinnumbers15[i] in ["1", "3", "5", "7", "9"]:
            footmark = footmark + 2
            target = target + 1
        elif remainingpinnumbers15[i] in ["2", "4", "6", "8"]:
            footmark = footmark - 2
            target = target - 1
    print("your spare footmark is", footmark)
    print("your spare target is", target)
#function that deals with the event of impossible marks
def zeroerror():
    global footmark, target
    #arrow too far right
    if target < 0:
        target = 5
        footmark = footmark + 10
    #arrow too far left
    elif target > 39:
        target = 35
        footmark = footmark - 10
    #standing too far right
    if footmark < 0:
        footmark = 1
        target = target +5
    #standing too far left 
    elif footmark > 39:
        footmark = 38
        target = target - 5 
    if target < 0:
        target = 5
        footmark = footmark + 10
    #arrow too far left
    elif target > 39:
        target = 35
        footmark = footmark - 10
    if footmark < 0:
        footmark = 1
        target = target +5
    #standing too far left 
    elif footmark > 39:
        footmark = 38
        target = target - 5 
#inputting conditions 
def setvalues():
    dominantfoot = input("what foot do you base your foot mark on(right or left)? ")
    if dominantfoot in ["right", "Right", "RIGHT", "R"]:
        dominantfoot = "right"
    else:
        dominantfoot = "left"
    dominanthand = input("are you right or left handed? *right now I only have right hand working? ")
    if dominanthand in ["right", "Right", "RIGHT", "R"]:
        dominanthand = "right"
    else:
        dominanthand = "left"
def eachthrowadjustment():
    global footmark, target, outcome
    footmark = footmark + (2*outcome)
    target = target + outcome
    zeroerror()
    print(" ")
    print(" ")
    print("your new foot mark is: ", footmark)
    print("your new target is: ", target)
    print(" ")
    print(" ")
#main function for each frame
def eachball(value1,value2):
    global footmark, target, outcome
    #strikes
    if input("did you make the strike? (yes/no): ") in ["yes", "Yes", "YES", "yes ", " yes", "y", "Y"]:
        print("congrats, on to next frame")
        value1 = "N/A"
        value2 = "strike"
        outcome = 0.0
        return
    #spares
    else:
        #getting outcome for next throw
        print(" ")
        print("what was the outcome of your throw?")
        print("******************************************************")
        print(" - far left                           - far right ")
        print("                                   - low pocket")
        print("    - low brooklyn               - in the pocket")
        print("       - high brooklyn        - high pocket")
        print("              - straight on head pin")
        print("******************************************************")
        print(" ")
        outcome = input("outcome: ")
        print(" ")
        if outcome in ["far left", "Far Left", "FAR LEFT", "far left ", " far left"]:
            outcome = 13.0
        elif outcome in ["far right", "Far Right", "FAR RIGHT", "far right ", " far right"]:
            outcome = -5.0
        elif outcome in ["low pocket", "Low Pocket", "LOW POCKET", "low pocket ", " low pocket"]:
            outcome = -2.0
        elif outcome in ["in the pocket", "In The Pocket", "IN THE POCKET", "in the pocket ", " in the pocket"]:
            outcome = 0.0
        elif outcome in ["high pocket", "High Pocket", "HIGH POCKET", "high pocket ", " high pocket"]:
            outcome = 2.0
        elif outcome in ["straight on head pin", "Straight On Head Pin", "STRAIGHT ON HEAD PIN", "straight on head pin ", " straight on head pin"]:
            outcome = 4.0
        elif outcome in ["low brooklyn", "Low Brooklyn", "LOW BROOKLYN", "low brooklyn ", " low brooklyn"]:
            outcome = 10.0
        elif outcome in ["high brooklyn", "High Brooklyn", "HIGH BROOKLYN", "high brooklyn ", " high brooklyn"]:
            outcome = 6.0
        #getting spare 
        pinsremaining = input("what pins are remaining? (type the numbers of the pins that are remaining with no spaces)")
        value1 = 10 - float(len(pinsremaining))
        print(" ")
        spareadjustment(pinsremaining)
        #spare outcome
        if input("did you make the spare? (yes/no): ") in ["yes", "Yes", "YES", "yes ", " yes", "y", "Y"]:
            print("congrats, on to next frame")
            value2 = "spare"
        else:
            value2 = float(input("how many pins are still standing after your second throw? "))
        return


#version 2
#with this second method I will indavidual functions for each frame to avoid the issue I was having in the last version
#with repeating global functions of the two overall functions not working for scoring, or marks
first1 = 0
second1 = 0
first2 = 0 
second2 = 0
first3 = 0
second3 = 0
first4 = 0
second4 = 0
first5 = 0
second5 = 0    
first6 = 0
second6 = 0
first7 = 0
second7 = 0
first8 = 0
second8 = 0
first9 = 0
second9 = 0
first10 = 0
second10 = 0    
additional10 = 0
def firstframe ():
    print("first frame: take your first throw then record first results")
    eachball(first1,second1)
    print(" ")
def secondframe ():
    print("second frame: take your first throw then record first results")
    eachthrowadjustment()
    eachball(first2,second2)
    print(" ")
def thirdframe ():
    print("third frame: take your first throw then record first results")
    eachthrowadjustment()
    eachball(first3,second3)
    print(" ")
def fourthframe ():
    print("fourth frame: take your first throw then record first results")
    eachthrowadjustment()
    eachball(first4,second4)
    print(" ")
def fifthframe ():
    print("fifth frame: take your first throw then record first results")
    eachthrowadjustment()
    eachball(first5,second5)
    print(" ")
def sixthframe (): 
    print("sixth frame: take your first throw then record first results")
    eachthrowadjustment()
    eachball(first6,second6)
    print(" ")
def seventhframe ():
    print("seventh frame: take your first throw then record first results")
    eachthrowadjustment()
    eachball(first7,second7)
    print(" ")
def eighthframe ():
    print("eighth frame: take your first throw then record first results")
    eachthrowadjustment()
    eachball(first8,second8)
    print(" ")
def ninthframe ():
    print("ninth frame: take your first throw then record first results")
    eachthrowadjustment()
    eachball(first9,second9)
    print(" ")
def tenthframe ():
    print("tenth frame: take your first throw then record first results")
    eachthrowadjustment()
    eachball(first10,second10)
    print(" ")
def scorecalculation():
    global first1, second1, first2, second2, first3, second3, first4, second4, first5, second5, first6, second6, first7, second7, first8, second8, first9, second9, first10, second10, additional10
    scorelist = [first1, second1, first2, second2, first3, second3, first4, second4, first5, second5, first6, second6, first7, second7, first8, second8, first9, second9, first10, second10]
    totalscore = 0
    for i in range(len(scorelist)):
        if scorelist[i] == "strike":
            totalscore = totalscore + 10
            if scorelist[i+1] == "strike":
                totalscore = totalscore + 10
                totalscore = totalscore + scorelist[i+2]
            else:
                totalscore = totalscore + scorelist[i+1]
        elif scorelist[i] == "spare":
            totalscore = totalscore + 10-scorelist[i-1]
            if scorelist[i+1] == "strike":
                totalscore = totalscore + 10
            else:
                totalscore = totalscore + scorelist[i+1]
        else:
            totalscore = totalscore + scorelist[i]
def main():
    #setvalues()
    footmark = cleandata(input("what is the foot mark that you are currently using? "))
    target = cleandata(input("what mark are you aiming for currently at the first arrow level? "))
    firstframe()
    secondframe()
    thirdframe()
    fourthframe()
    fifthframe()
    sixthframe()
    seventhframe()
    eighthframe()
    ninthframe()
    tenthframe()
    scorecalculation()
main()
