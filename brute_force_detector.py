import time
from collections import defaultdict, deque

# File created by the test site
log_file = "login_attempts.log"

# File where we log detected attacks
attack_log = "attack_log.txt"

# Detection rules
max_failures = 5        # Number of failed attempts
time_window = 60        # Time window in seconds

# Store failed attempts per IP
# Each IP gets a queue (deque) of timestamps
failed_attempts = defaultdict(deque)

def follow(file):
# Generator function that watches a file in real time.
# Similar to 'tail -f' in Linux.

    file.seek(0, 2)     # Move to end of file

    while True:
        line = file.readline()
        if not line:
            time.sleep(0.5)
            continue
        yield line


def log_attack(ip, count):
# Write detected brute force activity to a log file.

    timestamp = time.strftime("%d-%m-%Y %H:%M:%S")
    message = f"{timestamp} | BRUTE FORCE DETECTED | IP: {ip} | Failures: {count}\n"

    with open(attack_log, "a") as log:
        log.write(message)

    print(message.strip())


def main():
    print("Monitoring login attempts for brute force activity...\n")

    with open(log_file, "r") as file:
        loglines = follow(file)

        for line in loglines:
            # Example log line:
            # 2025-01-10 12:30:01 | 127.0.0.1 | admin | Failure!

            parts = line.strip().split(" | ")
            timestamp_str, ip, username, result = parts

            # Convert timestamp to epoch seconds
            timestamp = time.mktime(time.strptime(timestamp_str, "%d-%m-%Y %H:%M:%S"))

            if result == "Failure!":
                attempts = failed_attempts[ip]
                attempts.append(timestamp)

                # Remove attempts older than time_window
                while attempts and timestamp - attempts[0] > time_window:
                    attempts.popleft()

                # If threshold exceeded, flag as brute force
                if len(attempts) >= max_failures:
                    log_attack(ip, len(attempts))
                    attempts.clear()        # Reset to avoid spam alerts

if __name__ == "__main__":
    main()