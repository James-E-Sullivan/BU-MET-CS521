"""
10.1 (Assign grades)
Write a program that reads a list of scores and then assigns grades based on
the following scheme:

A if score >= best - 10
B if score >= best - 20
C if score >= best - 30
D if score >= best - 40
F otherwise
"""


def grade_score(student_score, max_score):
    """
    Assigns a grade based on a student's score and the maximum score
    :param student_score: The student score(int or float)
    :param max_score: The maximum score (int or float)
    :return:
    """

    if student_score >= max_score - 10:
        student_grade = 'A'
    elif student_score >= max_score - 20:
        student_grade = 'B'
    elif student_score >= max_score - 30:
        student_grade = 'C'
    elif student_score >= max_score - 40:
        student_grade = 'D'
    else:
        student_grade = 'F'

    return student_grade


def find_best_score(input_scores):
    """
    Evaluates user input scores and returns the greatest score
    :param input_scores: List of scores (integers)
    :return best_score: Returns greatest score in the list
    """

    # Starts best score at 0. Assumes no negative scores are possible.
    best_score = 0

    # Iterates through scores and updates best_score if a better score found
    for student_score in input_scores:
        new_score = student_score

        if new_score > best_score:
            best_score = new_score

    return best_score


while True:
    try:
        score_list = [int(input_score) for input_score in input(
            'Enter scores (integers separated by spaces): ').split()]

        student_number = 0

        for score in score_list:
            grade = grade_score(score, find_best_score(score_list))
            print('Student', student_number, 'score is', score, 'and grade is', grade)
            student_number += 1

        break

    # User prompted again if they enter invalid input
    except ValueError:
        print("Could not convert input to integer. Please try again.")
