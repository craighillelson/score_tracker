"""Compile daily post."""

from functions import (DATES_SCORES_CSV,
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

TODAY_STR = get_todays_date_string()
print(f"\n{TODAY_STR}")
todays_score = (prompt_user_for_score())

PREVIOUS_SCORES = import_scores(DATES_SCORES_CSV)
score_values = convert_values_to_list(PREVIOUS_SCORES)
most_recent_score = float(score_values[-1])
delta = calculate_delta(todays_score, most_recent_score)

SCORE_TODAY = {}
SCORE_TODAY[TODAY_STR] = float(todays_score)
SCORES_MERGED = merge_dictionaries(SCORE_TODAY, PREVIOUS_SCORES)

print(f"\ndate: {TODAY_STR}")
print(f"current score: {todays_score}")
print(f"most recent score: {most_recent_score}")
print_score_and_delta(delta)
MERGED_VALUES = convert_values_to_list(SCORES_MERGED)
print(f"average: {round(average(MERGED_VALUES), 2)}")

write_scores_to_csv(DATES_SCORES_CSV, SCORES_MERGED)
update_user(DATES_SCORES_CSV)
