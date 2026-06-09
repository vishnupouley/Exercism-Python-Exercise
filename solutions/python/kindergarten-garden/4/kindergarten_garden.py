""" Program to determine which plants belong to each student """
PLANTS = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}
STUDENTS = ("Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry")

class Garden:
    """ Class to find the plants selected by the students """
    
    def __init__(self, diagram, students = None):
        students = STUDENTS if not students else sorted(students)
        first_row, second_row = diagram.split("\n")
        self._plants = {students[index//2]: [PLANTS[first_row[index]], PLANTS[first_row[index+1]], PLANTS[second_row[index]], PLANTS[second_row[index+1]]] for index in range(0, len(first_row), 2)}

    def plants(self, student_name):
        """Return the plants for a specific student"""
        return self._plants[student_name]

    def all_students(self):
        """Return all student names"""
        return list(self._plants.keys())

    def __getitem__(self, student_name):
        """Allow garden[student_name] syntax"""
        return self.plants(student_name)