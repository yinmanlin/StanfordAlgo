def MaxSubArray(num):
    if len(num) == 1:
        return num[0]
    else:
        split = (int)(len(num) / 2)
        maxA = MaxSubArray(num[:split])
        maxB = MaxSubArray(num[:split])
        