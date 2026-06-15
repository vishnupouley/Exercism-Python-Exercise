""" Program to give it's rows and columns of a matrix """

class Matrix:
    """ Class to splits the columns and rows of a matrix """

    def __init__(self, matrix_string):
        self.matrix = [[int(number) for number in item.split()] for item in matrix_string.splitlines()]
        self.transpose = list(zip(*self.matrix))

    def row(self, index):
        """ Returns the row of the specified place """
        return self.matrix[index-1]

    def column(self, index):
        """ Returns the column of the specified place """
        return list(self.transpose[index-1])