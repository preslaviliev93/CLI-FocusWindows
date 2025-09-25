# Windows Application Usage Tracker

This project tracks your active application usage times on Windows and displays detailed statistics when the program is terminated (`CTRL + C`).

It is useful for analyzing how much time you spend on each application and specific windows (e.g., browser tabs).

---

## Features

- Tracks active window focus and records the time spent.
- Groups statistics by application (process name).
- Shows detailed breakdown per window title.
- Simple console report on exit.
- Lightweight and configurable.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/preslaviliev93/CLI-FocusWindows
   cd CLI-FocusWindows

2. Install requirements:

   ```bash
   pip install requirements.txt


3. Run the script:

   ```bash
   python main.py


## Sample output:

```text
Tracking ... Press CTRL+C to exit ...

Program exited by user
========= brave.exe (Total time: 00:10:05) =========
Messenger | Facebook - Brave -> 00:01:20
Facebook - Brave -> 00:08:45


