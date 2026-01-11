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

```
pip install flask
```

---

## How To Run The Project

### 1. Start the Test Site

```
python test_site.py
```

Visit in your browser:

```
http://127.0.0.1:5000
```

Try logging in with incorrect credentials multiple times.

---

### 2. Start The Brute Force Detector

In a **seperate terminal window**:

```
python brute_force_detector.py
```

The detector will begin monitoring login attempts in real time.

---

## Example Detection Output

Console output:

`2025-01-10 12:35:14 | BRUTE FORCE DETECTED | IP: 127.0.0.1 | Failures: 5`

attack_log.txt:

`2025-01-10 12:35:14 | BRUTE FORCE DETECTED | IP: 127.0.0.1 | Failures: 5`

---

## Configuration Options

You can adjust detection sensitivity in `brute_force_detector.py`:

- `max_failures` - number of failed attempts before triggering
- `time_window` - time window (seconds) for counting failures

Example:

```
max_failures = 5
time_window = 60
```

---

