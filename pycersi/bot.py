import json
import tempfile
import threading
import webbrowser

import tkinter as tk
from tkinter import scrolledtext, ttk

MODEL = "nvidia/nemotron-nano-9b-v2:free"
API_URL = "https://openrouter.ai/api/v1/chat/completions"


def _get_ai_response(messages, user_input, api_key):
    import requests

    messages.append({"role": "user", "content": user_input})
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.post(
            API_URL,
            headers=headers,
            data=json.dumps({
                "model": MODEL,
                "messages": messages,
            }),
            timeout=90,
        )
        data = response.json()

        if "error" in data:
            return f"[Error] {data['error'].get('message', 'Unknown API error')}"

        reply = data["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        return reply
    except Exception as exc:
        return f"[Error] {exc}"


def _cli_mode(api_key):
        messages = []
        print("\n=== PyCersi AI Bot | CLI Mode ===")
        print("Model:", MODEL)
        print("Type EXIT or QUIT to stop.\n")

        while True:
                user_input = input("You: ").strip()
                if user_input.lower() in ["exit", "quit"]:
                        print("Exiting PyCersi AI Bot. Goodbye!")
                        break
                if not user_input:
                        continue

                reply = _get_ai_response(messages, user_input, api_key)
                print("PyCersi:", reply)
                print()


def _tkinter_mode(api_key):
        messages = []

        root = tk.Tk()
        root.title("PyCersi AI Bot")
        root.geometry("860x650")
        root.minsize(760, 580)
        root.configure(bg="#0f172a")

        style = ttk.Style(root)
        style.theme_use("clam")
        style.configure("Top.TFrame", background="#111827")
        style.configure("Main.TFrame", background="#0f172a")
        style.configure("Accent.TButton", font=("Segoe UI", 11, "bold"), padding=8)

        top_bar = ttk.Frame(root, style="Top.TFrame", padding=(16, 12))
        top_bar.pack(fill=tk.X)

        title = tk.Label(
                top_bar,
                text="PyCersi AI Bot",
                bg="#111827",
                fg="#f8fafc",
                font=("Segoe UI", 18, "bold"),
        )
        title.pack(side=tk.LEFT)

        model_badge = tk.Label(
                top_bar,
                text=f"Model: {MODEL}",
                bg="#1f2937",
                fg="#93c5fd",
                font=("Consolas", 10, "bold"),
                padx=10,
                pady=6,
        )
        model_badge.pack(side=tk.RIGHT)

        body = ttk.Frame(root, style="Main.TFrame", padding=16)
        body.pack(fill=tk.BOTH, expand=True)

        chat_display = scrolledtext.ScrolledText(
                body,
                wrap=tk.WORD,
                font=("Consolas", 11),
                bg="#020617",
                fg="#e2e8f0",
                insertbackground="#e2e8f0",
                relief=tk.FLAT,
                padx=12,
                pady=12,
                height=24,
        )
        chat_display.pack(fill=tk.BOTH, expand=True)
        chat_display.insert(tk.END, "PyCersi is online. Ask anything.\n\n")
        chat_display.config(state=tk.DISABLED)

        input_wrap = tk.Frame(body, bg="#0f172a")
        input_wrap.pack(fill=tk.X, pady=(12, 0))

        user_input = tk.Entry(
                input_wrap,
                font=("Segoe UI", 12),
                bg="#e2e8f0",
                fg="#0f172a",
                relief=tk.FLAT,
        )
        user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=9)

        def display_message(label, msg):
                chat_display.config(state=tk.NORMAL)
                chat_display.insert(tk.END, f"{label}: {msg}\n\n")
                chat_display.config(state=tk.DISABLED)
                chat_display.yview(tk.END)

        def on_send():
                user_text = user_input.get().strip()
                if not user_text:
                        return
                if user_text.lower() in ["exit", "quit"]:
                        root.destroy()
                        return

                display_message("You", user_text)
                user_input.delete(0, tk.END)

                def run_in_thread():
                        reply = _get_ai_response(messages, user_text, api_key)
                        root.after(0, lambda: display_message("PyCersi", reply))

                threading.Thread(target=run_in_thread, daemon=True).start()

        send_button = ttk.Button(input_wrap, text="Send", style="Accent.TButton", command=on_send)
        send_button.pack(side=tk.LEFT, padx=(10, 0))

        user_input.bind("<Return>", lambda event: on_send())
        user_input.focus_set()
        root.mainloop()


