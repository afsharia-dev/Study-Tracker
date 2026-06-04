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


# save to cvs
def main():
    path = pathlib.Path("data/study_log.csv")

    if not path.exists():
        with open(path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Subject", "Time"])

    subject = study_subject()
    minutes = time_studied()

    if minutes is None:
        print("Invalid minutes")
        return

    with open(path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([todays_date(), subject, minutes])


if __name__ == "__main__":
    main()
