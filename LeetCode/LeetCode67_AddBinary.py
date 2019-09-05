def addBinaryDigits(a, b, carry, result):
    aNum = int(a)
    bNum = int(b)
    if carry == 0:
        if aNum == 0 or bNum == 0:
            result = str(aNum + bNum) + result
        else:
            result = '0' + result
            carry = 1
    else:
        if aNum == 0 and bNum == 0:
            result = '1' + result
            carry = 0
        elif aNum == 1 and bNum == 1:
            result = '1' + result
            carry = 1
        else: 
            result = '0' + result
            carry = 1
    return (result, carry)

def addBinary(a, b):
    result = ''
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 and j >= 0:
        result, carry = addBinaryDigits(a[i], b[j], carry, result)
        i -= 1
        j -= 1
        if i == -1 and j == -1 and carry == 1:
            result = '1' + result
   

    while i >= 0:
        if carry == 0:
            result = a[:i+1] + result
            break
        else:
            result, carry = addBinaryDigits(a[i], str(carry), 0, result)
            i -= 1
            if i == -1:
                result = '1' + result

    while j >= 0:
        if carry == 0:
            result = b[:j+1] + result
            break
        else:
            result, carry = addBinaryDigits(b[j], str(carry), 0, result)
            j -= 1
            if j == -1:
                result = '1' + result

    return result

print(addBinary('1010','1011'))