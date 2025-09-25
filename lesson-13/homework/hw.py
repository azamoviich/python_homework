import re
import time
from datetime import datetime, date, timedelta
import pytz

###########
# Homework 1 (Age Calculator)
###########
def calculate_age(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    today = date.today()

    years = today.year - birthdate.year
    months = today.month - birthdate.month
    days = today.day - birthdate.day

    if days < 0:
        months -= 1
        days += (date(today.year, today.month, 1) - timedelta(days=1)).day
    if months < 0:
        years -= 1
        months += 12

    print(f"Age: {years} years, {months} months, {days} days")

# Example
# calculate_age("2005-09-25")


###########
# Homework 2 (Days Until Next Birthday)
###########
def days_until_birthday(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
    today = date.today()
    next_birthday = date(today.year, birthdate.month, birthdate.day)

    if next_birthday < today:
        next_birthday = date(today.year + 1, birthdate.month, birthdate.day)

    remaining = (next_birthday - today).days
    print(f"Days until next birthday: {remaining}")

# Example
# days_until_birthday("2005-09-25")


###########
# Homework 3 (Meeting Scheduler)
###########
def meeting_scheduler(current_str, duration_h, duration_m):
    current = datetime.strptime(current_str, "%Y-%m-%d %H:%M")
    end_time = current + timedelta(hours=duration_h, minutes=duration_m)
    print("Meeting ends at:", end_time)

# Example
# meeting_scheduler("2025-09-25 14:00", 2, 30)


###########
# Homework 4 (Timezone Converter)
###########
def timezone_converter(date_str, from_tz, to_tz):
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)

    naive = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
    localized = from_zone.localize(naive)
    converted = localized.astimezone(to_zone)
    print("Converted time:", converted)

# Example
# timezone_converter("2025-09-25 14:00", "Asia/Tashkent", "America/New_York")


###########
# Homework 5 (Countdown Timer)
###########
def countdown(target_str):
    target = datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")
    while True:
        now = datetime.now()
        if now >= target:
            print("Countdown finished!")
            break
        remaining = target - now
        print("Time remaining:", remaining)
        time.sleep(1)

# Example (be careful, runs live countdown)
# countdown("2025-09-25 15:00:00")


###########
# Homework 6 (Email Validator)
###########
def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if re.match(pattern, email):
        print("Valid email")
    else:
        print("Invalid email")

# Example
# validate_email("test@gmail.com")


###########
# Homework 7 (Phone Number Formatter)
###########
def format_phone(number):
    number = re.sub(r"\D", "", number)
    if len(number) == 10:
        formatted = f"({number[:3]}) {number[3:6]}-{number[6:]}"
        print("Formatted:", formatted)
    else:
        print("Invalid phone number")

# Example
# format_phone("1234567890")


###########
# Homework 8 (Password Strength Checker)
###########
def check_password(password):
    if (len(password) >= 8 and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password) and
        re.search(r"[0-9]", password)):
        print("Strong password")
    else:
        print("Weak password")

# Example
# check_password("Test1234")


###########
# Homework 9 (Word Finder)
###########
def find_word(word, text):
    matches = [m.start() for m in re.finditer(rf"\b{word}\b", text)]
    print(f"'{word}' found at positions:", matches)

# Example
# find_word("cat", "The cat sat on the mat with another cat")


###########
# Homework 10 (Date Extractor)
###########
def extract_dates(text):
    pattern = r"\b\d{4}-\d{2}-\d{2}\b"
    dates = re.findall(pattern, text)
    print("Dates found:", dates)

# Example
# extract_dates("Important dates: 2025-09-25, 2024-12-31")
