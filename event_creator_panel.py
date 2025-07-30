import tkinter as tk
from tkinter import messagebox
from ics import Calendar, Event
from datetime import datetime
import os
import subprocess

class EventCreatorPanel(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#F6F9FC")
        self.pack(fill="both", expand=True)

        tk.Label(self, text="Create New Event", font=("Arial", 16), bg="#F6F9FC").pack(pady=10)

        self.title_entry = self._create_labeled_entry("Title")
        self.desc_entry = self._create_labeled_entry("Description")
        self.date_entry = self._create_labeled_entry("Date (YYYY-MM-DD)")
        self.time_entry = self._create_labeled_entry("Time (HH:MM, 24h)")

        tk.Button(self, text="Save Event", command=self.save_event, bg="#2980b9", fg="white").pack(pady=20)

    def _create_labeled_entry(self, label):
        frame = tk.Frame(self, bg="#F6F9FC")
        frame.pack(pady=5)
        tk.Label(frame, text=label, bg="#F6F9FC").pack(side="left", padx=10)
        entry = tk.Entry(frame, width=40)
        entry.pack(side="left")
        return entry

    def save_event(self):
        title = self.title_entry.get().strip()
        description = self.desc_entry.get().strip()
        date_str = self.date_entry.get().strip()
        time_str = self.time_entry.get().strip()

        if not (title and date_str and time_str):
            messagebox.showerror("Missing Info", "Please fill out Title, Date, and Time.")
            return

        try:
            dt_str = f"{date_str} {time_str}"
            event_time = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
        except ValueError:
            messagebox.showerror("Format Error", "Invalid date or time format.")
            return

        event = Event()
        event.name = title
        event.begin = event_time
        event.description = description

        cal = Calendar()
        cal.events.add(event)

        filename = f"event_{date_str}.ics"
        with open(filename, "w") as f:
            f.writelines(cal.serialize_iter())

        messagebox.showinfo("Success", f"Event '{title}' saved to {filename}.")

        self.push_to_github(filename)

    def push_to_github(self, filename):
        credentials_path = os.path.expanduser("~/.gh_credentials")
        if not os.path.exists(credentials_path):
            messagebox.showerror("GitHub Sync Error", "Missing ~/.gh_credentials file.")
            return

        creds = {}
        with open(credentials_path) as f:
            for line in f:
                if "=" in line:
                    key, val = line.strip().split("=", 1)
                    creds[key.strip()] = val.strip()

        repo_url = f"https://{creds['GITHUB_USERNAME']}:{creds['GITHUB_TOKEN']}@github.com/{creds['REPO']}.git"

        try:
            subprocess.run(["git", "init"], check=True)
            subprocess.run(["git", "remote", "remove", "origin"], check=False)
            subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)
            subprocess.run(["git", "add", filename], check=True)
            subprocess.run(["git", "commit", "-m", f"Add event {filename}"], check=True)
            subprocess.run(["git", "push", "origin", "main"], check=True)
        except subprocess.CalledProcessError as e:
            messagebox.showerror("GitHub Push Error", f"Failed to push to GitHub:\n{str(e)}")
