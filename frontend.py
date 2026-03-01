import tkinter as tk
from tkinter import scrolledtext

class OSINTUI:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Modular OSINT Investigator v1.0")
        self.root.geometry("600x500")
        self.setup_widgets()

    def setup_widgets(self):
        tk.Label(self.root, text="Target Domain:", font=("Arial", 12)).pack(pady=10)
        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack()

        tk.Button(self.root, text="Run Investigation", command=self.run_scan, bg="#2c3e50", fg="white").pack(pady=10)

        self.output = scrolledtext.ScrolledText(self.root, width=70, height=20)
        self.output.pack(padx=10, pady=10)

    def run_scan(self):
        domain = self.entry.get()
        self.output.delete(1.0, tk.END)
        self.output.insert(tk.END, f"Investigating: {domain}...\n" + "-"*30 + "\n")
        
        result = self.controller.process_investigation(domain)
        
        if "error" in result:
            self.output.insert(tk.END, f"ERROR: {result['error']}")
        else:
            self.output.insert(tk.END, f"DNS RECORDS:\n{result['dns']}\n\n")
            self.output.insert(tk.END, f"WHOIS DATA:\n{result['whois']}\n")
