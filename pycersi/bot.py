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
