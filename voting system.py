event = []
number =[]
name1 = []
name2 = []
name3 =[]
name4 = []
count1 = []
count2 = []
count3 = []
count4 = []
i =0

def Home ():
    print ("=========RAMSEY VOTING SYSTEM=========")
    print("1. input candidates")
    print("2. How to use")
    print("3. voting section")
    print("4. Check voting results ")

    vt=int(input("-->"))
    if vt ==1:
        print ("")
        voting ()
    elif vt==2:
        print("")
        howtouse()
    elif vt==3:
        print ("")
        votingsection ()
    elif vt==4:
        print ("")
        results()

    else:
        vt >4
        print (" check Home")
        Home ()


def voting ():
    global i
    e = input("what is the voting for: ")
    event.append(e)
    n = int(input("How many candidates are contesting: "))
    if n ==2:
        n1 = input("1. Name: ")
        n2 = input("2. Name: ")
        name1.append(n1)
        name2.append(n2)
        print ()

        print("below are the candidates")
        print("1- ",name1[i])
        print("2- ",name2[i])
    elif n==3:
        n1 = input("1. Name: ")
        n2 = input("2. Name: ")
        n3 = input("3. Name: ")
        name1.append(n1)
        name2.append(n2)
        name3.append(n3)
        print ()
        
        print("below are the candidates")
        print("1- ",name1[i])
        print("2- ",name2[i])
        print("3- ",name3[i])
    
    
    elif n==4:
        n1 = input("1. Name: ")
        n2 = input("2. Name: ")
        n3 = input("3. Name: ")
        n4 = input("4. Name: ")
        name1.append(n1)
        name2.append(n2)
        name3.append(n3)
        name4.append(n4)
        print ()
        
        print("below are the candidates")
        print("1- ", name1[i])
        print("2- ",name2[i])
        print("3- ",name3[i])
        print("4- ",name4[i])
    else:
        n>4
        print ("candidates cannot exceed 4 ")
        voting ()
    print ()
    bc = int(input("0-back n\ -->"))
    if bc == 0:
        Home ()
    else:
        exit ()
def votingsection ():
    print (" VOTING SECTION")
    mm = int(input("How many candidates contested: "))
    print("below are the candidates")
    if mm ==2:
        print("1- ", name1[i])
        print("2- ", name2[i])
    elif mm ==3:
        print("1- ", name1[i])
        print("2- ",name2[i])
        print("3- ",name3[i])
    elif mm ==4:
        print("1- ", name1[i])
        print("2- ",name2[i])
        print("3- ",name3[i])
        print("4- ",name4[i])
    else:
        mm > 4
        print ("Number of candidates does not  exist")
    print ()
    print ("Start voting ")
    print ("Enter 5 to  End vote section")
    while 1:
        vtt = int(input("who are you voting for: "))
        if vtt ==1:
            count1.append(vtt)
        elif vtt ==2:
            count2.append(vtt)
        elif vtt ==3:
            count3.append(vtt)
        elif vtt ==4:
            count4.append(vtt)
        elif vtt>5:
            print ("candidate does not exist")
            Home ()
        else:
            vtt==5
            print (" Thanks for your votes")
            break  
    bc = int(input("0-backn\-->"))
    if bc == 0:
        Home ()
    else:
        exit ()

