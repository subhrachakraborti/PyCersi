from __future__ import annotations

import base64
import tempfile
import textwrap
import webbrowser
from pathlib import Path


ACCENT = "#E67E22"
BACKGROUND = "#111827"
CARD = "#1F2937"
CARD_EDGE = "#334155"
TEXT = "#E5E7EB"
MUTED = "#94A3B8"
INPUT_BG = "#0F172A"
SUCCESS = "#22C55E"
DANGER = "#EF4444"
INFO = "#38BDF8"


def _expand_key(key_string: str) -> str:
    return (key_string * (32 // len(key_string) + 1))[:32]


def _xor_bytes(message: bytes, key: bytes) -> bytes:
    return bytes(message[index] ^ key[index % len(key)] for index in range(len(message)))


def _build_browser_page() -> str:
    return textwrap.dedent(
        """
        <!doctype html>
        <html lang="en">
        <head>
          <meta charset="utf-8" />
          <meta name="viewport" content="width=device-width, initial-scale=1" />
          <title>PyCersi Privator</title>
          <style>
            :root {
              color-scheme: dark;
              --panel: rgba(17, 24, 39, 0.88);
              --panel-border: rgba(148, 163, 184, 0.18);
              --text: #e5e7eb;
              --muted: #94a3b8;
              --accent: #e67e22;
              --accent-2: #38bdf8;
              --success: #22c55e;
              --danger: #ef4444;
              --shadow: 0 24px 80px rgba(0, 0, 0, 0.45);
            }
            * { box-sizing: border-box; }
            body {
              margin: 0;
              min-height: 100vh;
              font-family: "Segoe UI", "Trebuchet MS", sans-serif;
              color: var(--text);
              background:
                radial-gradient(circle at top left, rgba(230, 126, 34, 0.28), transparent 28%),
                radial-gradient(circle at top right, rgba(56, 189, 248, 0.22), transparent 24%),
                linear-gradient(160deg, #050816 0%, #0f172a 48%, #111827 100%);
              display: grid;
              place-items: center;
              padding: 28px;
            }
            .shell {
              width: min(1100px, 100%);
              background: var(--panel);
              border: 1px solid var(--panel-border);
              border-radius: 28px;
              box-shadow: var(--shadow);
              backdrop-filter: blur(20px);
              overflow: hidden;
            }
            .hero {
              padding: 32px 32px 18px;
              background: linear-gradient(135deg, rgba(230, 126, 34, 0.15), rgba(56, 189, 248, 0.1));
              border-bottom: 1px solid rgba(148, 163, 184, 0.14);
            }
            .eyebrow {
              display: inline-flex;
              align-items: center;
              padding: 8px 14px;
              border-radius: 999px;
              background: rgba(15, 23, 42, 0.8);
              color: var(--muted);
              font-size: 13px;
              letter-spacing: 0.12em;
              text-transform: uppercase;
            }
            h1 {
              margin: 16px 0 10px;
              font-size: clamp(34px, 4vw, 58px);
              line-height: 0.96;
              letter-spacing: -0.04em;
            }
            .hero p {
              margin: 0;
              max-width: 760px;
              color: var(--muted);
              font-size: 16px;
            }
            .content {
              display: grid;
              grid-template-columns: 1.1fr 0.9fr;
              gap: 18px;
              padding: 24px;
            }
            .card {
              background: rgba(15, 23, 42, 0.9);
              border: 1px solid rgba(148, 163, 184, 0.16);
              border-radius: 22px;
              padding: 18px;
              box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.03);
            }
            .card h2 {
              margin: 0 0 12px;
              font-size: 18px;
            }
            .field {
              display: flex;
              flex-direction: column;
              gap: 8px;
              margin-bottom: 14px;
            }
            label {
              font-size: 13px;
              letter-spacing: 0.04em;
              color: var(--muted);
            }
            textarea, input {
              width: 100%;
              border: 1px solid rgba(148, 163, 184, 0.18);
              border-radius: 16px;
              background: rgba(2, 6, 23, 0.72);
              color: var(--text);
              padding: 14px 16px;
              font: inherit;
              outline: none;
            }
            textarea:focus, input:focus {
              border-color: rgba(230, 126, 34, 0.9);
              box-shadow: 0 0 0 4px rgba(230, 126, 34, 0.15);
            }
            textarea {
              min-height: 180px;
              resize: vertical;
            }
            .row {
              display: flex;
              gap: 12px;
              flex-wrap: wrap;
            }
            button {
              border: 0;
              border-radius: 14px;
              padding: 12px 16px;
              color: white;
              font: inherit;
              font-weight: 700;
              cursor: pointer;
            }
            .primary { background: linear-gradient(135deg, var(--accent), #f59e0b); }
            .secondary { background: linear-gradient(135deg, var(--accent-2), #2563eb); }
            .success { background: linear-gradient(135deg, var(--success), #16a34a); }
            .danger { background: linear-gradient(135deg, var(--danger), #dc2626); }
            .ghost { background: rgba(148, 163, 184, 0.16); color: var(--text); }
            .result {
              min-height: 260px;
              white-space: pre-wrap;
              word-break: break-word;
              line-height: 1.6;
              background: rgba(2, 6, 23, 0.72);
              border: 1px solid rgba(148, 163, 184, 0.18);
              border-radius: 18px;
              padding: 16px;
              margin-top: 14px;
            }
            .status {
              margin-top: 12px;
              color: var(--muted);
              min-height: 20px;
              font-size: 13px;
            }
            .footer {
              padding: 0 24px 24px;
              color: var(--muted);
              font-size: 13px;
            }
            @media (max-width: 920px) {
              .content { grid-template-columns: 1fr; }
            }
          </style>
        </head>
        <body>
          <main class="shell">
            <section class="hero">
              <div class="eyebrow">PyCersi Privator</div>
              <h1>Encrypted messages, now in your browser.</h1>
              <p>Use the same XOR plus base64 workflow as the desktop tool, with a cleaner layout and no extra install step.</p>
            </section>

            <section class="content">
              <div class="card">
                <h2>Input</h2>
                <div class="field">
                  <label for="message">Message or encoded text</label>
                  <textarea id="message" placeholder="Type a message to encrypt or paste encoded text to decrypt."></textarea>
                </div>
                <div class="field">
                  <label for="key">Key</label>
                  <input id="key" type="text" placeholder="Enter a key or leave blank to use 150847" />
                </div>
                <div class="row">
                  <button class="primary" onclick="encryptText()">Encrypt</button>
                  <button class="danger" onclick="decryptText()">Decrypt</button>
                  <button class="ghost" onclick="fillDefaultKey()">Use Default Key</button>
                </div>
                <div class="status" id="status"></div>
              </div>

              <div class="card">
                <h2>Output</h2>
                <div class="row">
                  <button class="secondary" onclick="copyOutput()">Copy Output</button>
                  <button class="ghost" onclick="clearAll()">Clear</button>
                </div>
                <div class="result" id="output" aria-live="polite"></div>
              </div>
            </section>

            <div class="footer">Made with care by Subhra Chakraborti</div>
          </main>

          <script>
            const DEFAULT_KEY = "150847";

            function setStatus(text) {
              document.getElementById("status").textContent = text;
            }

            function getKey() {
              const key = document.getElementById("key").value.trim();
              return key || DEFAULT_KEY;
            }

            function expandKey(key) {
              return key.repeat(Math.floor(32 / key.length) + 1).slice(0, 32);
            }

            function encryptText() {
              const message = document.getElementById("message").value;
              const key = getKey();
              if (!message.trim()) {
                setStatus("Enter a message first.");
                return;
              }
              const bytes = new TextEncoder().encode(message);
              const expandedKey = new TextEncoder().encode(expandKey(key));
              const encrypted = new Uint8Array(bytes.length);
              for (let index = 0; index < bytes.length; index++) {
                encrypted[index] = bytes[index] ^ expandedKey[index % expandedKey.length];
              }
              let binary = "";
              encrypted.forEach((value) => binary += String.fromCharCode(value));
              document.getElementById("output").textContent = btoa(binary);
              setStatus(document.getElementById("key").value.trim() ? "Encrypted successfully." : "Using default key 150847.");
            }

            function decryptText() {
              const message = document.getElementById("message").value.trim();
              const key = getKey();
              if (!message) {
                setStatus("Enter an encoded message first.");
                return;
              }
              try {
                const binary = atob(message);
                const bytes = Uint8Array.from(binary, (character) => character.charCodeAt(0));
                const expandedKey = new TextEncoder().encode(expandKey(key));
                const decrypted = new Uint8Array(bytes.length);
                for (let index = 0; index < bytes.length; index++) {
                  decrypted[index] = bytes[index] ^ expandedKey[index % expandedKey.length];
                }
                document.getElementById("output").textContent = new TextDecoder().decode(decrypted);
                setStatus("Decrypted successfully.");
              } catch (error) {
                setStatus("Invalid encoded text or key.");
              }
            }

            async function copyOutput() {
              const text = document.getElementById("output").textContent;
              if (!text) {
                setStatus("Nothing to copy.");
                return;
              }
              try {
                await navigator.clipboard.writeText(text);
                setStatus("Output copied to clipboard.");
              } catch (error) {
                setStatus("Clipboard access was blocked by the browser.");
              }
            }

            function clearAll() {
              document.getElementById("message").value = "";
              document.getElementById("key").value = "";
              document.getElementById("output").textContent = "";
              setStatus("Cleared.");
            }

            function fillDefaultKey() {
              document.getElementById("key").value = DEFAULT_KEY;
              setStatus("Default key applied.");
            }
          </script>
        </body>
        </html>
        """
    ).strip()


def _open_browser_page() -> None:
    html_file = Path(tempfile.gettempdir()) / "pycersi_privator.html"
    html_file.write_text(_build_browser_page(), encoding="utf-8")
    webbrowser.open(html_file.as_uri())


def privator() -> None:
    try:
        import tkinter as tk
        from tkinter import font, messagebox, ttk

        class PrivatorApp:
            def __init__(self, master):
                self.master = master
                master.title("PyCersi Privator")
                master.geometry("960x720")
                master.minsize(900, 680)
                master.configure(bg=BACKGROUND)

                self.title_font = font.Font(family="Segoe UI", size=24, weight="bold")
                self.body_font = font.Font(family="Segoe UI", size=10)
                self.section_font = font.Font(family="Segoe UI", size=13, weight="bold")
                self.input_font = font.Font(family="Consolas", size=11)
                self.button_font = font.Font(family="Segoe UI", size=11, weight="bold")

                self.header = tk.Frame(master, bg=BACKGROUND)
                self.header.pack(fill=tk.X, padx=24, pady=(22, 12))

                tk.Label(self.header, text="Privator", font=self.body_font, bg=ACCENT, fg="white", padx=12, pady=4).pack(anchor="w")
                tk.Label(self.header, text="Secret Message Encoder", font=self.title_font, bg=BACKGROUND, fg=TEXT).pack(anchor="w", pady=(10, 2))
                tk.Label(
                    self.header,
                    text="Encrypt and decrypt messages locally, or launch the browser view for a cleaner layout.",
                    font=self.body_font,
                    bg=BACKGROUND,
                    fg=MUTED,
                    wraplength=840,
                    justify="left",
                ).pack(anchor="w")

                self.content = tk.Frame(master, bg=BACKGROUND)
                self.content.pack(fill=tk.BOTH, expand=True, padx=24, pady=(0, 20))

                self.input_card = tk.Frame(self.content, bg=CARD, highlightbackground=CARD_EDGE, highlightthickness=1)
                self.input_card.pack(fill=tk.BOTH, expand=True, pady=(0, 16))

                tk.Label(self.input_card, text="Input", font=self.section_font, bg=CARD, fg=TEXT).pack(anchor="w", padx=18, pady=(16, 8))

                self.input_frame = tk.Frame(self.input_card, bg=CARD)
                self.input_frame.pack(fill=tk.BOTH, expand=True, padx=18, pady=(0, 12))

                self.input_entry = tk.Text(
                    self.input_frame,
                    height=7,
                    font=self.input_font,
                    bg=INPUT_BG,
                    fg=TEXT,
                    insertbackground=TEXT,
                    relief="flat",
                    wrap="word",
                    padx=12,
                    pady=12,
                )
                self.input_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

                self.input_scrollbar = ttk.Scrollbar(self.input_frame, orient="vertical", command=self.input_entry.yview)
                self.input_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                self.input_entry.configure(yscrollcommand=self.input_scrollbar.set)

                controls = tk.Frame(self.input_card, bg=CARD)
                controls.pack(fill=tk.X, padx=18, pady=(0, 18))

                key_group = tk.Frame(controls, bg=CARD)
                key_group.pack(fill=tk.X, pady=(0, 12))

                tk.Label(key_group, text="Key", font=self.section_font, bg=CARD, fg=TEXT).pack(anchor="w")
                self.key_entry = tk.Entry(
                    key_group,
                    width=14,
                    font=self.input_font,
                    bg=INPUT_BG,
                    fg=TEXT,
                    insertbackground=TEXT,
                    relief="flat",
                    justify="center",
                )
                self.key_entry.pack(anchor="w", pady=(8, 0))

                button_row = tk.Frame(controls, bg=CARD)
                button_row.pack(fill=tk.X)

                tk.Button(button_row, text="Encrypt", command=self.encrypt, font=self.button_font, bg=SUCCESS, fg="white", padx=18, pady=8).pack(side=tk.LEFT, padx=(0, 10))
                tk.Button(button_row, text="Decrypt", command=self.decrypt, font=self.button_font, bg=DANGER, fg="white", padx=18, pady=8).pack(side=tk.LEFT, padx=(0, 10))
                tk.Button(button_row, text="Default Key", command=self.use_default_key, font=self.button_font, bg=INFO, fg="white", padx=18, pady=8).pack(side=tk.LEFT, padx=(0, 10))
                tk.Button(button_row, text="Open in Browser", command=self.open_browser, font=self.button_font, bg=ACCENT, fg="white", padx=18, pady=8).pack(side=tk.LEFT)

                self.result_card = tk.Frame(self.content, bg=CARD, highlightbackground=CARD_EDGE, highlightthickness=1)
                self.result_card.pack(fill=tk.BOTH, expand=True)

                tk.Label(self.result_card, text="Result", font=self.section_font, bg=CARD, fg=TEXT).pack(anchor="w", padx=18, pady=(16, 8))

                self.result_frame = tk.Frame(self.result_card, bg=CARD)
                self.result_frame.pack(fill=tk.BOTH, expand=True, padx=18, pady=(0, 12))

                self.result_entry = tk.Text(
                    self.result_frame,
                    height=7,
                    font=self.input_font,
                    bg=INPUT_BG,
                    fg=TEXT,
                    insertbackground=TEXT,
                    relief="flat",
                    wrap="word",
                    padx=12,
                    pady=12,
                )
                self.result_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

                self.result_scrollbar = ttk.Scrollbar(self.result_frame, orient="vertical", command=self.result_entry.yview)
                self.result_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
                self.result_entry.configure(yscrollcommand=self.result_scrollbar.set)

                result_actions = tk.Frame(self.result_card, bg=CARD)
                result_actions.pack(fill=tk.X, padx=18, pady=(0, 16))

                tk.Button(result_actions, text="Copy Result", command=self.copy_result, font=self.button_font, bg=INFO, fg="white", padx=18, pady=8).pack(side=tk.LEFT)
                tk.Button(result_actions, text="Clear", command=self.clear_fields, font=self.button_font, bg="#64748B", fg="white", padx=18, pady=8).pack(side=tk.LEFT, padx=(10, 0))

                self.input_entry.bind("<Return>", self.encrypt_event)
                self.key_entry.bind("<Return>", self.encrypt_event)

                tk.Label(master, text="Made with care by Subhra Chakraborti", font=self.body_font, bg=BACKGROUND, fg=MUTED).pack(anchor="e", padx=24, pady=(0, 14))

            def generate_key(self, key_string):
                return _expand_key(key_string).encode()

            def xor_encrypt_decrypt(self, message, key):
                return _xor_bytes(message, key)

            def encrypt_event(self, event):
                self.encrypt()
                return "break"

            def decrypt_event(self, event):
                self.decrypt()
                return "break"

            def encrypt(self):
                message = self.input_entry.get("1.0", tk.END).strip()
                key_string = self.key_entry.get().strip()
                if not message:
                    messagebox.showwarning("Warning", "Please enter message!")
                    return

                if not key_string:
                    key_string = "150847"
                    messagebox.showinfo("Default Key Used!", "Default Key: 150847")

                encrypted = self.xor_encrypt_decrypt(message.encode(), self.generate_key(key_string))
                self.result_entry.delete("1.0", tk.END)
                self.result_entry.insert("1.0", base64.b64encode(encrypted).decode())

            def decrypt(self):
                encrypted_message = self.input_entry.get("1.0", tk.END).strip()
                key_string = self.key_entry.get().strip() or "150847"
                if not encrypted_message:
                    messagebox.showwarning("Warning", "Please enter both an encrypted message and the correct key.")
                    return

                try:
                    encrypted = base64.b64decode(encrypted_message)
                    decrypted = self.xor_encrypt_decrypt(encrypted, self.generate_key(key_string)).decode()
                except Exception:
                    messagebox.showerror("Error", "Invalid encrypted message or key.")
                    return

                self.result_entry.delete("1.0", tk.END)
                self.result_entry.insert("1.0", decrypted)

            def copy_result(self):
                result = self.result_entry.get("1.0", tk.END).strip()
                if not result:
                    messagebox.showwarning("Warning", "No result to copy.")
                    return

                self.master.clipboard_clear()
                self.master.clipboard_append(result)
                self.master.update()

            def clear_fields(self):
                self.input_entry.delete("1.0", tk.END)
                self.key_entry.delete(0, tk.END)
                self.result_entry.delete("1.0", tk.END)

            def use_default_key(self):
                self.key_entry.delete(0, tk.END)
                self.key_entry.insert(0, "150847")

            def open_browser(self):
                _open_browser_page()

        root = tk.Tk()
        PrivatorApp(root)
        root.mainloop()
    except ImportError:
        print("Try Installing Tkinter Module.")


def privator_browser() -> None:
    try:
        _open_browser_page()
    except Exception:
        print("Try opening with a browser that allows local files.")


if __name__ == "__main__":
    privator()