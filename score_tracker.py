"""Compile daily post."""

from functions import (FILE,
                       average,
                       convert_values_to_list,
                       get_todays_date_string,
                       prompt_user_for_score,
                       import_scores,
                       print_score_and_delta,
                       calculate_delta,
                       merge_dictionaries,
                       write_scores_to_csv,
                       update_user)

today_str = get_todays_date_string()
print(f"\n{today_str}")
todays_score = (prompt_user_for_score())

PREVIOUS_SCORES = import_scores(FILE)
score_values = convert_values_to_list(PREVIOUS_SCORES)
most_recent_score = float(score_values[-1])
delta = calculate_delta(todays_score, most_recent_score)

SCORE_TODAY = {}
SCORE_TODAY[today_str] = float(todays_score)
SCORES_MERGED = merge_dictionaries(SCORE_TODAY, PREVIOUS_SCORES)

print(f"\ndate: {today_str}")
print(f"current score: {todays_score}")
print(f"most recent score: {most_recent_score}")
print_score_and_delta(delta)
MERGED_VALUES = convert_values_to_list(SCORES_MERGED)
print(f"average: {round(average(MERGED_VALUES), 2)}")

write_scores_to_csv(FILE, SCORES_MERGED)
update_user(FILE)
