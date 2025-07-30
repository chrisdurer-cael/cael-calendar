import os
import requests
from tkinter import messagebox, Tk

calendar_urls = {
    "work": "https://chrisdurer-cael.github.io/cael-calendar/cael-work/index.ics",
    "appts": "https://chrisdurer-cael.github.io/cael-calendar/cael-appts/index.ics",
    "home": "https://chrisdurer-cael.github.io/cael-calendar/cael-home/index.ics",
    "projects": "https://chrisdurer-cael.github.io/cael-calendar/cael-projects/index.ics",
    "health": "https://chrisdurer-cael.github.io/cael-calendar/cael-health/index.ics",
}

calendar_path = os.path.expanduser("~/Cael/Calendar")
os.makedirs(calendar_path, exist_ok=True)

success = True
for name, url in calendar_urls.items():
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(os.path.join(calendar_path, f"{name}.ics"), "wb") as f:
            f.write(response.content)
    except Exception as e:
        success = False

root = Tk()
root.withdraw()
if success:
    messagebox.showinfo("Cael Core", "✅ Calendars synced successfully!")
else:
    messagebox.showerror("Cael Core", "❌ Failed to sync one or more calendars.")
