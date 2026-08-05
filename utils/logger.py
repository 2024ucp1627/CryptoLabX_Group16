from datetime import datetime


LOG_FILE = "logs/activity.log"


def log_activity(option):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"{current_time} | {option}\n")