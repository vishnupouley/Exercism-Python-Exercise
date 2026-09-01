class Allergies:
    """ Class to find their allergies from the score """
    ALLERGIES = {128: "cats", 64: "pollen", 32: "chocolate", 16: "tomatoes", 8: "strawberries", 4: "shellfish", 2: "peanuts", 1: "eggs"}

    def __init__(self, score):
        self.allergies_list = []
        while score:
            for power in range(10):
                if score == 2**power:
                    value = 2**(power)
                    if self.ALLERGIES.get(value, False):
                        self.allergies_list.append(self.ALLERGIES.get(value))
                    score -= value
                    break
                if score < 2**power:
                    value = 2**(power-1)
                    if self.ALLERGIES.get(value, False):
                        self.allergies_list.append(self.ALLERGIES.get(value))
                    score -= value
                    break

    def allergic_to(self, item):
        return item in self.allergies_list

    @property
    def lst(self):
        return self.allergies_list