def _build_browser_html():
        return f"""<!doctype html>
<html lang=\"en\">
<head>
    <meta charset=\"utf-8\" />
    <meta name=\"viewport\" content=\"width=device-width,initial-scale=1\" />
    <title>PyCersi AI Bot</title>
    <style>
        :root {{
            --bg1: #0f172a;
            --bg2: #1e293b;
            --panel: rgba(2, 6, 23, 0.76);
            --text: #e2e8f0;
            --muted: #94a3b8;
            --accent: #38bdf8;
            --accent-2: #f59e0b;
            --user: #0b3b57;
            --assistant: #2b1f0c;
        }}
        * {{ box-sizing: border-box; }}
        body {{
            margin: 0;
            min-height: 100vh;
            font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
            color: var(--text);
            background: radial-gradient(circle at 10% 10%, #1d4ed8 0%, transparent 40%),
                                    radial-gradient(circle at 90% 20%, #f59e0b 0%, transparent 35%),
                                    linear-gradient(140deg, var(--bg1), var(--bg2));
            display: grid;
            place-items: center;
            padding: 20px;
        }}
        .app {{
            width: min(980px, 100%);
            height: min(780px, calc(100vh - 40px));
            background: var(--panel);
            border: 1px solid rgba(148, 163, 184, 0.2);
            border-radius: 20px;
            backdrop-filter: blur(10px);
            display: grid;
            grid-template-rows: auto auto 1fr auto;
            overflow: hidden;
            box-shadow: 0 20px 80px rgba(2, 6, 23, 0.5);
        }}
        .header {{
            padding: 18px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(148, 163, 184, 0.2);
        }}
        .title {{ font-size: 1.25rem; font-weight: 800; letter-spacing: 0.4px; }}
        .model {{
            font-family: Consolas, monospace;
            font-size: 0.8rem;
            color: var(--accent);
            background: rgba(56, 189, 248, 0.12);
            padding: 6px 10px;
            border-radius: 999px;
            border: 1px solid rgba(56, 189, 248, 0.25);
        }}
        .key-wrap {{
            display: grid;
            grid-template-columns: 1fr auto;
            gap: 10px;
            padding: 14px 20px;
            border-bottom: 1px solid rgba(148, 163, 184, 0.2);
        }}
        input, button, textarea {{ font: inherit; }}
        .key-input, .msg-input {{
            width: 100%;
            border: 1px solid rgba(148, 163, 184, 0.3);
            background: rgba(15, 23, 42, 0.9);
            color: var(--text);
            border-radius: 12px;
            padding: 10px 12px;
            outline: none;
        }}
        .chat {{
            overflow: auto;
            padding: 18px 20px;
            display: flex;
            flex-direction: column;
            gap: 12px;
        }}
        .bubble {{
            max-width: 85%;
            padding: 10px 12px;
            border-radius: 12px;
            line-height: 1.4;
            white-space: pre-wrap;
            border: 1px solid rgba(148, 163, 184, 0.2);
        }}
        .you {{ align-self: flex-end; background: var(--user); }}
        .bot {{ align-self: flex-start; background: var(--assistant); }}
        .composer {{
            display: grid;
            grid-template-columns: 1fr auto;
            gap: 10px;
            padding: 16px 20px;
            border-top: 1px solid rgba(148, 163, 184, 0.2);
        }}
        .btn {{
            background: linear-gradient(135deg, var(--accent), var(--accent-2));
            color: #001018;
            border: 0;
            font-weight: 800;
            padding: 10px 14px;
            border-radius: 12px;
            cursor: pointer;
        }}
        .hint {{ color: var(--muted); font-size: 0.86rem; padding: 0 20px 12px; }}
        @media (max-width: 720px) {{
            .app {{ height: calc(100vh - 20px); border-radius: 14px; }}
            .bubble {{ max-width: 92%; }}
            .key-wrap, .composer {{ grid-template-columns: 1fr; }}
        }}
    </style>
</head>
<body>
    <main class=\"app\">
        <section class=\"header\">
            <div class=\"title\">PyCersi AI Bot | Browser Mode</div>
            <div class=\"model\">{MODEL}</div>
        </section>
        <section class=\"key-wrap\">
            <input id=\"apiKey\" class=\"key-input\" type=\"password\" placeholder=\"Enter your OpenRouter API key\" />
            <button id=\"saveKey\" class=\"btn\">Save Key</button>
        </section>
        <section id=\"chat\" class=\"chat\"></section>
        <section class=\"composer\">
            <textarea id=\"message\" class=\"msg-input\" rows=\"2\" placeholder=\"Type your message...\"></textarea>
            <button id=\"send\" class=\"btn\">Send</button>
        </section>
        <div class=\"hint\">Type EXIT or QUIT to clear and close this tab manually.</div>
    </main>
    <script>
        const model = {json.dumps(MODEL)};
        const apiUrl = {json.dumps(API_URL)};
        let apiKey = "";
        const messages = [];

        const chat = document.getElementById("chat");
        const apiKeyInput = document.getElementById("apiKey");
        const saveKeyBtn = document.getElementById("saveKey");
        const sendBtn = document.getElementById("send");
        const messageInput = document.getElementById("message");

        function addBubble(text, role) {{
            const div = document.createElement("div");
            div.className = `bubble ${{role}}`;
            div.textContent = text;
            chat.appendChild(div);
            chat.scrollTop = chat.scrollHeight;
        }}

        async function ask() {{
            const prompt = messageInput.value.trim();
            if (!prompt) return;
            if (!apiKey) {{
                alert("Please save your OpenRouter API key first.");
                return;
            }}

            addBubble(prompt, "you");
            messageInput.value = "";

            if (["exit", "quit"].includes(prompt.toLowerCase())) {{
                addBubble("Session ended. You can close this tab.", "bot");
                return;
            }}

            messages.push({{ role: "user", content: prompt }});
            addBubble("Thinking...", "bot");
            const thinking = chat.lastElementChild;

            try {{
                const res = await fetch(apiUrl, {{
                    method: "POST",
                    headers: {{
                        "Authorization": `Bearer ${{apiKey}}`,
                        "Content-Type": "application/json"
                    }},
                    body: JSON.stringify({{ model, messages }})
                }});

                const data = await res.json();
                if (data.error) {{
                    thinking.textContent = `[Error] ${{data.error.message || "Unknown API error"}}`;
                    return;
                }}

                const reply = data.choices?.[0]?.message?.content || "No response.";
                messages.push({{ role: "assistant", content: reply }});
                thinking.textContent = reply;
            }} catch (err) {{
                thinking.textContent = `[Error] ${{err}}`;
            }}
        }}

        saveKeyBtn.addEventListener("click", () => {{
            apiKey = apiKeyInput.value.trim();
            if (!apiKey) {{
                alert("Please enter a valid API key.");
                return;
            }}
            addBubble("API key loaded for this tab session.", "bot");
        }});

        sendBtn.addEventListener("click", ask);
        messageInput.addEventListener("keydown", (event) => {{
            if (event.key === "Enter" && !event.shiftKey) {{
                event.preventDefault();
                ask();
            }}
        }});

        addBubble("Welcome to PyCersi Browser Mode. Enter your OpenRouter key to begin.", "bot");
    </script>
</body>
</html>
"""


def _browser_mode():
        html = _build_browser_html()
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as tmp_file:
                tmp_file.write(html)
                file_path = tmp_file.name

        webbrowser.open(f"file://{file_path}")
        print("Browser mode launched.")
        print("Enter your OpenRouter API key in the page and start chatting.")


def bot():
        print("\n=== PyCersi AI Bot ===")
        print("1. CLI Mode")
        print("2. Tkinter Mode")
        print("3. Browser Mode")
        print("Model:", MODEL)
        print("======================")

        choice = input("Choose mode (1/2/3): ").strip()

        if choice == "1":
                api_key = input("Enter OpenRouter API key: ").strip()
                if not api_key:
                        print("API key is required for CLI Mode.")
                        return
                _cli_mode(api_key)
                return

        if choice == "2":
                api_key = input("Enter OpenRouter API key for Tkinter Mode: ").strip()
                if not api_key:
                        print("API key is required for Tkinter Mode.")
                        return
                _tkinter_mode(api_key)
                return

        if choice == "3":
                _browser_mode()
                return

        print("Invalid choice. Exiting...")


if __name__ == "__main__":
        bot()