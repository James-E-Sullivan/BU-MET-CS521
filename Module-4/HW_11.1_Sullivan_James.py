"""
HW 11.1
(Sum elements column by column)
Write a function that returns the sum of all the elements in a specified column
in a matrix using the following header:

def sumColumn(m, columnIndex):

Write a test program that reads a 3x4 matrix and displays the sum of each
column. Here is a sample run:

Enter a 3-by-4 matrix row for row 0: 1.5 2 3 4
Enter a 3-by-4 matrix row for row 1: 5.5 6 7 8
Enter a 3-by-4 matrix row for row 2: 9.5 1 3 1
Sum of the elements for column 0 is 16.5
"""


def test_sumColumn():
    """
    Function that tests sumColumn with a 3x4 matrix.
    User inputs 3 rows of 4 columns, which are appended to a matrix.
    sumColumn prints the sum of each row.

    Row and column is currently hard-coded into the function by design, but this
    can be changed.
    """

    def get_matrix_row(row):
        """
        User inputs 4 numbers, which are converted to float and added to a list.
        :param row: The row of the matrix the user is creating.
        :return row_values: A list of float values.
        """
        while True:

            try:
                row_values = [
                    float(input_int) for input_int in input(
                        'Enter a 3-by-4 matrix row for row ' +
                        str(row) + ': ').split()]

                if len(row_values) is not 4:
                    print('You did not enter four numbers.')
                    row_values = get_matrix_row(row)

                break

            except ValueError:
                print('Not a valid input.')

        return row_values

    # test_matrix initialized as blank list
    test_matrix = []

    # Appends 3 rows of user input values to test_matrix
    for row_number in range(0, 3):

        matrix_row = get_matrix_row(row_number)
        test_matrix.append(matrix_row)

    # Loops through columns in test_matrix, prints sum of each column
    for column_number in range(0, 4):

        sumColumn(test_matrix, column_number)


def sumColumn(m, columnIndex):

    column_sum = 0
    for row in range(len(m)):
        column_sum += m[row][columnIndex]

    print('Sum of the elements for column', columnIndex, 'is', column_sum)


test_sumColumn()
