def sumLst(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return(total)

def calcX(lst,n):
    numerator = 0
    for i in range(len(lst)):
        numerator += ((3**i)*(2**(sumLst(lst[i+1:n]))))
    denominator = 2**(sumLst(lst)) - 3**n
    return(float(numerator)/float(denominator))
n = 0
lst = []
count = 0
while True:
    n += 1
    for i in range(n-1):
        lst[i] = 0
    lst.append(0)
    index = -1
    finished = False
    while finished == False:
        while True:
            count += 1
            if count % 100000 == 0:
                print("Check")
            index += 1
            for i in range(0,index):
                lst[i] = 0
            lst[index] += 1
            x = calcX(lst, n)
            if x > 0 and x == float(x//1):
                print(lst,int(x))
            if x > 0 and x < (((3**(index)-1)/2)//1)+1:
                if index == n-1:
                    finished = True
                break
            else:
                index = -1


