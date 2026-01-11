# Brute Force Detection

This repository contains a Python project that demonstrates how brute force login attempts can be detected in real time using log analysis.

The project in designed for demonstation purposes and uses a local test site only. **No attacking, scanning, or exploitation is performed.**

---

## What This Project Does

- Runs a local Flask test site with a login form
- Logs every login attempt (success or failure)
- Monitors the log file in real time
- Detects brute force like behaviour based on configurable thresholds
- Logs detected attacks to a seperate file

This mirrors how real world security tools (IDS / SIEM / Fail2Ban style systems) work as a simplified level.

---

## How Brute Force Detection Works

The detector watches for:

- Multiple failed login attempts:
  - from the same IP address
  - within a short time window
 
If the threshold is exceeded, the activity is flagged as a potential brute force attack.

---

## Requirements

- Python 3.8+
- Flask

Install dependencies:

`pip install flask`
