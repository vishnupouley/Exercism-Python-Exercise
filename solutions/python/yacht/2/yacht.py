from collections import Counter

# Score categories.
# Change the values as you see fit.
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11
YACHT = 12


def score(dice: list, category: int) -> int:
    unique_dice = list(set(dice))
    match category:
        case 1 | 2 | 3 | 4 | 5 | 6:
            return dice.count(category) * category
        case 7:
            if len(unique_dice) == 2:
                if dice.count(unique_dice[0]) in [2, 3] and dice.count(unique_dice[0]) in [2, 3]:
                    return sum(dice)
            return 0
        case 8:
            if len(unique_dice) in [1, 2]:
                number, count = Counter(dice).most_common(1)[0]
                if count >= 4:
                    return number * 4
            return 0
        case 9:
            if sorted(dice) == [1, 2, 3, 4, 5]:
                return 30
            return 0
        case 10:
            if sorted(dice) == [2, 3, 4, 5, 6]:
                return 30
            return 0
        case 11:
            return sum(dice)
        case 12:
            if len(unique_dice) == 1:
                return 50
            return 0
        case _:
            return 0