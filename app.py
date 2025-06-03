import tkinter as tk
from tkinter import messagebox, scrolledtext
import joblib
import os
import re
from datetime import datetime

# Verificare existență fișiere model
if not os.path.exists("phishing_model.pkl") or not os.path.exists("vectorizer.pkl"):
    messagebox.showerror("Eroare", "Fișierele modelului nu au fost găsite!")
    exit()

model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Funcție detectare linkuri suspecte
def detect_suspicious_links(text):
    links = re.findall(r'https?://[^\s]+', text)
    flagged = []
    for link in links:
        if any(bad in link for bad in ['bit.ly', 'tinyurl', '.ru', '.xyz', 'http://']):
            flagged.append(link)
    return flagged

# Verifică e-mail + linkuri
def check_email():
    email_text = text_input.get("1.0", tk.END).strip()
    if not email_text:
        messagebox.showwarning("Atenție", "Introdu textul e-mailului.")
        return

    vectorized = vectorizer.transform([email_text])
    prediction = model.predict(vectorized)
    verdict_ml = "⚠️ PHISHING!" if prediction[0] == 1 else " LEGITIM"

    flagged_links = detect_suspicious_links(email_text)
    if flagged_links:
        verdict = f"{verdict_ml}  Link suspect detectat:\n" + "\n".join(flagged_links)
    else:
        verdict = verdict_ml

    result.set(verdict)

    with open("logs.txt", "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] Rezultat: {verdict_ml}\nText: {email_text}\n{'-'*50}\n")

# Resetare
def reset_fields():
    text_input.delete("1.0", tk.END)
    result.set("")

# Log viewer
def view_logs():
    if not os.path.exists("logs.txt"):
        messagebox.showinfo("Loguri", "Nu există loguri salvate.")
        return

    with open("logs.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    last_entries = "".join(lines[-50:])  # ultimele ~10 e-mailuri (50 linii)
    log_win = tk.Toplevel(root)
    log_win.title("Loguri recente")
    log_text = scrolledtext.ScrolledText(log_win, width=80, height=25)
    log_text.pack()
    log_text.insert(tk.END, last_entries)
    log_text.config(state=tk.DISABLED)

# Interfață
root = tk.Tk()
root.title("Detector Phishing E-mail")
root.geometry("650x500")

tk.Label(root, text="Introdu textul e-mailului:", font=("Arial", 12)).pack(pady=10)
text_input = tk.Text(root, height=10, width=75)
text_input.pack()

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Verifică", command=check_email, font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
tk.Button(frame_buttons, text="Resetează", command=reset_fields, font=("Arial", 12)).pack(side=tk.LEFT, padx=10)
tk.Button(frame_buttons, text="Vezi loguri", command=view_logs, font=("Arial", 12)).pack(side=tk.LEFT, padx=10)

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 14, "bold"), fg="blue").pack(pady=20)

root.mainloop()
