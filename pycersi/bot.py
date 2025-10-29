import requests
import json
import threading
import tkinter as tk
from tkinter import scrolledtext

# ==========================================
# === CONFIG ===
# ==========================================
API_KEY = "<>"
MODEL = "nvidia/nemotron-nano-12b-v2-vl:free"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

messages = []  # Conversation memory


# ==========================================
# === BACKEND FUNCTION ===
# ==========================================
def get_ai_response(user_input):
    """Handles sending a chat message and getting AI response (used by both modes)."""
    global messages
    messages.append({"role": "user", "content": user_input})

    try:
        response = requests.post(
            API_URL,
            headers=HEADERS,
            data=json.dumps({
                "model": MODEL,
                "messages": messages,
            }),
        )
        data = response.json()

        if "error" in data:
            return f"[Error] {data['error']['message']}"

        reply = data["choices"][0]["message"]["content"]
        messages.append({"role": "assistant", "content": reply})
        return reply

    except Exception as e:
        return f"[Error] {str(e)}"


# ==========================================
# === MODE 1: LIGHT MODE (CONSOLE) ===
# ==========================================
def console_mode():
    print("=== PyCersi AI Bot (Light Mode) ===")
    print("Type EXIT or QUIT to stop.\n")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("Exiting PyCersi AI Bot. Goodbye!")
            break

        reply = get_ai_response(user_input)
        print("PyCersi:", reply)
        print()


# ==========================================
# === MODE 2: UI MODE (TKINTER) ===
# ==========================================
def ui_mode():
    def display_message(msg):
        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, msg + "\n\n")
        chat_display.config(state=tk.DISABLED)
        chat_display.yview(tk.END)

    def on_send():
        user_text = user_input.get().strip()
        if not user_text:
            return
        if user_text.lower() in ["exit", "quit"]:
            root.destroy()
            return

        display_message(f"You: {user_text}")
        user_input.delete(0, tk.END)

        def run_in_thread():
            reply = get_ai_response(user_text)
            display_message(f"PyCersi: {reply}")

        threading.Thread(target=run_in_thread, daemon=True).start()

    # === TKINTER UI ===
    root = tk.Tk()
    root.title("PyCersi AI Bot (UI Mode)")
    root.geometry("700x600")
    root.resizable(False, False)
    root.configure(bg="#ffffff")  # Light mode background

    chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Consolas", 11), bg="#f7f7f7")
    chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    chat_display.insert(tk.END, "🤖 PyCersi AI Bot (UI Mode) is running...\nType your message below.\n\n")
    chat_display.config(state=tk.DISABLED)

    user_input = tk.Entry(root, font=("Consolas", 12))
    user_input.pack(padx=10, pady=(0, 10), fill=tk.X)

    send_button = tk.Button(root, text="Send", font=("Consolas", 12, "bold"), bg="#007acc", fg="white", command=on_send)
    send_button.pack(pady=(0, 10))

    user_input.bind("<Return>", lambda event: on_send())
    root.mainloop()


# ==========================================
# === SWITCH CASE MENU ===
# ==========================================
def main():
    print("\n=== PyCersi AI Bot ===")
    print("1. Light Mode (Console)")
    print("2. UI Mode (Tkinter)")
    print("======================")

    choice = input("Choose mode (1 or 2): ").strip()

    match choice:
        case "1":
            console_mode()
        case "2":
            ui_mode()
        case _:
            print("Invalid choice. Exiting...")


if __name__ == "__main__":
    main()