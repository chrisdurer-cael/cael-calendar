
import tkinter as tk
from tkinter import ttk

# === COLORS & STYLES ===
BG = "#f3f7fa"
NAV_BG = "#d6e6f2"
BTN_ACTIVE = "#c4dbed"
TEXT = "#1f2a36"
FONT = ("Segoe UI", 12)
TITLE_FONT = ("Segoe UI", 16, "bold")

class CaelCoreApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cael Core 2.0")
        self.geometry("800x500")
        self.configure(bg=BG)

        # Layout: Left = nav, Right = content
        self.nav_frame = tk.Frame(self, bg=NAV_BG, width=160)
        self.nav_frame.pack(side="left", fill="y")

        self.content_frame = tk.Frame(self, bg=BG)
        self.content_frame.pack(side="right", fill="both", expand=True)

        # Nav buttons
        self.nav_buttons = {}
        nav_items = ["Home", "Calendar", "Finance", "Logs", "Voice"]
        for item in nav_items:
            btn = tk.Button(self.nav_frame, text=item, bg=NAV_BG, fg=TEXT, font=FONT, relief="flat",
                            activebackground=BTN_ACTIVE, anchor="w", command=lambda i=item: self.show_panel(i))
            btn.pack(fill="x", pady=2, padx=5)
            self.nav_buttons[item] = btn

        # Panels
        self.panels = {
            "Home": self.create_home_panel(),
            "Calendar": self.create_placeholder_panel("📅 Calendar Module Coming Soon"),
            "Finance": self.create_placeholder_panel("💰 Finance Module Coming Soon"),
            "Logs": self.create_placeholder_panel("📓 Logs Viewer Coming Soon"),
            "Voice": self.create_placeholder_panel("🎤 Voice Module Coming Soon"),
        }

        self.show_panel("Home")

    def create_home_panel(self):
        frame = tk.Frame(self.content_frame, bg=BG)
        label = tk.Label(frame, text="🩵 Welcome to Cael Core", font=TITLE_FONT, fg=TEXT, bg=BG)
        label.pack(pady=20)
        return frame

    def create_placeholder_panel(self, text):
        frame = tk.Frame(self.content_frame, bg=BG)
        label = tk.Label(frame, text=text, font=FONT, fg=TEXT, bg=BG)
        label.pack(pady=20)
        return frame

    def show_panel(self, name):
        for panel in self.panels.values():
            panel.pack_forget()
        self.panels[name].pack(fill="both", expand=True)

if __name__ == "__main__":
    app = CaelCoreApp()
    app.mainloop()
