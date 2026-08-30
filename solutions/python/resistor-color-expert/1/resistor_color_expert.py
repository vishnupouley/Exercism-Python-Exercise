BAND = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
OHMS = {1: 'ohms', 2: 'ohms', 3: 'ohms', 4: 'kiloohms', 5: 'kiloohms', 6: 'kiloohms', 7: 'megaohms', 8: 'megaohms' , 9: 'megaohms', 10: 'gigaohms', 11: 'gigaohms', 12: 'gigaohms'}
METRICS = {'ohms': 0, 'kiloohms': 3, 'megaohms': 6, 'gigaohms': 9}
TOLERANCE = {"grey": "±0.05%", "violet": "±0.1%", "blue": "±0.25%", "green": "±0.5%", "brown": "±1%", "red": "±2%", "gold": "±5%", "silver": "±10%"}


def resistor_label(colors):
    if len(colors) == 1: return f"{BAND[colors[0]]} ohms"
    elif len(colors) == 4: ohms = (BAND[colors[0]]*10 + BAND[colors[1]]) * 10**BAND[colors[2]]
    else: ohms = (BAND[colors[0]]*100 + BAND[colors[1]]*10 + BAND[colors[2]]) * 10**BAND[colors[3]]
    ohm = ohms / 10**METRICS[OHMS[len(str(ohms))]] if ohms % 10**METRICS[OHMS[len(str(ohms))]] else ohms // 10**METRICS[OHMS[len(str(ohms))]]
    return f"{ohm} {OHMS[len(str(ohms))]} {TOLERANCE[colors[-1]]}"