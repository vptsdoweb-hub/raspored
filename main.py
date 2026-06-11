import csv
import time
import os
from datetime import datetime

os.system("git pull origin main")

FILENAME = "raspored/schedule.csv"
DELAY_SECONDS = 4

def clear_screen():
    os.system("clear")  # For Linux/macOS; use 'cls' on Windows if needed

def load_schedule(filename):
    with open(filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [row for row in reader]

def get_today_schedule(schedule):
    today = datetime.today().strftime('%Y-%m-%d')
    today_classes = [cls for cls in schedule if cls['date'] == today]
    today_classes.sort(key=lambda x: x['time'])
    return today_classes

def display_schedule_one_by_one(classes):
    print(f"\nRaspored za {datetime.today().strftime('%d.%m.%Y')}\n")
    for cls in classes:
        print(f"{cls['time']} - [{cls['type']}] {cls['name']} ({cls['room']})")
        time.sleep(DELAY_SECONDS)


while True:
    clear_screen()
    schedule = load_schedule(FILENAME)
    today_schedule = get_today_schedule(schedule)
    if today_schedule:
        display_schedule_one_by_one(today_schedule)
    else:
        print("Nema planiranih predavanja i/ili ispita.")
        time.sleep(5)
    clear_screen()

