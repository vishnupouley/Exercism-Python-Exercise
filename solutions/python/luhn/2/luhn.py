class Luhn:
    def __init__(self, card_num: str):
        self.card_num = card_num.replace(" ", "")
    def valid(self) -> bool:
        if len(self.card_num) > 1 and self.card_num.isdigit():
            luhn_list = list(map(int, list(self.card_num)))[::-1]
            for index, luhn in enumerate(luhn_list):
                double = luhn_list[index] * 2 if index % 2 else luhn_list[index]
                luhn_list[index] = double if double < 10 else double - 9
            return not sum(luhn_list) % 10
        return False