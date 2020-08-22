"""Functions."""

import csv
import pyinputplus as pyip
from datetime import date
from statistics import mean

FILE = "dates_scores.csv"


def average(scores):
    """Return the average value of a list of numbers."""
    return mean(scores)


def convert_values_to_list(DATES_AND_SCORES):
    """Return a list of a dictionary's values."""
    return list(DATES_AND_SCORES.values())


def get_todays_date_string():
    """Get today's date in YYYY-MM-DD format."""
    return str(date.today())


def import_scores(FILE):
    """Import dates and scores and dictionary keys and values."""
    DCT = {}

    with open(FILE, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            DCT[row["date"]] = float(row["score"])

    return DCT


def merge_dictionaries(DCT1, DCT2):
    """Merge dictionaries."""
    return {**DCT1, **DCT2}


def write_scores_to_csv(FILE, DCT):
    """Write dictionary to csv."""
    with open(FILE, "w") as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(["date","score"])
        for date_str, score in DCT.items():
            out_csv.writerow([date_str, score])


def update_user(FILE):
    """Update the user."""
    print(f'\n"{FILE}" exported successfully\n')


def prompt_user_for_score():
    """Prompt user for today's score."""
    return pyip.inputNum("\nEnter current score.\n> ")


def calculate_delta(todays_score, most_recent_score):
    """Subtract the previous score from today's score."""
    return todays_score - most_recent_score


def print_score_and_delta(delta):
    """Print the tNPS and delta."""
    if delta == 0:
        print(f"delta: no change")
    elif delta > 0:
        print(f"delta: +{round(delta, 2)}")
    else:
        print(f"delta: {round(delta, 2)}")
