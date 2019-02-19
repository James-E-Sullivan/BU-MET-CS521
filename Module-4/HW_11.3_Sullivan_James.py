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

    # Grade all answers
    for i in range(len(answers)):
        # Grade one student
        correctCount = 0
        for j in range(len(answers[i])):
            if answers[i][j] == keys[j]:
                correctCount += 1

        # Append student scores to a list
        student_scores.append([correctCount, i])

    # Sorts score/student pairs based on first value (score), descending order
    student_scores.sort(reverse=True)

    # Prints student number and score values
    for i in range(len(student_scores)):
        print("Student", str(student_scores[i][1]) + "'s correct count is",
              student_scores[i][0])



main()  # Call the main function
