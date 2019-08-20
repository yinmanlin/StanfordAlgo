def Karatsuba(num1, num2):
    '''
    Assume inputs are positive integers
    because otherwise - will take one character
    int() can handle negative numbers
    '''
    #first convert numbers into string
    num1String = str(num1)
    num2String = str(num2)

    #base case
    if len(num1String) == 1 and len(num2String) == 1:
        return num1 * num2
    elif len(num1String) == 1 and len(num2String) > 1:
        split2 = int(len(num2String) / 2)
        c = int(num2String[:split2])
        d = int(num2String[split2:])
        acProduct = Karatsuba(num1, c)
        adProduct = Karatsuba(num1, d)
        return 10 ** (len(num2String) - split2) * acProduct + adProduct
    elif len(num1String) > 1 and len(num2String) == 1:
        split1 = int(len(num1String) / 2)
        a = int(num1String[:split1])
        b = int(num1String[split1:])
        acProduct = Karatsuba(a, num2)
        bcProduct = Karatsuba(b, num2)
        return 10 ** (len(num1String) - split1) * acProduct + bcProduct
    else:
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
        #only valid for two same digit numbers
        #middleProduct = Karatsuba(a + b, c + d) - acProduct - bdProduct
        return 10 ** (len(num2String) - split2 + len(num1String) - split1) * acProduct + 10 ** (len(num1String) - split1) * adProduct + 10 ** (len(num2String) - split2) * bcProduct + bdProduct


print(Karatsuba(3, 671))


    
    
