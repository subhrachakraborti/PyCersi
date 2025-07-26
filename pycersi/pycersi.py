"""
DEVELOPED BY SUBHRA CHAKRABORTI
Last Update: 14th December 2024
Version: 6.1.0

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
        t.write("6.1.0", font=("Courier New", 30, "bold"), align="center")
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

#AI Bot
def bot():
    import tkinter as tk
    from tkinter import filedialog, messagebox, scrolledtext
    import ttkbootstrap as tb
    import google.generativeai as genai
    import json
    import time
    import threading
    import re

    DEFAULT_API_KEY = "AIzaSyCJWlb4s5PQbQIaImbqh-SczW5v_7mvzcc"
    MODELS = ["gemini-1.5-flash", "gemini-2.0-flash"]

    def parse_ai_response(text):
        """
        Parses **bold**, *italic*, and bullet lists:
        - **bold**
        - *italic* or bullet via '* ' at line start
        """
        lines = text.split("\n")
        out = []
        for line in lines:
            if line.strip().startswith("* "):
                content = line.strip()[2:].strip()
                out.append(("bullet", content))
            else:
                b = re.sub(r"\*\*(.*?)\*\*", r"\1", line)
                i = re.sub(r"\*(.*?)\*", r"\1", b)
                out.append(("text", i))
        return out

    class GeminiChatApp(tb.Window):
        def __init__(self):
            super().__init__(themename="darkly")
            self.title("PyCersi AI Chat (Gemini)")
            self.geometry("1000x650")
            self.chat = None
            self.history = []
            self.create_ui()

        def create_ui(self):
            menu = tk.Menu(self)
            theme_menu = tk.Menu(menu, tearoff=0)
            for theme in tb.Style().theme_names():
                theme_menu.add_command(label=theme, command=lambda t=theme: self.change_theme(t))
            menu.add_cascade(label="Theme", menu=theme_menu)
            menu.add_command(label="Export to TXT", command=self.export_txt)
            menu.add_command(label="Export to JSON", command=self.export_json)
            menu.add_command(label="Clear Chat", command=self.clear_chat)
            self.config(menu=menu)

            f = tb.Frame(self)
            f.pack(pady=10, padx=20, fill="x")
            tb.Label(f, text="🔑 API Key:", font=("Segoe UI", 12)).grid(row=0, column=0, padx=5)
            self.api_entry = tb.Entry(f, width=50)
            self.api_entry.grid(row=0, column=1, padx=5)
            self.api_entry.insert(0, "Enter your Gemini API Key here or use a free one")
            self.api_entry.bind("<FocusIn>", self.clear_placeholder)

            tb.Label(f, text="📦 Model:", font=("Segoe UI", 12)).grid(row=0, column=2, padx=10)
            self.model_var = tk.StringVar(value=MODELS[0])
            self.model_menu = tb.Combobox(f, textvariable=self.model_var, values=MODELS, state="readonly", width=20)
            self.model_menu.grid(row=0, column=3)

            self.start_btn = tb.Button(self, text="🚀 Start Chat", bootstyle="success", command=self.initialize_chat)
            self.start_btn.pack(pady=5)

            self.chat_display = scrolledtext.ScrolledText(self, wrap=tk.WORD, font=("Consolas", 12), state="disabled", height=20)
            self.chat_display.pack(fill="both", expand=True, padx=20, pady=10)

            bf = tb.Frame(self)
            bf.pack(pady=10, fill="x", padx=20)
            self.user_input = tb.Entry(bf, font=("Segoe UI", 11))
            self.user_input.pack(side="left", fill="x", expand=True, padx=(0,10))
            self.user_input.bind("<Return>", self.send_message)
            tb.Button(bf, text="Send", bootstyle="primary", command=self.send_message).pack(side="right")

        def change_theme(self, theme):
            self.style.theme_use(theme)

        def clear_placeholder(self, e):
            if self.api_entry.get().lower().startswith("enter your"):
                self.api_entry.delete(0, tk.END)

        def initialize_chat(self):
            api_key = self.api_entry.get().strip()
            if not api_key or "enter your" in api_key.lower() or api_key.lower() == "free one":
                api_key = DEFAULT_API_KEY
            model_name = self.model_var.get()
            try:
                genai.configure(api_key=api_key)
                model = genai.GenerativeModel(model_name)
                self.chat = model.start_chat()
                self.append_to_chat("🧠 System", f"Chat started using {model_name}")
            except Exception as e:
                messagebox.showerror("Init Error", str(e))

        def send_message(self, event=None):
            if not self.chat:
                messagebox.showwarning("Not Ready", "Click 'Start Chat' first.")
                return
            msg = self.user_input.get().strip()
            if not msg:
                return
            self.append_to_chat("👤 You", msg)
            self.user_input.delete(0, tk.END)
            threading.Thread(target=self.get_bot_response, args=(msg,), daemon=True).start()

        def get_bot_response(self, user_msg):
            try:
                response = self.chat.send_message(user_msg)
                text = response.text.strip()
                self.append_with_typing("🤖 Bot", text)
            except Exception as e:
                self.append_to_chat("❗ Error", str(e))

        def append_to_chat(self, sender, message):
            self.history.append((sender, message))
            self.chat_display.config(state="normal")
            self.chat_display.insert(tk.END, f"{sender}: {message}\n\n")
            self.chat_display.yview(tk.END)
            self.chat_display.config(state="disabled")

        def append_with_typing(self, sender, full_text):
            parsed = parse_ai_response(full_text)
            self.history.append((sender, full_text))
            self.chat_display.config(state="normal")
            self.chat_display.insert(tk.END, f"{sender}: ")
            for kind, segment in parsed:
                if kind == "bullet":
                    self.chat_display.insert(tk.END, f"• {segment}\n")
                else:
                    for ch in segment:
                        self.chat_display.insert(tk.END, ch)
                        self.chat_display.see(tk.END)
                        time.sleep(0.02)
                    self.chat_display.insert(tk.END, "\n")
            self.chat_display.insert(tk.END, "\n")
            self.chat_display.config(state="disabled")
            self.chat_display.see(tk.END)

        def export_txt(self):
            f = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text file","*.txt")])
            if not f: return
            with open(f, "w", encoding="utf-8") as fp:
                for sender, msg in self.history:
                    fp.write(f"{sender}: {msg}\n\n")
            messagebox.showinfo("Exported", f"Chat exported to {f}")

        def export_json(self):
            f = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON file","*.json")])
            if not f: return
            data = [{"sender": s, "message": m} for s, m in self.history]
            with open(f, "w", encoding="utf-8") as fp:
                json.dump(data, fp, indent=2, ensure_ascii=False)
            messagebox.showinfo("Exported", f"Chat exported to {f}")

        def clear_chat(self):
            self.history.clear()
            self.chat_display.config(state="normal")
            self.chat_display.delete("1.0", tk.END)
            self.chat_display.config(state="disabled")

    if __name__ == "__main__":
        app = GeminiChatApp()
        app.mainloop()

def liteBot():
    import google.generativeai as genai

    api = input("Enter your Gemini API Key (or press Enter for default): ").strip()
    if not api:
        api = "AIzaSyCJWlb4s5PQbQIaImbqh-SczW5v_7mvzcc"
    genai.configure(api_key=api)
    model = genai.GenerativeModel("gemini-2.0-flash")

    chat = model.start_chat()

    print("PyCersi AI Bot is running...")
    print("Enter EXIT or QUIT to Exit...")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting PyCersi AI Bot. Goodbye!")
            break

        try:
            response = chat.send_message(user_input)
            print("Bot:", response.text)
        except Exception as e:
            print("Error:", e)