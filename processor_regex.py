import re
def classify_with_regex(log_message):
    regex_patterns = {
        r"User User\d+ logged (in|out).": "User Action",
        r"Backup (started|ended) at .*": "System Notification",
        r"Backup completed successfully.": "System Notification",
        r"System updated to version .*": "System Notification",
        r"File .* uploaded successfully by user .*": "System Notification",
        r"Disk cleanup completed successfully.": "System Notification",
        r"System reboot initiated by user .*": "System Notification",
        r"Account with ID .* created by .*": "User Action"
    }
    for pattern, label in regex_patterns.items():
        if re.search(pattern, log_message, re.IGNORECASE):
            return label
    return None

if __name__ == "__main__":
    print (classify_with_regex("User User123 logged in.")) # User Action
    print (classify_with_regex("Backup started at 2020-01-01 12:00:00.")) # System Notification
    print (classify_with_regex("Backup (started|ended) at .*")) # System Notification
    print (classify_with_regex("System updated to version 1.0.")) # System Notification
    print (classify_with_regex("File report.pdf uploaded successfully by user User123.")) # System Notification
    print (classify_with_regex("Disk cleanup completed successfully.")) # System Notification
    print (classify_with_regex("System reboot initiated by user Admin.")) # System Notification
    print (classify_with_regex("Account with ID 123 created by Admin.")) # User Action
    print (classify_with_regex("Chill bruh.")) # User Action
    
    