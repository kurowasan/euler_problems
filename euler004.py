'''
Problem:
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''
def isPalindrome(nb):
    arr = str(nb)
    for i in range(int(len(arr)/2)):
        if(arr[i] != arr[len(arr) - 1 - i]):
            return False
    return True

def findHighestPalindrome(nbDigit):
    allProduct = findAllProduct(nbDigit)
    
    for p in allProduct:
        if(isPalindrome(p[0])):
            return p  
    return -1
    

def findAllProduct(nb):
    allProduct = list()
    n1 = 0
    n2 = 0
    
    for i in range(nbDigit):
        n1 += 9 * 10**i
        n2 += 9 * 10**i
        
    startN1 = n1
    startN2 = n2
        
    for ii in range(startN1, 10**(nbDigit - 1), -1):
        n1 -= 1
        for iii in range(startN2, 10**(nbDigit - 1), -1):
            allProduct.append([(n1 * n2), n1, n2])
            n2 -= 1
        n2 = startN2
    allProduct.sort(key = lambda r: r[0], reverse=True)
    
    return allProduct
             
nbDigit = 3 
print(findHighestPalindrome(nbDigit))