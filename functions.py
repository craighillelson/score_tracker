"""Functions."""

from datetime import date
from statistics import mean
import csv
import pyinputplus as pyip

DATES_SCORES_CSV = "dates_scores.csv"


def average(scores):
    """Return the average value of a list of numbers."""
    return mean(scores)


def calculate_delta(score_1, score_2):
    """Subtract the previous score from today's score."""
    return round((score_1 - score_2), 2)


def convert_values_to_list(dates_and_scores):
    """Return a list of a dictionary's values."""
    return list(dates_and_scores.values())


def find_min_max(min_or_max, lst):
    """Find high or low score."""
    return min_or_max(lst)


def get_todays_date_string():
    """Get today's date in YYYY-MM-DD format."""
    return str(date.today())


def import_scores(file_name):
    """Import dates and scores and dictionary keys and values."""
    dct_1 = {}

    with open(file_name, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            dct_1[row["date"]] = float(row["score"])

    return dct_1


def merge_dictionaries(dct_1, dct_2):
    """Merge dictionaries."""
    return {**dct_1, **dct_2}


def output_result(delta_str, delta):
    """Format result."""
    print(delta_str, end=" ")
    if delta > 0:
        print(f"+{delta}")
    else:
        print(delta)


def print_high_or_low_scores(label, dct, score):
    """Output high or low score."""
    print(label, dct[score])


def prompt_user_for_score():
    """Prompt user for today's score."""
    return pyip.inputNum("\nEnter current score.\n> ")


def prompt_user_for_target():
    """Prompt the user for the target score."""
    return pyip.inputNum("\nEnter the target score.\n> ")


def update_user(file_name):
    """Update the user."""
    print(f'\n"{file_name}" exported successfully\n')


def write_scores_to_csv(file_name, dct_1):
    """Write dictionary to csv."""
    with open(file_name, "w") as out_file:
        out_csv = csv.writer(out_file)
        out_csv.writerow(["date", "score"])
        for date_str, score in dct_1.items():
            out_csv.writerow([date_str, score])
