NUMBER_NAMES = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred'
}
BASE = {1: 'thousand', 2: 'million', 3: 'billion'}

def say(number):
    if not -1 < number < 1_000_000_000_000: raise ValueError("input out of range")
    if number < 21: return NUMBER_NAMES[number]
    int_groups = list(map(int, f"{number:,}".split(",")))
    n = len(int_groups) - 1
    num_list = [None] * (n + 1)
    for idx, num in enumerate(int_groups): num_list[idx] = [num, BASE[n - idx]] if BASE.get(n - idx, False) else [num]
    for idx, num in enumerate(num_list):
        if num[0]:
            huns = NUMBER_NAMES[num[0] // 100] + " hundred" if not num[0] % 100 == num[0] else None
            num[0] %= 100
            tens = NUMBER_NAMES[num[0]] if NUMBER_NAMES.get(num[0], False) and num[0] else NUMBER_NAMES[(num[0] // 10) * 10] + "-" + NUMBER_NAMES[num[0] % 10] if num[0] else None
            num[0] = huns + " " + tens if huns and tens else tens if tens else huns 
            num = num[0] + num[1] if not idx == n else num[0]
    return " ".join([" ".join(name) for name in num_list if name[0]])
