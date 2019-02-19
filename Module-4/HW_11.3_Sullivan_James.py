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
    ordered_scores = []

    # Grade all answers
    for i in range(len(answers)):
        # Grade one student
        correctCount = 0
        for j in range(len(answers[i])):
            if answers[i][j] == keys[j]:
                correctCount += 1

        # Append student scores to a list
        student_scores.append([i, correctCount])

    # Initialize a list of ordered scores, starting with first student's score
    ordered_scores.append(student_scores[0])

    # Append/insert scores into ordered scores, in descending order
    # Keeps original Student # and score together
    for i in range(1, len(student_scores)):

        for j in range(len(ordered_scores)):

            # Inserts score to ahead of value if it is greater
            if student_scores[i][1] > ordered_scores[j][1]:
                ordered_scores.insert(j, student_scores[i])
                break

            # Appends score to end of list if it <= all other values
            elif (j + 1) is len(ordered_scores):
                ordered_scores.append(student_scores[i])

    # Iterates through ordered_scores, prints student # and score
    for i in range(len(ordered_scores)):

        print("Student", str(ordered_scores[i][0]) + "'s correct count is",
              ordered_scores[i][1])


main()  # Call the main function
