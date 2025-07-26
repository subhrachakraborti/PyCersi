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