import time

#change file handling for your files, if it differs on upload.

KnownNumbersFile = open("KnownNumbers.txt","r")
Numbers = KnownNumbersFile.readlines()
KnownNumbers = []
for i in Numbers:
    number = i.strip('\n')
    number = int(number)
    KnownNumbers.append(number)

TuplesTestedFile = open("TuplesTested.txt","r")
Tuples = TuplesTestedFile.readlines()
TuplesTested = []
for string in Tuples:
    string = string.strip('\n')
    number_list = string.split(",")
    newlist = []
    for number in number_list:
        if number.isdigit() == True:
            newlist.append(int(number))
    TuplesTested.append(newlist)

GoodTuples = []
DistinctNonTrivialTuples = []
TrivialNumbers1 = []
TrivialNumbers2 = []
TrivialNumbers8 = []
TrivialNumbers16 = []

#NonTrivial Finder

def TupleTester(TupleToTest):
    n = len(TupleToTest)
    numerator = 0
    for i in range(1,n+1):
        three = 3**(n-i)
        power_sum = 0
        for j in range(0,i):
            if j != 0:
                power_sum += TupleToTest[j-1]
            else:
                power_sum += 0
        numerator += three*(2**power_sum)
    denominator = 0
    power_sum = 0
    for i in range(0,n):
        power_sum += TupleToTest[i]
    denominator = (2**power_sum) - (3**n)
    number = numerator/denominator
    return number

def bitwise(lst):
    lst = list(lst)
    lst.append(lst[0])
    lst.pop(0)
    return lst

def reflect(tupl):
  newtupl = []
  for i in range(len(tupl)-1,-1,-1):
    newtupl.append(tupl[i])
  return(newtupl)

def Rotate_Tuple_Family(tupl):
    tupl = list(tupl)
    Family = []
    for i in range(0,len(tupl)):
        Family.append(tupl)
        tupl = bitwise(tupl)
    return Family

def Finder(tupl):
    Family = Rotate_Tuple_Family(tupl)
    gothrough = 0
    if tupl not in TuplesTested:
        gothrough = 1
        for i in Family:
            TuplesTested.append(i)
    x = TupleTester(Family[0])
    if gothrough == 1:
        if x.is_integer() == True and x > 0:
            g_numbers = [int(x)]
            for i in range(1,len(Family)):
                g_numbers.append(int(TupleTester(Family[i])))
            theend = str(tupl)
            string = str(g_numbers) + " | " + theend
            #rotation = False
            DistinctNonTrivialTuples.append(string)
            for i in g_numbers:
                if i not in KnownNumbers:
                    KnownNumbers.append(i)
            for i in Family:
                if i not in GoodTuples:
                    GoodTuples.append(i)
    return x, Family

