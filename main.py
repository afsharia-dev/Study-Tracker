import datetime
import csv
import pathlib


# ask user for subject
def study_subject():
    return input("What subject did you study? ")


# ask user for study time
def time_studied():
    while True:
        try:
            minutes = int(input("How many minutes? "))
            if minutes <= 0:
                raise ValueError
            return minutes
        except ValueError:
            print("Enter Valid Minutes")


# get today's date
def todays_date():
    return datetime.date.today()


# Today's total
def todays_total(reader):
    total = 0
    next(reader, None)
    today = str(todays_date())
    for row in reader:
        if row[0] == today:
            total += int(row[2])
    return total


# save to csv
def main():
    path = pathlib.Path("data/study_log.csv")
    path.parent.mkdir(exist_ok=True)

    if not path.exists():
        with open(path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Subject", "Time"])

    subject = study_subject()
    minutes = time_studied()

    with open(path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([todays_date(), subject, minutes])
    print("Session Saved")

    with open(path, "r", newline="") as file:
        reader = csv.reader(file)
        total = todays_total(reader)
        print(f"Today's Total: {total} Minutes")


if __name__ == "__main__":
    main()