def results():
    global i
    print ("=======RAMSEY VOTING SYSTEM======")
    print ("VOTING RESULTS")
    print ("Voting For: ",event[i])
    print ()
    mmm = int(input("How many candidates contested: "))
    if mmm == 2:
        print ("--------------------------------")
        print ("Candidate 1: ", name1[i])
        print ("Vote count: ",len(count1))
        print ()
        print("--------------------------------")
        print ("Candidate 2: ", name2[i])
        print ("Vote count: ",len(count2))
        print ()
        print ("--------------------------------")
    elif mmm==3:
        print ("--------------------------------")
        print ("Candidate 1: ", name1[i])
        print ("Vote count: ",len(count1))
        print ()
        print("--------------------------------")
        print ("Candidate 2: ", name2[i])
        print ("Vote count: ",len(count2))
        print ()
        print ("--------------------------------")
        print ("Candidate 3: ", name3[i])
        print ("Vote count: ",len(count3))
        print ()
        print ("---------------------------------")
    elif mmm==4:
        print ("--------------------------------")
        print ("Candidate 1: ", name1[i])
        print ("Vote count: ",len(count1))
        print ()
        print("--------------------------------")
        print ("Candidate 2: ", name2[i])
        print ("Vote count: ",len(count2))
        print ()
        print ("--------------------------------")
        print ("Candidate 3: ", name3[i])
        print ("Vote count: ",len(count3))
        print ()
        print ("---------------------------------")
        print ("Candidate 4: ", name4[i])
        print ("Vote count: ",len(count4))
        print ()
        print ("---------------------------------")
    else:
        mmm !=("2,3,4")
        print ("Number of candidates does not  exist")
        print ()
        
    if len(count1)==len(count2)>len(count3) or len(count2)==len(count3)>len(count1) or len(count1)==len(count3)>len(count2) or len(count1)==len(count2)>len(count3)>len(count4) or len(count2)==len(count3)>len(count1)>len(count4) or len(count3)==len(count4)>len(count1)>len(count2):
        print(" 2 candidates got equal votes")
        print(" a bye-election can be conducted")
    elif len(count1)>len(count2)>len(count3)>len(count4) or len(count1)>len(count2)>len(count3) or len(count1)>len(count2):
         print ("Candidate 1: ", name1[i], end="")
         print (" wins the elecetion")
    elif  len(count2)>len(count1)>len(count3)>len(count4) or len(count2)>len(count1)>len(count3) or len(count2)>len(count1):
        print ("Candidate 2:", name2[i], end="")
        print ("  wins the election")
    elif  len(count3)>len(count2)>len(count1)>len(count4) or len(count3)>len(count1)>len(count2):
        print ("Candidate 3: ", name3[i], end="")
        print (" wins the election")
    elif  len(count4)>len(count1)>len(count2)>len(count3) :
        print ("Candidate 4: ", name4[i], end="")
        print (" wins the election")
    elif len(count1)==len(count2)>len(count3) or len(count2)==len(count3)>len(count1) or len(count1)==len(count3)>len(count2) or len(count1)==len(count2)>len(count3)>len(count4) or len(count2)==len(count3)>len(count1)>len(count4) or len(count3)==len(count4)>len(count1)>len(count2):
        print(" 2 candidates got equal votes")
        print(" a bye-election can be conducted")
    elif len(count1)==len(count2)==len(count3)>len(count4) or len(count1)==len(count2)==len(count4)>len(count3) or len(count2)==len(count3)==len(count4)>len(count1):
        print("3 candidates got equal votes")
        print("a bye-election can be conducted")
    else:
        len(count1)==len(count2)==len(count3)==len(count4) or len(count1)==len(count2) or len(count1)==len(count2)==len(count3) 
        print (" All candidates got equal votes")
        print (" A bye-election can be conducted")
    print ()
    bc = int(input("0-backn\-->"))
    if bc == 0:
        Home ()
    else:
        exit ()

def howtouse ():
    print("========== RAMSEY VOTING SYSTEM ===========")
    print("Read the following guidelines ")
    print()
    print("HOW TO INPUT CANDIDATES NAMES")
    print("-->")
    print("*. First choose the 1 memu in Home( input candidates names)")
    print("input the reason for the voting")
    print("example: ")
    print("--")
    print("'position for director of welfare' ")
    print("*. Second input the number of candidates contesting for the position")
    print("NOTE-->")
    print("candidates cannot exceed 4 and cannot be 1")
    print("input the candidates names")
    print("----------------------------------------------------------------------------------")
    print()
    print("Voting Section")
    print("- For people to start voting first input the number of candidates that contested")
    print("- The names of the candidates will be displayed")
    print("- people can start voting by inputing the number for each of the candidates")
    print("depending on who they want to vote for")
    print("-----------------------------------------------------------------------------------")
    print()
    print("voting results")
    print("input the number of candidates that contested")
    print("Results of candidates will be shown and the winner of the election would be declared")
    print()
    print("Thank you. Head over to home")
    bc = int(input("0-backn\-->"))
    if bc == 0:
        Home ()
    else:
        exit ()
    
    

Home ()

    
    
        
        
    



