class Allergies:
    ALLERGIES = {128: "cats", 64: "pollen", 32: "chocolate", 16: "tomatoes", 8: "strawberries", 4: "shellfish", 2: "peanuts", 1: "eggs"}

    def __init__(self, score):
        self.allergies_list = list()
        while score:
            for i in range(10):
                if score == 2**i:
                    pow = 2**(i)
                    if self.ALLERGIES.get(pow, False):
                        self.allergies_list.append(self.ALLERGIES.get(pow))
                    score -= pow
                    break
                elif score < 2**i:
                    pow = 2**(i-1)
                    if self.ALLERGIES.get(pow, False):
                        self.allergies_list.append(self.ALLERGIES.get(pow))
                    score -= pow
                    break

    def allergic_to(self, item):
        return True if self.allergies_list.count(item) else False

    @property
    def lst(self):
        return self.allergies_list
