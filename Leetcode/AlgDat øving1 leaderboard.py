import time
from datetime import timedelta




def recorsiveCheck(M, t, workingSet, usedSetKeys, backtrackList):
    #sjekker om nøkkelen har dukket opp i working set før. hvis den har det så finner man hvor den ligger og adder alle elementer etter til complete.
    #returner den fulstendige listen, i tillegg til alle de tideligere brukte plassene, separert av en -2. 
    if M[t] in usedSetKeys or M[t] == t:
        return [-1] 
    elif (M[t] not in workingSet):
        workingSet.add(M[t])
        backtrackList.append(M[t])
        return [M[t]]+recorsiveCheck(M, M[t], workingSet, usedSetKeys, backtrackList)

    else:
        for i in range(len(backtrackList)):
            backtrackList.reverse()
            if backtrackList[-1] != M[t]:
                del backtrackList[-1]
            else:
                return [-1] + backtrackList + [-2]

 

def max_permutations(M):
    # Skriv koden din her
    SetofAvailables = set(M) #Liste over alle seter som noen har lyst på. Første sjekk om key-en er mulig å komme tilbake til sete i en closed loop
    usedSetKeys = set() #liste over alle seter som har vært relatert. De kommer til å oppføre seg på samme måte hver gang så de kan ikke lage nye mønstre.
    finishedSets = set() #liste over fulført sett som skal returneres. 
    for k in range(len(M)):
        tally = 0
        workingSet = set() #en true false liste som sier om en nøkkel har dukket opp før. 
        backtrackList = [] #en liste som skal brukes av induksjonsfunksjonen til å finne ut hvor en closed loop er i en større loop
        if k in SetofAvailables and k not in usedSetKeys:
            workingSet.add(k)
            backtrackList.append(k)
            a = recorsiveCheck(M, k, workingSet, usedSetKeys, backtrackList)
            if a[-1] == -1:
                for i in a:
                    usedSetKeys.add(i)
            elif (a[-1] == -2):
                for i in a:
                    if (i == -1):
                        tally = 1
                    elif tally == 1:
                        usedSetKeys.add(i)
                        finishedSets.add(i)
    finishedSets.discard(-2)         
    #print(usedSetKeys)
    #print(finishedSets)
    return finishedSets


start_time = time.time()
max_permutations([18, 24, 2, 33, 20, 42, 15, 33, 35, 23, 18, 37, 9, 32, 29, 24, 6,
             23, 12, 29, 16, 10, 2, 42, 22, 37, 25, 28, 14, 40, 2, 31, 27, 5,
             11, 21, 29, 31, 33, 35, 12, 14, 16, 1, 44])
max_permutations([2, 0, 1, 1, 5, 4, 6])
max_permutations([
                4, 62, 24, 34, 55, 1, 57, 29, 22, 60, 21, 63, 8, 45, 46, 32, 70,
                43, 21, 45, 14, 54, 15, 64, 28, 63, 50, 35, 34, 36, 66, 7, 13,
                64, 67, 40, 21, 65, 63, 67, 47, 45, 37, 38, 8, 17, 33, 52, 19,
                1, 49, 43, 37, 58, 4, 24, 24, 53, 20, 26, 50, 12, 44, 26, 71,
                70, 53, 18, 23, 55, 72, 52, 3
            ])
max_permutations([
                56, 65, 31, 39, 46, 49, 55, 16, 55, 55, 49, 52, 10, 41, 47, 54,
                3, 15, 20, 3, 42, 65, 10, 62, 17, 42, 55, 27, 9, 37, 69, 1, 50,
                24, 41, 16, 31, 69, 20, 67, 65, 39, 64, 60, 49, 52, 14, 67, 27,
                17, 53, 60, 18, 69, 49, 0, 6, 63, 68, 2, 69, 52, 24, 20, 36, 34,
                1, 57, 45, 32
            ],)
max_permutations([46, 43, 11, 40, 35, 44, 8, 25, 30, 6, 34, 29, 19, 46, 14, 9, 19,
             29, 41, 8, 32, 4, 10, 10, 15, 35, 29, 9, 19, 11, 8, 9, 13, 4, 41,
             13, 22, 38, 5, 13, 32, 0, 2, 8, 26, 31, 37])

end_time = time.time()
print(float(end_time - start_time))

                

'''
def insertion_sort(A, n):
    # Skriv koden din her
    sortA = [A[0]]
    for i in range(1, len(A)):
        for j in range(len(sortA)):
            if A[i] <= sortA[j] or j == (len(sortA) -1):
                sortA.insert(j-1, A[i])
    return sortA
print(insertion_sort(M, 3))

'''


