class Garden:
    """ Class to find the plants selected by the students """
    PLANTS = {"G": "Grass", "C": "Clover", "R": "Radishes", "V": "Violets"}
    STUDENTS = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]
    
    def __init__(self, diagram, students = []):
        self.selected_plants = {}
        students = self.STUDENTS if not students else sorted(students)
        first_row, second_row = diagram.split("\n")
        self.selected_plants = {students[i//2]: [self.PLANTS[first_row[i]], self.PLANTS[first_row[i+1]], self.PLANTS[second_row[i]], self.PLANTS[second_row[i+1]]] for i in range(0, len(first_row), 2)}

    def plants(self, student_name):
        return self.selected_plants[student_name]