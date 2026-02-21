import csv
import time
import random
from datetime import datetime

log_file = "backend/data/realtime_logs.csv"

levels = ["INFO", "WARN", "ERROR"]
messages = {
    "INFO": ["Server started", "User logged in", "File uploaded"],
    "WARN": ["High memory usage", "Disk almost full"],
    "ERROR": ["Database failed", "Connection timeout"]
}

# Create file with header if not exists
with open(log_file, "a", newline="") as f:
    writer = csv.writer(f)
    if f.tell() == 0:
        writer.writerow(["timestamp", "level", "message"])

while True:
    level = random.choice(levels)
    message = random.choice(messages[level])
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(log_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, level, message])

    print(f"{timestamp} - {level} - {message}")
    time.sleep(3)