"""
DEVELOPED BY SUBHRA CHAKRABORTI
Last Update: 16th April 2026
Version: 7.0.5

Welcome to PyCersi!
I’ve designed it with careful consideration of user experience.
PyCersi contains a wealth of useful number-checking programs.
Feel free to utilize it to save your precious time. 😊
"""

#Math Module is Required.
import math as m
import json

try:
    from .privator import privator, privator_browser
except ImportError:
    from privator import privator, privator_browser

try:
    from .bot import bot
except ImportError:
    from bot import bot

#Constants
pi = 3.14159265
e = 2.718281828459045
GR = 1.618033988749895
loge = 2.302585092994046
c = 299792458
G = 6.67430 * 10**-11
h = 6.62607015 * 10**-34
Q = 1.602176634 * 10**-19
me = 9.10938356 * 10**-31
mp = 1.6726219 * 10**-27
mn = 1.674927471 * 10**-27
NA = 6.02214076 * 10**23
R = 8.314462618
ME = 5.972 * 10**24
MS = 1.988416 * 10**30
BK = 1.38064852 * 10**-23
SBK = 5.670374419 * 10**-8
Eo = 8.854187817 * 10**-12
Muo = 4 * pi * 10**-7
AU = 149597870700
LY = 9.461 * 10**15
PC = 3.086 * 10**16
hbar = 1.0545718 * 10**-34
F = 96485.33212
H = 2.268 * 10**-18
fsc = 7.2973525693 * 10**-3
CSK = 1.4 * MS

#Intro
def pycersi():
    import turtle
    t = turtle.Turtle()
    s = turtle.Screen()
    s.bgcolor("black")
    t.speed(3)

    font_size = 80
    font_type = ("Courier New", font_size, "bold")

    def write_colorful_text(text, colors):
        for i, letter in enumerate(text):
            t.pencolor(colors[i % len(colors)])
            t.write(letter, font=font_type, align="center")
            t.penup()
            t.forward(font_size + 10)
            t.pendown()

    def draw_pycersi():
        t.penup()
        t.goto(-250, 50)
        t.pendown()
        colors = ["#FFD43B", "#306998", "#FFE873", "#4B8BBE", "#3776AB", "#FFDF5B", "#646464"]
        write_colorful_text("PyCersi", colors)
        t.hideturtle()

    def draw_version():
        t.penup()
        t.goto(140, -20)
        t.pendown()
        t.pencolor("white")
        t.write("7.0.5", font=("Courier New", 30, "bold"), align="center")
        t.hideturtle()

    def notes():
        t.penup()
        t.goto(0, -150)
        t.pendown()
        t.pencolor("white")
        t.write("By Subhra Chakraborti", font=("Courier New", 30, "bold"), align="center")
        t.hideturtle()

    draw_pycersi()
    draw_version()
    notes()
    turtle.done()



#Searchers Functions.
def fiboupto(n):
    a, b = 0, 1
    l = [a]
    while b <= n:
        l.append(b)
        a, b = b, a + b
    return l
def fiborange(n):
    if n == 0:
        return []
    a, b = 0, 1
    l = [a]
    for i in range(n-1):
        l.append(b)
        a, b = b, a + b
    return l

def floyd(rows):
    n = 1
    print("Floyd's Triangle")
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(n, end='  ')
            n += 1
        print()  # Add a newline after each row

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
    if n == 0:
        return 0
    s = 1
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
    for i in range(1,n):
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
def isfibonacci(n):
    if n in fiboupto(n):
        return True
    return False
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
    if n < 2:
        return False
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False
    return True
def ispronic(n):
    for i in range(n):
        if i * (i + 1) == n:
            return True
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
    seen = set()
    while n > 0:
        digit = n % 10
        if digit in seen:
            return False
        seen.add(digit)
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
def ar_circle(radius):
    return 2 * pi * radius
def ar_rect(l, b=1):
    return l * b
def ar_triangle(side1, side2, side3):
    s = (side1 + side2 + side3) / 2
    area = m.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    return area
def digiwords(num):
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
def comb(n, r):
    nf = fact(n)
    rf = fact(r)
    nrf = fact(n-r)
    return nf // (rf * nrf)
def perm(n, r):
    nf = fact(n)
    nrf = fact(n-r)
    return nf // nrf

#Stack Functions
def s_push(stack,element):
    stack.append(element)
def s_size(stack):
    return len(stack)
def s_Empty(stack):
    if s_size(stack) == 0:
        return True
    else:
        return False
def s_pop(stack):
    if s_Empty(stack):
        print('Underflow')
        return None
    else:
        return stack.pop()
def s_top(stack):
    if s_Empty(stack):
        print('Stack is empty.')
        return None
    else:
        x = s_size(stack)
        element = stack[x-1]
        return element
def s_display(stack):
    x = s_size(stack)  
    print("Current elements are : ")
    for i in range(x-1,-1,-1):
        print(stack[i])


#Scientific Computation and Number Intelligence
def convert_units(value, from_unit, to_unit):
    unit_factors = {
        "m": 1.0,
        "meter": 1.0,
        "meters": 1.0,
        "km": 1000.0,
        "kilometer": 1000.0,
        "kilometers": 1000.0,
        "cm": 0.01,
        "centimeter": 0.01,
        "centimeters": 0.01,
        "mm": 0.001,
        "millimeter": 0.001,
        "millimeters": 0.001,
        "au": float(AU),
        "ly": float(LY),
        "pc": float(PC),
    }

    f_unit = str(from_unit).strip().lower()
    t_unit = str(to_unit).strip().lower()

    if f_unit not in unit_factors:
        raise ValueError(f"Unsupported from_unit: {from_unit}")
    if t_unit not in unit_factors:
        raise ValueError(f"Unsupported to_unit: {to_unit}")

    meters = float(value) * unit_factors[f_unit]
    return meters / unit_factors[t_unit]


