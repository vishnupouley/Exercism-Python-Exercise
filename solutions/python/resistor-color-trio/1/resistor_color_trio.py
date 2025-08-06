BAND = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
OHMS = {1: 'ohms', 2: 'ohms', 3: 'ohms', 4: 'kiloohms', 5: 'kiloohms', 6: 'kiloohms', 7: 'megaohms', 8: 'megaohms' , 9: 'megaohms', 10: 'gigaohms', 11: 'gigaohms', 12: 'gigaohms'}
METRICS = {'ohms': 0, 'kiloohms': 3, 'megaohms': 6, 'gigaohms': 9}


def label(colors):
    ohms = (BAND[colors[0]]*10 + BAND[colors[1]]) * 10**BAND[colors[2]]
    return str(ohms // 10**METRICS[OHMS[len(str(ohms))]]) + " " + OHMS[len(str(ohms))]