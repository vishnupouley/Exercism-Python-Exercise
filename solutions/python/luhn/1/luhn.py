class Luhn:
    def __init__(self, card_num: str):
        self.card_num = card_num
    def valid(self) -> bool:
        luhn_num = self.card_num.replace(" ", "")
        if len(luhn_num) > 1 and luhn_num.isdigit():
            luhn_list = list(map(int, list(luhn_num)))[::-1]
            for index, luhn in enumerate(luhn_list):
                double = luhn_list[index] * 2 if index % 2 else luhn_list[index]
                luhn_list[index] = double if double < 10 else double - 9
            return True if not sum(luhn_list) % 10 else False
        return False