def SPEED():
    elapsed = False
    now = time.time()
    timer = int(input("After how long would you like to stop?\n"))
    n = 1
    tupl = [0]
    while elapsed == False:
        n += 1
        for i in range(n-1):
            tupl[i] = 0
        tupl.append(0)
        index = -1
        finished = False
        while finished == False and elapsed == False:
            while elapsed == False:
                if (time.time()-now)//1 >= timer:
                    elapsed = True
                #time.sleep(0.1)
                index += 1
                for i in range(0,index):
                    tupl[i] = 0
                tupl[index] += 1
                x, Family = Finder(reflect(tupl))
                #print(x)
                if x > 0 and x == float(x//1):
                    print(reflect(tupl),int(x))
                if x > 0 and x < ((3**(index)/2)//1)+1:
                    if index == n-1:
                        finished = True
                    break
                else:
                    index = -1

#TrivialFinder

def Collatz(n, i, seednum):
    powers = []
    for x in range(i - 1):
        powers.append(0)
    count = 0
    power_of_two = 0
    while n != seednum:
        if len(str(bin(n))) == len(str(bin(n - 1))) + 1:
            power_of_two += 1
        if n % 2 == 0:
            n = n // 2
            count += 1
        else:
            n = 3 * n + 1
            powers.append(count)
            count = 0
        if n not in KnownNumbers:
            KnownNumbers.append(n)
    powers.append(power_of_two)
    return powers

#This should find loops, and store new results into their trivial.txt files, KnownNumbers, and TupleTests.
def TrivialLoopFinder(seednum, beginnum, endnum):
    a = seednum
    mem = str(a)
    for k in range(1,beginnum):
        a = 3*a + 1
    for i in range(beginnum, endnum):
        a = 3*a + 1
        string = str(i) + ": " + mem + " -> ... -> " + str(a) + " ->...-> " + mem + " | "
        powers = Collatz(a, i, seednum)
        if powers not in TuplesTested:
            Family = Rotate_Tuple_Family(powers)
            for a_tuple in Family:
                TuplesTested.append(a_tuple)
                GoodTuples.append(a_tuple)
        string += str(powers)
        #print(str(i) + " is done \n")
        if (string not in TrivialNumbers1) and (seednum == 1):
            TrivialNumbers1.append(string)
        if (string not in TrivialNumbers2) and (seednum == 2):
            TrivialNumbers2.append(string)
        if (string not in TrivialNumbers8) and (seednum == 8):
            TrivialNumbers8.append(string)
        if (string not in TrivialNumbers16) and (seednum == 16):
            TrivialNumbers16.append(string)

def Trivial():
    while True:
        seednum = int(input("Please choose 1,2,8 or 16. Else, select another number\n"))
        if (seednum == 1) or (seednum == 2) or (seednum == 8) or (seednum == 16):
            while True:
                beginnum = int(input("Please choose a beginning positive integer\n"))
                if beginnum > 0:
                    break
            while True:
                endnum = int(input("Please choose an ending positive integer\n"))
                endnum += 1
                if endnum > beginnum:
                    break
            TrivialLoopFinder(seednum, beginnum, endnum)
        else:
          break

def Delete():
    with open('1Trivial.txt', 'w') as f:
        f.write("")
    with open('2Trivial.txt', 'w') as f:
        f.write("")
    with open('8Trivial.txt', 'w') as f:
        f.write("")
    with open('16Trivial.txt', 'w') as f:
        f.write("")
    #---------------------------------------------------
    with open('KnownNumbers.txt', 'w') as f:
        f.write("")
    with open('TuplesTested.txt', 'w') as f:
        f.write("")
    with open('GoodTuples.txt', 'w') as f:
        f.write("")
    with open('NonTrivialTuples.txt', 'w') as f:
        f.write("")


def Menu():
    while True:
        option = int(input("Please choose 0 for NonTrivial Finder, 1 for Trivial Finder, or 2 for File Delete: "))
        if option == 0:
            SPEED()
        elif option == 1:
            Trivial()
        elif option == 2:
            Delete()
        else:
            break
          
Menu()

#change file handling for your files, if it differs on upload.

with open('Results/1Trivial.txt', 'a') as f:
    for item in TrivialNumbers1:
        f.write("%s\n" % item)
with open('Results/2Trivial.txt', 'a') as f:
    for item in TrivialNumbers2:
        f.write("%s\n" % item)
with open('Results/8Trivial.txt', 'a') as f:
    for item in TrivialNumbers8:
        f.write("%s\n" % item)
with open('Results/16Trivial.txt', 'a') as f:
    for item in TrivialNumbers16:
        f.write("%s\n" % item)
#---------------------------------------------------
with open('Results/KnownNumbers.txt', 'w') as f:
    for item in sorted(KnownNumbers):
        f.write("%s\n" % item)
with open('Results/TuplesTested.txt', 'w') as f:
    for item in TuplesTested:
        for number in range(0,len(item)):
            if number == len(item)-1:
                f.write('%s\n' % item[number])
            else:
                f.write('%s,' % item[number])

with open('Results/GoodTuples.txt', 'w') as f:
    for item in GoodTuples:
        for number in range(0,len(item)):
            if number == len(item)-1:
                f.write('%s\n' % item[number])
            else:
                f.write('%s,' % item[number])
with open('Results/NonTrivialTuples.txt', 'w') as f:
    for item in DistinctNonTrivialTuples:
        f.write("%s\n" % item)
