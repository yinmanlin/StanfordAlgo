def addBinary(a, b):
    result = ''
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 and j >= 0:
        aNum = int(a[i])
        bNum = int(b[j])
        if carry == 0:
            if aNum == 0 or bNum == 0:
                result = str(aNum + bNum) + result
                i -= 1
                j -= 1
            else:
                result = '0' + result
                carry = 1
                i -= 1
                j -= 1
        else:
            if aNum == 0 and bNum == 0:
                result = '1' + result
                carry = 0
                i -= 1
                j -= 1
            elif aNum == 1 and bNum == 1:
                result = '1' + result
                carry = 1
                i -= 1
                j -= 1
            else: 
                result = '0' + result
                carry = 1
                i -= 1
                j -= 1
        
    if i > 0 or j > 0:
        if carry == 1:
            result = '10' + result
        else:
            result = '1' + result
    return result