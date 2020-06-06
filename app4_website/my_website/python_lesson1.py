def score_to_rating_string(avg_score):

    if avg_score < 1:
        rating = "Terrible. Your score is:"
    elif avg_score < 2:
        rating = "Bad"
    elif avg_score < 3:
        rating = "OK"
    elif avg_score < 4:
        rating = "Good"
    else:
        rating = "Excellent"
    return rating


def sum_of_middle_three(score1, score2, score3, score4, score5):

    max_num = max(score1, score2, score3, score4, score5)
    min_num = min(score1, score2, score3, score4, score5)
    sum_all = score1 + score2 + score3 + score4 + score5
    return sum_all - max_num - min_num


def convert_to_numeric(score):

    return float(score)


"""def score_to_rating_string(score):

    return str(score)"""


def scores_to_rating(score1, score2, score3, score4, score5):
    """
    Turns five scores into a rating by averaging the
    middle three of the five scores and assigning this average
    to a written rating.
    """
    # STEP 1 convert scores to numbers
    score1 = convert_to_numeric(score1)
    score2 = convert_to_numeric(score2)
    score3 = convert_to_numeric(score3)
    score4 = convert_to_numeric(score4)
    score5 = convert_to_numeric(score5)

    # STEP 2 and STEP 3 find the average of the middle three scores
    average_score = sum_of_middle_three(score1, score2, score3, score4, score5)/3

    # STEP 4 turn average score into a rating
    rating = score_to_rating_string(average_score)

    return rating


score_1 = input("Enter score 1:")
score_2 = input("Enter score 2:")
score_3 = input("Enter score 3:")
score_4 = input("Enter score 4:")
score_5 = input("Enter score 5:")

print(scores_to_rating(score_1, score_2, score_3, score_4, score_5))
