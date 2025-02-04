#MARK: Imports

from time import sleep

#MARK: Functions
def isPrime(numberToCheck)->bool:
    if numberToCheck == 0 or numberToCheck == 1:
        return False
    # noinspection PyArgumentList
    for i in range(2, int((numberToCheck/2)+1)):
        if numberToCheck%i == 0:
            return False
    return True
"""Checks if a number is prime by trying to divide it cleanly by all numbers from to to itself -1"""


def isListPrime(listToCheck:list):
    for i in listToCheck:
        if not isPrime(i):
            return False
    return True
"""Checks if all numbers in a list are prime by seeing if each number in it is prime(using the isPrime() function)"""


# noinspection PyArgumentList
def primeFactorisation(numberToFactorise):
    startList = [numberToFactorise]
    while not isListPrime(startList):#While the list containing the (prime) factors is not completely made of primes
        for i in startList:
            if not isPrime(i):#If i isn't prime, it finds something to divide it by
                for d in range(2, int((i/2)+1)):
                    if i%d == 0:
                        startList.remove(i)
                        startList.append(d)
                        startList.append(int(i/d))
                        break
    return startList
"""Returns all prime factors of a given number as integers in a list. For example, primeFactorisation(8) would return [2, 2, 2]"""


# noinspection PyArgumentList
def multiples(number, maximumNumber):
    numbList = [number * i for i in range(1, maximumNumber + 1)]
    return numbList
"""Returns the multiples of a dNum as integers in a list. The multiples go from dNum to dNum*mNum"""


def factors(number):
    # noinspection PyArgumentList
    numbeList = [i for i in range(1, int((number/2)+1)) if number % i == 0]
    return numbeList
"""Returns all factors of numbe as integers in a list."""


def lcmAndHCF(firstNum, allNumbers):
    HCF = 1
    LCM = 1
    allFactorLists = [primeFactorisation(number) for number in allNumbers]
    firstNumFactorList = primeFactorisation(firstNum)
    commonPrimeFactors = []
    for z in firstNumFactorList.copy():
        if all(z in factorList for factorList in allFactorLists):
            commonPrimeFactors.append(z)
            for factorList in allFactorLists:
                factorList.remove(z)
            firstNumFactorList.remove(z)
    for blablabla in commonPrimeFactors:
        HCF *= blablabla
    LCM = HCF
    for factorList in allFactorLists:
        for factor in factorList:
            LCM *= factor
    for factor in firstNumFactorList:
        LCM *= factor
    return {"HCF": HCF,
            "LCM": LCM}
"""Returns the HCF and LCM of firstNum and the numbers in the list allNumbers"""

def primesUpTo(upperLimit, lowerLimit=0):
    allPrimesToLimit = []
    # noinspection PyArgumentList
    for i in range(lowerLimit, upperLimit + 1):
        if isPrime(i):
            allPrimesToLimit.append(i)
    return allPrimesToLimit
"""Returns all primes from lowerLimit to upperLimit as integers in a list"""


#MARK: Mainloop
on = True
while on:

    try:#In case a user types a letter instead of a number
        whatDo = int(input("Press 1 for the multiples of a number, 2 for the factors of a number, 3 to check if a number is prime, 4 to search for the primes between two numbers, 5 for prime factorisation, 6 for LCM and HCF: \n"))
    except ValueError:
        print("Please enter a valid number from the list of options above\n")
        sleep(4)
        continue
    print("\n")

    #MARK: Multiples
    if whatDo == 1:
         num = int(input("What number would you like to find the multiples of?\n"))
         print("\n")
         maxNum = int(input("What number would you like to multiply up to?\n"))
         print("\n")

         numList = multiples(num, maxNum)
         outputList = [str(num) for num in numList]
         outputList = ', '.join(outputList)

         x = input(f"Here are all the multiples {outputList}\nWould you like to do somthing else('N' to exit the program or anything else to continue)?\n").lower()
         if x == "n":
             on = False
         else:
             pass

    #MARK: Factors
    elif whatDo == 2:
        num = int(input("What number would you like to find the factors of?\n"))
        print("\n")

        # noinspection PyArgumentList
        numList = factors(num)
        outputList = [str(num) for num in numList]
        outputList = ', '.join(outputList)

        x = input(f"Here are all the factors {outputList}\nWould you like to do somthing else('N' to exit the program or anything else to continue)?\n").lower()
        if x == "n":
            on = False
        else:
            pass


    #MARK: Check if a number is prime
    elif whatDo == 3:

        num = int(input("Which number would you check to see if it's prime?\n"))
        print("\n")

        #NOTE: If num is prime
        if isPrime(num):

            x = input(f"{num} is prime.\nWould you like to do somthing else('N' to exit the program or anything else to continue)?\n").lower()
            if x == "n":
                on = False
            else:
                pass

        #NOTE: If num isn't prime
        elif not isPrime(num):

            x = input(f"{num} isn't prime.\nWould you like to do somthing else('N' to exit the program or anything else to continue)?\n").lower()
            if x == "n":
                on = False
            else:
                pass


    #MARK: Primes from l to u
    elif whatDo == 4:
        l = int(input("What is your lower limit(eg. 100 in 100-200)?\n"))
        u = int(input("What is your upper limit(eg. 200 in 100-200)?\n"))
        p = primesUpTo(u, l)
        p = [str(num) for num in p]
        x = input(f"The primes from {l} to {u} are{"\n".join(p)}.\nWould you like to do somthing else('N' to exit the program or anything else to continue)?\n").lower()
        if x == "n":
            on = False
        else:
            pass


    #NOTE: Find the prime factors of a number
    elif whatDo == 5:
        num = int(input("Which number would you like to see the prime factors of?\n"))
        print("\n")

        a = primeFactorisation(num)
        b = [str(z) for z in a]
        c = ', '.join(b)

        x = input(f"The prime factor(s) of {num} is/are {c}.\nWould you like to do somthing else('N' to exit the program or anything else to continue)?\n").lower()
        if x == "n":
            on = False
        else:
            pass


    #NOTE: HCF and LCM
    elif whatDo == 6:

        moreNumbersFromUserInput = True
        allInputtedNumbers = []
        a = int(input("What is your first number?\n"))
        b = int(input("What is your second number?\n"))

        while moreNumbersFromUserInput:
            newNumber = input("Enter a number to find its HCF and LCM along with the others, or enter anything else to calculate the HCF and LCM of your chosen numbers.")
            try:
                allInputtedNumbers.append(int(newNumber))
            except ValueError:
                print("Calculating...\n")
                moreNumbersFromUserInput = False

        allInputtedNumbers.append(b)
        lcmHCF = lcmAndHCF(a, allInputtedNumbers)
        allInputtedNumbers.append(a)
        allInputtedNumbers.sort()
        a = allInputtedNumbers[len(allInputtedNumbers) - 1]
        allInputtedNumbers.pop(len(allInputtedNumbers) - 1)
        allInputtedNumbers = [str(x) for x in allInputtedNumbers]
        #Most of the above code is for the purpose of proper grammar in the input() statement below

        x = input(f"The HCF and LCM of {', '.join(allInputtedNumbers)} and {a} are {lcmHCF["HCF"]} and {lcmHCF["LCM"]}.\nWould you like to do something else('N' to exit the program or anything else to continue)").lower()
        if x == "n":
            on = False
        else:
            pass


    else:
        print("Please choose a valid option")
        sleep(4)
        print("\n"*2)