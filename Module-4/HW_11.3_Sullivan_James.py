"""
HW 11.3
(Sort students by grades)
Rewrite Listing 11.2, GradeExam.py, to display the students in increasing
order of the number of correct answers.
"""


def main():
    # Students' answers to the questions
    answers = [
        ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
        ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
        ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
        ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']]

    # Key to the questions
    keys = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']

    student_scores = []
    student_dict = {}
    ordered_scores = []

    # Grade all answers
    for i in range(len(answers)):
        # Grade one student
        correctCount = 0
        for j in range(len(answers[i])):
            if answers[i][j] == keys[j]:
                correctCount += 1

        student_scores.append([i, correctCount])
        student_dict[i] = correctCount

        print("Student", i, "'s correct count is", correctCount)



    print(student_scores)
    print(student_dict)
    """
    ordered_scores = [(k, student_dict[k]) for k in sorted(
        student_dict, key=student_dict.get, reverse=True)]
    print(ordered_scores)
    """
    for i in range(len(student_scores)):
        print(student_scores[i][1])





    ordered_scores = [(k, student_scores[k]) for k in sorted(student_scores, reverse=True)]

    def selection_sort(score_list):

        start_point = 0
        for students in score_list:
            students[1]

        for start_point in range(0, len(score_list)):



            min_value_index = score_list.index



main()  # Call the main function
