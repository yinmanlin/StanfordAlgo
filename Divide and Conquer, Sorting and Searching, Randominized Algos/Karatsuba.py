def Karatsuba(num1, num2):
    '''
    Assume inputs are positive integers
    because otherwise - will take one character
    int() can handle negative numbers
    time complexity is n**1.59
    can take two integers with different length
    '''
    #first convert numbers into string
    num1String = str(num1)
    num2String = str(num2)

    #base case
    if len(num1String) == 1 and len(num2String) == 1:
        return num1 * num2
    # one single digit one multiple digits
    elif len(num1String) == 1 and len(num2String) > 1:
        split2 = int(len(num2String) / 2)
        c = int(num2String[:split2])
        d = int(num2String[split2:])
        acProduct = Karatsuba(num1, c)
        adProduct = Karatsuba(num1, d)
        # merge the subproblem solution
        return 10 ** (len(num2String) - split2) * acProduct + adProduct
    elif len(num1String) > 1 and len(num2String) == 1:
        split1 = int(len(num1String) / 2)
        a = int(num1String[:split1])
        b = int(num1String[split1:])
        acProduct = Karatsuba(a, num2)
        bcProduct = Karatsuba(b, num2)
        # merge the subproblem solution
        return 10 ** (len(num1String) - split1) * acProduct + bcProduct
    # two multiple digits
    else:
        # because two numbers can have different digits, use 4 recursive calls
        split1 = int(len(num1String) / 2)
        split2 = int(len(num2String) / 2)
        a = int(num1String[:split1])
        b = int(num1String[split1:])
        c = int(num2String[:split2])
        d = int(num2String[split2:])
        acProduct = Karatsuba(a, c)
        adProduct = Karatsuba(a, d)
        bcProduct = Karatsuba(b, c)
        bdProduct = Karatsuba(b, d)
        # only valid for two same digit numbers
        # middleProduct = Karatsuba(a + b, c + d) - acProduct - bdProduct
        # merge the subproblem solution
        return 10 ** (len(num2String) - split2 + len(num1String) - split1) * acProduct + 10 ** (len(num1String) - split1) * adProduct + 10 ** (len(num2String) - split2) * bcProduct + bdProduct


print(Karatsuba(3141592653589793238462643383279502884197169399375105820974944592, 2718281828459045235360287471352662497757247093699959574966967627))


    
    