def dimensional_analysis(numerator_units, denominator_units=None):
    powers = {}

    for unit in numerator_units:
        u = str(unit).strip()
        if u:
            powers[u] = powers.get(u, 0) + 1

    if denominator_units:
        for unit in denominator_units:
            u = str(unit).strip()
            if u:
                powers[u] = powers.get(u, 0) - 1

    simplified = {k: v for k, v in powers.items() if v != 0}
    if not simplified:
        return {"units": {}, "expression": "dimensionless"}

    positives = []
    negatives = []
    for unit, power in sorted(simplified.items()):
        if power > 0:
            positives.append(unit if power == 1 else f"{unit}^{power}")
        else:
            p = abs(power)
            negatives.append(unit if p == 1 else f"{unit}^{p}")

    num_expr = " * ".join(positives) if positives else "1"
    den_expr = " * ".join(negatives)
    expr = f"{num_expr} / {den_expr}" if den_expr else num_expr

    return {"units": simplified, "expression": expr}


def solve_linear(a, b):
    if a == 0:
        raise ValueError("a cannot be 0 for a linear equation.")
    return -b / a


def solve_quadratic(a, b, c):
    if a == 0:
        return {"type": "linear", "root": solve_linear(b, c)}

    d = b**2 - 4 * a * c
    sqrt_d = m.sqrt(abs(d))
    if d >= 0:
        r1 = (-b + sqrt_d) / (2 * a)
        r2 = (-b - sqrt_d) / (2 * a)
    else:
        real = -b / (2 * a)
        imag = sqrt_d / (2 * a)
        r1 = complex(real, imag)
        r2 = complex(real, -imag)

    return {"type": "quadratic", "discriminant": d, "roots": (r1, r2)}


def symbolic_derivative(expression, variable="x"):
    expr = str(expression).replace(" ", "")
    expr = expr.replace("-", "+-")
    if expr.startswith("+"):
        expr = expr[1:]

    raw_terms = [t for t in expr.split("+") if t]
    derivative_terms = []

    for term in raw_terms:
        if variable not in term:
            continue

        if "^" in term:
            base_part, power_str = term.split("^", 1)
            power = int(power_str)
        else:
            base_part = term
            power = 1

        coeff_text = base_part.replace(variable, "")
        if coeff_text in ("", "+"):
            coeff = 1
        elif coeff_text == "-":
            coeff = -1
        else:
            coeff = int(coeff_text)

        new_coeff = coeff * power
        new_power = power - 1

        if new_power == 0:
            derivative_terms.append(str(new_coeff))
        elif new_power == 1:
            if new_coeff == 1:
                derivative_terms.append(variable)
            elif new_coeff == -1:
                derivative_terms.append(f"-{variable}")
            else:
                derivative_terms.append(f"{new_coeff}{variable}")
        else:
            if new_coeff == 1:
                derivative_terms.append(f"{variable}^{new_power}")
            elif new_coeff == -1:
                derivative_terms.append(f"-{variable}^{new_power}")
            else:
                derivative_terms.append(f"{new_coeff}{variable}^{new_power}")

    if not derivative_terms:
        return "0"

    output = derivative_terms[0]
    for t in derivative_terms[1:]:
        if t.startswith("-"):
            output += t
        else:
            output += f"+{t}"
    return output


def statistics(data):
    if data is None:
        raise ValueError("data cannot be None")

    values = [float(x) for x in data]
    if len(values) == 0:
        raise ValueError("data cannot be empty")

    n = len(values)
    mean_value = sum(values) / n
    sorted_values = sorted(values)

    if n % 2 == 1:
        median_value = sorted_values[n // 2]
    else:
        median_value = (sorted_values[n // 2 - 1] + sorted_values[n // 2]) / 2

    variance_value = sum((x - mean_value) ** 2 for x in values) / n
    std_dev_value = m.sqrt(variance_value)

    return {
        "count": n,
        "sum": sum(values),
        "min": min(values),
        "max": max(values),
        "mean": mean_value,
        "median": median_value,
        "variance": variance_value,
        "std_dev": std_dev_value,
    }


def analyze_number(n, output="text"):
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    checks = [
        ("Abundant number", isabundant),
        ("Armstrong number", isarmstrong),
        ("Automorphic number", isautomorphic),
        ("Composite number", lambda x: x > 1 and iscomposite(x)),
        ("Disarium number", isdisarium),
        ("Duck number", isduck),
        ("Even number", iseven),
        ("Fibonacci number", isfibonacci),
        ("Harshad number", isharshad),
        ("Krishnamurthy number", iskrishnamurthy),
        ("Magic number", ismagic),
        ("Neon number", isneon),
        ("Odd number", isodd),
        ("Palindrome number", ispalindrome),
        ("Perfect number", isperfect),
        ("Prime number", isprime),
        ("Special number", ispecial),
        ("Spy number", isspy),
        ("Sunny number", issunny),
        ("Tech number", istech),
        ("Ugly number", isugly),
        ("Unique number", isunique),
    ]

    matched = []
    for label, checker in checks:
        try:
            if checker(n):
                matched.append(label)
        except Exception:
            continue

    report = {
        "number": n,
        "properties": matched,
        "count": len(matched),
    }

    out = str(output).strip().lower()
    if out == "dict":
        return report
    if out == "json":
        return json.dumps(report, indent=2)

    lines = [f"{n} is:"]
    if matched:
        lines.extend([f"- {item}" for item in matched])
    else:
        lines.append("- No special properties found in current checks")
    return "\n".join(lines)


def analyze(n, output="text"):
    return analyze_number(n, output)