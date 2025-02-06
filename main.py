#MARK: Imports----------------------------------------------------------------------------------------------------------
from time import sleep, time

#MARK: Functions--------------------------------------------------------------------------------------------------------
def isPrime(numberToCheck)->bool:
    if numberToCheck <= 1:
        return False
    if type(numberToCheck) == float:
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
    startList.sort()
    return startList
"""Returns all prime factors of a given number as integers in a list. For example, primeFactorisation(8) would return [2, 2, 2]"""



# noinspection PyArgumentList
def multiples(number, maximumNumber):
    numbList = [number * i for i in range(1, maximumNumber + 1)]
    numbList.sort()
    return numbList
"""Returns the multiples of a dNum as integers in a list. The multiples go from dNum to dNum*mNum"""



def factors(number):
    # noinspection PyArgumentList
    numbeList = [i for i in range(1, int((number/2)+1)) if number % i == 0]
    numbeList.append(number)
    numbeList.sort()
    return numbeList
"""Returns all factors of numbe as integers in a list."""



def lcmAndHCF(lastNum, allNumbers):
    HCF = 1
    LCM = 1
    allFactorLists = [primeFactorisation(number) for number in allNumbers]
    firstNumFactorList = primeFactorisation(lastNum)
    commonPrimeFactors = []

    for firstNumFactor in firstNumFactorList.copy():
        if all(firstNumFactor in factorList for factorList in allFactorLists):
            commonPrimeFactors.append(firstNumFactor)
            for factorList in allFactorLists:
                factorList.remove(firstNumFactor)
            firstNumFactorList.remove(firstNumFactor)

    for commonPrimeFactor in commonPrimeFactors:
        HCF *= commonPrimeFactor #Finds HCF by multiplying all the comm on
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
    start = time()
    allPrimesToLimit = []
    # noinspection PyArgumentList
    for i in range(lowerLimit, upperLimit + 1):
        if isPrime(i):
            allPrimesToLimit.append(i)

    end = time() #ChatGPT
    timeTaken = end-start#ChatGPT
    # Convert to hours, minutes, seconds, and fractional seconds
    hours = int(timeTaken // 3600)  #ChatGPT
    minutes = int((timeTaken % 3600) // 60)  #ChatGPT
    seconds = int(timeTaken % 60)  #ChatGPT
    milliseconds = (timeTaken % 1) * 1000000  #ChatGPT
    formatted_time = f"Time taken:  {hours}:{minutes}:{seconds}.{int(milliseconds)}"

    print(formatted_time)
    allPrimesToLimit.sort()
    return allPrimesToLimit
"""Returns all primes from lowerLimit to upperLimit as integers in a list"""



#MARK: Mainloop---------------------------------------------------------------------------------------------------------
FMP = True
while FMP:
    try:#In case a user types a letter instead of a number
        whatDo = int(input("""
Choose an option:
    1: Multiples
    2: Factors
    3: Prime Check
    4: Primes in Range
    5: Prime Factorization
    6: LCM and HCF
Enter choice: """))
    except ValueError:
        print("Please enter a valid number from the list of options above\n")
        continue
    print("\n")


    #MARK: Multiples----------------------------------------------------------------------------------------------------
    if whatDo == 1:
        on = True
        while on:

            invalidChar = True
            while invalidChar:
                try:
                    num = int(input("What number would you like to find the multiples of?\n"))
                except ValueError:
                    print("Invalid number, please try again\n")
                    continue
                else:
                    invalidChar = False

            print("\n")
            invalidChar = True
            while invalidChar:
                try:
                    maxNum = int(input("What number would you like to multiply up to?\n"))
                except ValueError:
                    print("Invalid number, please try again\n")
                else:
                    invalidChar = False

            print("\n")

            multipleList = [str(num) for num in multiples(num, maxNum)]
            

            if len(multipleList) == 1:
                goAgain = input(f"The multiple of {num} to {maxNum} is {multipleList[0]}.\nWould you like to find the multiples of a number again('Y') or would you like to do somthing else(Anything but 'Y')?\n").lower()
            else:
                lastMultiple = multipleList[len(multipleList) - 1]
                multipleList.remove(lastMultiple)
                multipleList = ', '.join(multipleList)
                goAgain = input(f"The multiples of {num} up to {maxNum} are {multipleList} and {lastMultiple}.\nWould you like to find the multiples of a number again('Y') or would you like to do somthing else(Anything but 'Y')?\n")


            if goAgain == "y":
                continue
            else:
                on = False

    #MARK: Factors------------------------------------------------------------------------------------------------------
    elif whatDo == 2:
        on = True
        while on:

            invalidChar = True
            while invalidChar:
                try:
                    num = int(input("What number would you like to find the factors of?\n"))
                except ValueError:
                    print("Invalid number, please try again.\n")
                else:
                    invalidChar = False

            print("\n")
            # noinspection PyArgumentList
            factorList = factors(num)
            factorList = [str(num) for num in factorList]

            lastMultiple = factorList[len(factorList) - 1]
            factorList.remove(lastMultiple)
            factorList.sort()
            factorList = ', '.join(factorList)
            goAgain = input(f"The factors of {num} are {factorList} and {lastMultiple}.\nWould you like to find the factors of a number again('Y') or would you like to do somthing else(Anything but 'Y')?\n")

            if goAgain == "y":
                continue
            else:
                on = False


    #MARK: Check if a number is prime-----------------------------------------------------------------------------------
    elif whatDo == 3:
        on = True
        while on:

            invalidChar = True
            while invalidChar:
                try:
                    num = int(input("Which number would you check to see if it's prime?\n"))
                except ValueError:
                    print("Invalid number, please try again.\n")
                else:
                    invalidChar = False

            print("\n")

            #NOTE: If num is prime
            if isPrime(num):

                goAgain = input(
                    f"{num} is prime.\nWould you like to see if a number is prime again('Y') or would you like to do somthing else(Anything but 'Y')?\n")


            #NOTE: If num isn't prime
            elif not isPrime(num):

                goAgain = input(
                    f"{num} is not prime.\nWould you like to see if a number is prime again('Y') or would you like to do somthing else(Anything but 'Y')?\n")

            if goAgain == "y":
                continue
            else:
                on = False


    #MARK: Primes from l to u-------------------------------------------------------------------------------------------
    elif whatDo == 4:
        on = True
        while on:
            invalidChar = True
            while invalidChar:
                try:
                    lowerLimit = int(input("What is your lower limit(eg. 100 in 100-200)?\n"))
                except ValueError:
                    print("Invalid number, please try again.\n")
                else:
                    invalidChar = False


            invalidChar = True
            while invalidChar:
                try:
                    upperLimit = int(input("What is your upper limit(eg. 200 in 100-200)?\n"))
                except ValueError:
                    print("Invalid number, please try again.\n")
                else:
                    invalidChar = False

            primes = primesUpTo(upperLimit, lowerLimit)
            primes = [str(num) for num in primes]
            goAgain = input(f"The primes from {lowerLimit} to {upperLimit} are {", ".join(primes)}\nWould you like to see the primes in a range again('Y') or would you like to do somthing else(Anything but 'Y')?\n").lower()
            if goAgain == "y":
                continue
            else:
                on = False


    #MARK: Prime Factorisation
    elif whatDo == 5:
        on = True
        while on:
            invalidChar = True
            while invalidChar:
                try:
                    num = int(input("Which number would you like to see the prime factors of?\n"))
                except ValueError:
                    print("Invalid number, please try again.\n")
                else:
                    invalidChar = False

            print("\n")
            primeFactors = primeFactorisation(num)
            primeFactors = [str(primeFactor) for primeFactor in primeFactors]

            if len(primeFactors) == 1:
                goAgain = input(f"The prime factor of {num} is {primeFactors[0]}.\nWould you like to see a number's prime factors again('Y') or would you like to do somthing else(Anything but 'Y')?\n").lower()
            else:
                lastPrimeFactor = primeFactors[len(primeFactors)-1]
                primeFactors.remove(lastPrimeFactor)
                primeFactors = ', '.join(primeFactors)
                goAgain = input(f"The prime factors of {num} are {primeFactors} and {lastPrimeFactor}.\nWould you like to see a number's prime factors again('Y') or would you like to do somthing else(Anything but 'Y')?\n").lower()

            if goAgain == "y":
                continue
            else:
                on = False


    #MARK: HCF and LCM--------------------------------------------------------------------------------------------------
    elif whatDo == 6:

        on = True
        while on:
            allInputtedNumbers = []
            invalidChar = True
            while invalidChar:
                try:
                    firstInputtedNumber = int(input("What is your first number?\n"))
                except ValueError:
                    print("Invalid number, please try again.\n")
                else:
                    invalidChar = False
            allInputtedNumbers.append(firstInputtedNumber)

            invalidChar = True
            while invalidChar:
                try:
                    secondInputtedNumber = int(input("What is your second number?\n"))
                except ValueError:
                    print("Invalid number, please try again.\n")
                else:
                    invalidChar = False

            allInputtedNumbers.append(secondInputtedNumber)

            moreNumbersFromUserInput = True
            while moreNumbersFromUserInput:
                newNumber = input("Enter a number to find its HCF and LCM along with the others, or enter any letter/enter to calculate the HCF and LCM of your chosen numbers.")
                try:
                    allInputtedNumbers.append(int(newNumber))
                except ValueError:
                    print("Calculating...\n")
                    moreNumbersFromUserInput = False

            # Most of the below code is for the purpose of proper grammar in the input() statement at the bottom

            lcmHCF = lcmAndHCF(firstInputtedNumber, allInputtedNumbers)
            lastInputtedNumber = allInputtedNumbers[len(allInputtedNumbers) - 1]
            allInputtedNumbers.remove(lastInputtedNumber)
            allInputtedNumbers = [str(x) for x in allInputtedNumbers]

            goAgain = input(f"The HCF and LCM of {', '.join(allInputtedNumbers)} and {lastInputtedNumber} are {lcmHCF["HCF"]} and {lcmHCF["LCM"]}.\nWould you like to see a number's prime factors again('Y') or would you like to do somthing else(Anything but 'Y')?").lower()

            if goAgain == "y":
                continue
            else:
                on = False


    else:
        print("Please enter a valid number from the list of options above\n")
        continue
    print("\n"*75)
