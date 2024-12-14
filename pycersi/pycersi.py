"""
DEVELOPED BY SUBHRA CHAKRABORTI
Last Update: 14th December 2024
Version: 5.5.0

Welcome to PyCersi!
I’ve designed it with careful consideration of user experience.
PyCersi contains a wealth of useful number-checking programs.
Feel free to utilize it to save your precious time. 😊
"""

#Math Module is Required.
import math as m

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
        t.write("5.5.0", font=("Courier New", 30, "bold"), align="center")
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

#Encryptor and Decriptor - Pycersi Privator
def privator():
    try:
        import tkinter as tk
        from tkinter import messagebox, font, ttk
        import base64

        class ColorfulEncryptionApp:
            def __init__(self, master):
                self.master = master
                master.title("PyCersi Privator")
                master.geometry("800x525")
                master.configure(bg="#2C3E50")

                # Define cool fonts
                self.title_font = font.Font(family="Orbitron", size=20, weight="bold")
                self.label_font = font.Font(family="Exo 2", size=15)
                self.input_font = font.Font(family="Times New Roman", size=12)
                self.button_font = font.Font(family="Calibri", size=15, weight="bold")

                self.title_label = tk.Label(master, text="🔐 Secret Message Encoder 🔓", font=self.title_font, bg="#2C3E50", fg="#ECF0F1")
                self.title_label.pack(pady=20)

                self.input_label = tk.Label(master, text="Enter Your Message ⬇️", font=self.label_font, bg="#2C3E50", fg="#ECF0F1")
                self.input_label.pack()

                # Create a frame for input text and scrollbar
                self.input_frame = tk.Frame(master, bg="#2C3E50")
                self.input_frame.pack(pady=5)

                self.input_entry = tk.Text(self.input_frame, width=60, height=5, font=self.input_font, bg="#ECF0F1")
                self.input_entry.pack(side=tk.LEFT)

                self.input_scrollbar = ttk.Scrollbar(self.input_frame, orient="vertical", command=self.input_entry.yview)
                self.input_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                self.input_entry.configure(yscrollcommand=self.input_scrollbar.set)

                self.key_label = tk.Label(master, text="Enter Key", font=self.label_font, bg="#2C3E50", fg="#ECF0F1")
                self.key_label.pack()
                self.key_entry = tk.Entry(master, width=10, font=self.input_font, bg="#ECF0F1", justify='center')
                self.key_entry.pack(pady=5)

                self.button_frame = tk.Frame(master, bg="#2C3E50")
                self.button_frame.pack(pady=10)

                self.encrypt_button = tk.Button(self.button_frame, text="🔒 ENCRYPT", command=self.encrypt, 
                                                font=self.button_font, bg="#27AE60", fg="white", padx=15)
                self.encrypt_button.pack(side=tk.LEFT, padx=5)

                self.decrypt_button = tk.Button(self.button_frame, text="🔓 DECRYPT", command=self.decrypt, 
                                                font=self.button_font, bg="#E74C3C", fg="white", padx=15)
                self.decrypt_button.pack(side=tk.LEFT, padx=5)

                self.result_label = tk.Label(master, text="RESULT 🟰", font=self.label_font, bg="#2C3E50", fg="#ECF0F1")
                self.result_label.pack()
                
                # Create a frame for result text and scrollbar
                self.result_frame = tk.Frame(master, bg="#2C3E50")
                self.result_frame.pack(pady=5)
                
                self.result_entry = tk.Text(self.result_frame, width=60, height=5, font=self.input_font, bg="#ECF0F1")
                self.result_entry.pack(side=tk.LEFT)

                self.result_scrollbar = ttk.Scrollbar(self.result_frame, orient="vertical", command=self.result_entry.yview)
                self.result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                self.result_entry.configure(yscrollcommand=self.result_scrollbar.set)
                
                self.copy_button = tk.Button(master, text="📋 Copy", command=self.copy_result, 
                                            font=self.button_font, bg="#3498DB", fg="white")
                self.copy_button.pack(pady=5)

                # Bind keyboard shortcuts
                self.input_entry.bind('<Return>', self.encrypt_event)
                self.key_entry.bind('<Return>', self.encrypt_event)

                x = tk.Label(master, text="Made with 💖 by Subhra Chakraborti", font=self.label_font, bg="#2C3E50", fg="#ECF0F1")
                x.pack(pady=120)

            # The rest of the methods remain the same
            def generate_key(self, key_string):
                return (key_string * (32 // len(key_string) + 1))[:32].encode()

            def xor_encrypt_decrypt(self, message, key):
                return bytes([message[i] ^ key[i % len(key)] for i in range(len(message))])

            def encrypt_event(self, event):
                self.encrypt()
                return 'break'

            def decrypt_event(self, event):
                self.decrypt()
                return 'break'

            def encrypt(self):
                message = self.input_entry.get("1.0", tk.END).strip()
                key_string = self.key_entry.get()
                if message and key_string:
                    key = self.generate_key(key_string)
                    encrypted = self.xor_encrypt_decrypt(message.encode(), key)
                    self.result_entry.delete("1.0", tk.END)
                    self.result_entry.insert("1.0", base64.b64encode(encrypted).decode())
                elif message and not key_string:
                    key = self.generate_key("150847")
                    messagebox.showinfo("Default Key Used!", "Default Key: 150847")
                    encrypted = self.xor_encrypt_decrypt(message.encode(), key)
                    self.result_entry.delete("1.0", tk.END)
                    self.result_entry.insert("1.0", base64.b64encode(encrypted).decode())
                else:
                    messagebox.showwarning("⚠️WARNING⚠️", "Please enter message!")

            def decrypt(self):
                encrypted_message = self.input_entry.get("1.0", tk.END).strip()
                key_string = self.key_entry.get()
                if encrypted_message and key_string:
                    try:
                        key = self.generate_key(key_string)
                        encrypted = base64.b64decode(encrypted_message)
                        decrypted = self.xor_encrypt_decrypt(encrypted, key).decode()
                        self.result_entry.delete("1.0", tk.END)
                        self.result_entry.insert("1.0", decrypted)
                    except:
                        messagebox.showerror("Error", "Invalid encrypted message or key.")
                else:
                    messagebox.showwarning("⚠️WARNING⚠️", "Please enter both an encrypted message and the correct key.")

            def copy_result(self):
                result = self.result_entry.get("1.0", tk.END).strip()
                if result:
                    self.master.clipboard_clear()
                    self.master.clipboard_append(result)
                    self.master.update()
                else:
                    messagebox.showwarning("⚠️WARNING⚠️", "No result to copy.")

        root = tk.Tk()
        app = ColorfulEncryptionApp(root)
        root.mainloop()
    except ImportError:
        print("Try Installing Tkinter Module.")