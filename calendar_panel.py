import tkinter as tk
from tkinter import ttk
import requests
from ics import Calendar
from datetime import datetime
import pytz

class CalendarPanel(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#F6F9FC")
        self.pack(fill="both", expand=True)
        self.display_events()

    def display_events(self):
        try:
            # Replace with your real .ics URL
            ics_url = "https://chrisdurer-cael.github.io/cael-calendar/index.ics"
            response = requests.get(ics_url)
            calendar = Calendar(response.text)

            events = sorted(calendar.events, key=lambda e: e.begin)[:10]  # Limit to next 10
            for event in events:
                begin_time = event.begin.to('local').format('YYYY-MM-DD HH:mm')
                label = tk.Label(self, text=f"{begin_time} - {event.name}", anchor="w", bg="#F6F9FC", font=("Arial", 12))
                label.pack(fill="x", padx=20, pady=5)
        except Exception as e:
            error_label = tk.Label(self, text=f"Error loading calendar: {e}", fg="red", bg="#F6F9FC")
            error_label.pack(pady=20)
