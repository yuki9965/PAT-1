__author__ = 'Yaicky'
import sys

array = [1111, 2222, 3333, 4444, 5555, 6666, 7777, 8888, 9999]

for line in sys.stdin:
    num = line.split()
    for n in num:
        # print(n)
        if int(n) in array:
            print ("%s - %s = 0000" % (n, n))
        else:
            while int(n) < 1000:
                n += '0'
            numList = list(map(int, n))
            while True:
                numList.sort()
                # print (numList)
                minStr = ''.join(map(str, numList))
                # print(minStr)
                maxStr = minStr[::-1]
                minus = int(maxStr) - int(minStr)
                print ("%s - %s = %4d" % (maxStr, minStr, minus))

                if minus == 6174 or minus == 0:
                    break
                numList = list(map(int, str(minus)))
