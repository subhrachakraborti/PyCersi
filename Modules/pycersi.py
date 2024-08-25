"""
DEVELOPED BY SUBHRA CHAKRABORTI
Last Update: 25th August 2024
Version: v.1.beta

Welcome to PyCersi!
I’ve designed it with careful consideration of user experience.
PyCersi contains a wealth of useful number-checking programs.
Feel free to utilize it to save your precious time. 😊
"""

#Math Module is Required.
import math as m
pi = m.pi
e = m.e

#Searchers Functions.
def fibo(n):
    a, b, c = 0, 1, 0
    print(a)
    while c<=n:
        c = a + b
        print(b)
        a,b = b,c
        if c > n:
            break
def floyd(rows):
    n = 1
    print("Floyd's Triangle") 
    for i in range(1, rows + 1):
        for j in range(1, i + 1):        
            print(n, end = '  ')
            n = n + 1
    print()
def gcd(list1):
    return m.gcd(*list1)
def lcm(list1):
    return m.lcm(*list1)

#Associated Functions.
def digirev(n):
    s = 0
    while n > 0:
        d = n % 10
        n = n // 10
        s = s*10 + d
    return s
def digipro(n):
    s = 0
    while n > 0:
        d = n % 10
        n = n // 10
        s = s * d
    return s
def digisum(n):
    s = 0
    while n > 0:
        d = n % 10
        n = n // 10
        s = s + d
    return s
def numSquareSum(n):
    squareSum = 0
    while n:
        squareSum += (n % 10) ** 2
        n = n // 10
    return squareSum

#Number Checkers Functions.
def isabundant(n):
    sum = 0
    for i in range(n):
        if(n%i == 0):
            sum += i
    if(sum > n):
        return True
    else:
        return False
def isarmstrong(n):
    s = str(n)
    l = len(s)
    o = n
    sum  = 0
    while n > 0:
        d = n % 10
        n = n // 10
        sum = sum + d**l
    if sum == o:
        return True
    else:
        return False
def isautomorphic(n):
    o = n**2
    d = str(o)
    c = str(n)
    if (d.endswith(c)):
        return True
    else :
        return False
def isbuzz(n):
    if n % 10 == 7 or n % 7 == 0:
        return True
    else:
        return False
def iscircularprime(n):
    l = len(n)
    num = int(n)
    s = 0
    i = 0
    while i < l:
        rem = num % 10
        num = num // 10
        num = (rem * (10 ** (l - 1))) + num
        if isprime(num):
            s += 1
        i += 1
    if s == l:
        return True
    else:
        return False
def iscurzon(n):
    p1 = 2**n + 1
    p2 = 2 * n + 1
    if p1 % p2 == 0:
        return True
    else:
        return False
def iscomposite(n):
    if isprime(n):
        return False
    else:
        return True
def iscoprime(nlist):
    if gcd(nlist) == 1:
        return True
    else:
        return False
def isdisarium(n):
    cop, s = n, 0
    while n > 0:
        num = str(n)
        d = n % 10
        s += d**len(num)
        n = n // 10
    if s == cop:
        return True
    else:
        return False
def isdudeney(n):
    if digisum(n) == m.cbrt(n):
        return True
    else:
        return False
def isduck(n):
    num = str(n)
    num = num.lstrip('0')
    return '0' in num
def iseven(n):
    return n % 2 == 0
def ishappy(n):
    slow, fast = n, n
    while True:
        slow = numSquareSum(slow)
        fast = numSquareSum(numSquareSum(fast))
        if slow != fast:
            continue
        else:
            break
    return slow == 1
def isharshad(n):
    s = 0
    temp = n
    while temp > 0:
        s += temp % 10
        temp //= 10
    return n % s == 0
def isheteromecic(n):
    return isoblong(n)
def iskrishnamurthy(n):
    o = n
    Sum =0
    while(n>0):
        a = n%10
        fact = 1
        for i in range(1, a+1):
            fact = fact * i
        Sum = Sum + fact
        n = n//10
    if(Sum == o):
        return True
    else:
        return False
def ismagic(n):
    return n % 9 == 1
def isneon(n):
    if digisum(n*n) == n:
        return True
    else:
        return False
def isniven(n):
    return isharshad(n)
def isoblong(n):
    return ispronic(n)
def isodd(n):
    return iseven(n+1)
def ispalindrome(n):
    if digirev(n) == n:
        return True
    else:
        return False
def isperfect(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if s == n:
        return True
    else:
        return False
def isprime(n):
    c = 0
    for i in range(2,(n//2)+1):
        if n % i == 0:
            c += 1
            break
    if c == 0:
        return True
    else:
        return False
def ispronic(n):
    for i in range():
        if i * (i + 1) == n:
            return True
        else:
            return False
def issunny(n):
    o = n+1
    if m.sqrt(o) == int(m.sqrt(o)):
        return True
    else:
        return False
def ispecial(n):
    if (digisum(n)+digipro(n)) == n:
        return True
    else:
        return False
def isspy(n):
    if digisum(n) == digipro(n):
        return True
    else:
        return False
def istwinprime(n,m):
    if isprime(n) and isprime(m):
        if abs(n-m) == 2:
            return True
        else:
            return False
    else:
        return False
def istwistedprime(n):
    if isprime(n) and isprime(digirev(n)):
        return True
    else:
        return False
def isunique(n):
    ld = n % 10
    while n > 0:
        digit = n % 10
        if digit == ld:
            return False
        n //= 10
    return True
def istech(n):
    digit = len(str(n))
    if digit % 2 != 0:
        return False
    half = digit // 2
    first = n // 10**half
    second = n % 10**half
    tsum = first + second
    square = tsum**2
    return square == n
def isugly(N):
    while N % 2 == 0:
        N //= 2
    while N % 3 == 0:
        N //= 3
    while N % 5 == 0:
        N //= 5
    return N == 1

#Mathematical Functions
def digwords():
    if num == 0:
        return "zero"
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    words = ""
    if num >= 1000:
        words += ones[num // 1000] + " Thousand "
        num %= 1000
    if num >= 100:
        words += ones[num // 100] + " Hundred "
        num %= 100
    if 10 <= num <= 19:
        words += teens[num - 10] + " "
        num = 0
    elif num >= 20:
        words += tens[num // 10] + " "
        num %= 10
    if num >= 1:
        words += ones[num] + " "
    return words.strip()

def fact(n):
    return m.factorial(n)
def factor(n):
    l = list()
    for i in range(2,(n//2)+1):
        if n % i == 0:
            l.append(i)
    return l