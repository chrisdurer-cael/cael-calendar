import tkinter as tk
from tkinter import ttk
import requests
from ics import Calendar
from datetime import datetime
import pytz

class MultiCalendarPanel(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#F6F9FC")
        self.pack(fill="both", expand=True)
        self.display_events()

    def display_events(self):
        urls = [
            ("Master", "https://chrisdurer-cael.github.io/cael-calendar/index.ics"),
            ("Health", "https://chrisdurer-cael.github.io/cael-calendar/health.ics"),
            ("Journal", "https://chrisdurer-cael.github.io/cael-calendar/journal.ics"),
            ("Projects", "https://chrisdurer-cael.github.io/cael-calendar/projects.ics"),
            ("Kids", "https://chrisdurer-cael.github.io/cael-calendar/kids.ics"),
        ]

        all_events = []

        for label, url in urls:
            try:
                response = requests.get(url)
                calendar = Calendar(response.text)
                for event in calendar.events:
                    all_events.append((label, event))
            except Exception as e:
                error = tk.Label(self, text=f"Error loading {label} calendar: {e}", fg="red", bg="#F6F9FC")
                error.pack(pady=5)

        # Sort and display next 15 events
        all_events.sort(key=lambda e: e[1].begin)
        all_events = all_events[:15]

        for label, event in all_events:
            begin_time = event.begin.to('local').format('YYYY-MM-DD HH:mm')
            color = self.get_color_for_label(label)
            text = f"[{label}] {begin_time} - {event.name}"
            label_widget = tk.Label(self, text=text, anchor="w", bg="#F6F9FC", fg=color, font=("Arial", 12))
            label_widget.pack(fill="x", padx=20, pady=3)

    def get_color_for_label(self, label):
        colors = {
            "Master": "#2c3e50",
            "Health": "#e74c3c",
            "Journal": "#8e44ad",
            "Projects": "#2980b9",
            "Kids": "#27ae60"
        }
        return colors.get(label, "#000000")
