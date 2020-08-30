"""Compile daily post."""

from functions import (DATES_SCORES_CSV,
                       average,
                       calculate_delta,
                       convert_values_to_list,
                       find_min_max,
                       get_todays_date_string,
                       import_scores,
                       merge_dictionaries,
                       output_result,
                       print_high_or_low_scores,
                       prompt_user_for_score,
                       prompt_user_for_target,
                       update_user,
                       write_scores_to_csv)

PREVIOUS_SCORES = import_scores(DATES_SCORES_CSV)
TODAY_STR = get_todays_date_string()

if PREVIOUS_SCORES:
    score_values = convert_values_to_list(PREVIOUS_SCORES)
else:
    print("\nno previous scores")

target_score = prompt_user_for_target()
todays_score = prompt_user_for_score()
SCORE_TODAY = {}
SCORE_TODAY[TODAY_STR] = float(todays_score)
SCORES_MERGED = merge_dictionaries(SCORE_TODAY, PREVIOUS_SCORES)
delta_from_target = calculate_delta(todays_score, target_score)

print(f"\ndate: {TODAY_STR}")
print(f"\ntarget: {target_score}")
print(f"current score: {todays_score}")
output_result("delta from target:", delta_from_target)

if len(SCORES_MERGED) > 1:
    most_recent_score = score_values[0]
    print(f"most recent score: {most_recent_score}")
    delta_from_previous_score = calculate_delta(todays_score, most_recent_score)
    output_result("delta from previous score:", delta_from_previous_score)
    MERGED_VALUES = convert_values_to_list(SCORES_MERGED)
    print(f"average: {round(average(MERGED_VALUES), 2)}")
else:
    pass

key_min = find_min_max(min, SCORES_MERGED)
key_max = find_min_max(max, SCORES_MERGED)
print_high_or_low_scores("low score:", SCORES_MERGED, key_min)
print_high_or_low_scores("high score:", SCORES_MERGED, key_max)

write_scores_to_csv(DATES_SCORES_CSV, SCORES_MERGED)
update_user(DATES_SCORES_CSV)
