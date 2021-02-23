def isPrime(number):
    checkPrime = 1
    for i in range(2, number):
        if (number % i == 0):
            checkPrime = 0
            break
    if (checkPrime == 1):
        return True
    else:
        return False


while True:
    while True:
        number = float(input("Enter floating number (12 digit) : "))
        if (number == 0.0):
            exit()
        if (len(str(number)) <= 12):
            break

    floatPrime = 0
    for i in [10, 100, 1000]:
        if (isPrime(int(number * i))):
            floatPrime = 1
            break
    if (floatPrime == 1):
        print("TRUE")
    else:
        print("FALSE")