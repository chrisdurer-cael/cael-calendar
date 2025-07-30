import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from calendar_panel_multi import MultiCalendarPanel
from event_creator_panel import EventCreatorPanel

class CaelCoreApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cael Core")
        self.geometry("900x600")
        self.configure(bg="#F6F9FC")

        # Side Navigation Bar
        self.nav_frame = tk.Frame(self, bg="#DDEEFF", width=120)
        self.nav_frame.pack(side="left", fill="y")

        nav_label = tk.Label(self.nav_frame, text="Cael", bg="#DDEEFF", font=("Arial", 16, "bold"))
        nav_label.pack(pady=20)

        self.nav_buttons = [
            ("Home", self.show_home),
            ("Calendar", self.show_calendar),
            ("Finance", self.show_finance),
        ]

        for text, command in self.nav_buttons:
            btn = tk.Button(self.nav_frame, text=text, command=command, width=12)
            btn.pack(pady=10)

        # Add Event button
        tk.Button(self.nav_frame, text="➕ Add Event", command=self.show_create_event, width=12).pack(pady=10)

        # Main Content Frame
        self.content_frame = tk.Frame(self, bg="#F6F9FC")
        self.content_frame.pack(side="left", fill="both", expand=True)

        self.current_panel = None
        self.show_home()

    def clear_panel(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_home(self):
        self.clear_panel()

        # Avatar
        avatar_frame = tk.Frame(self.content_frame, bg="#F6F9FC")
        avatar_frame.pack(pady=10)

        try:
            avatar_image = Image.open("/home/cael/cael-core-gui/assets/avatar-default.png")
            avatar_image = avatar_image.resize((128, 128), Image.Resampling.LANCZOS)
            avatar_photo = ImageTk.PhotoImage(avatar_image)
            avatar_label = tk.Label(avatar_frame, image=avatar_photo, bg="#F6F9FC")
            avatar_label.image = avatar_photo  # Prevent garbage collection
            avatar_label.pack()
        except Exception as e:
            tk.Label(avatar_frame, text="(Avatar failed to load)", bg="#F6F9FC", fg="red").pack()

        # Welcome message
        tk.Label(self.content_frame, text="Welcome back, Christopher 🩵", font=("Arial", 16), bg="#F6F9FC").pack(pady=10)

        # Home Buttons
        buttons = ["Log Mood", "Log Hydration", "Log Food", "Sync Calendar"]
        for b in buttons:
            tk.Button(self.content_frame, text=b, width=20).pack(pady=5)

    def show_calendar(self):
        self.clear_panel()
        MultiCalendarPanel(self.content_frame)

    def show_create_event(self):
        self.clear_panel()
        EventCreatorPanel(self.content_frame)

    def show_finance(self):
        self.clear_panel()
        tk.Label(self.content_frame, text="(Finance tracker coming soon)", font=("Arial", 14), bg="#F6F9FC").pack(pady=20)

if __name__ == "__main__":
    app = CaelCoreApp()
    app.mainloop()
