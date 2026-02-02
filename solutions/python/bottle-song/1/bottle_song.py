NUMBERS = ['no', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']

def recite(start, take=1):
    BOTTLE_SONG = []
    for index in range(start, start-take, -1):
        if not index == 1:
            BOTTLE_SONG.extend([
                f"{NUMBERS[index]} green bottles hanging on the wall,",
                f"{NUMBERS[index]} green bottles hanging on the wall,",
                "And if one green bottle should accidentally fall,",
                f"There'll be {NUMBERS[index-1].lower()} green bottles hanging on the wall.",
            ])
        else:
            BOTTLE_SONG.extend([
                "One green bottle hanging on the wall,",
                "One green bottle hanging on the wall,",
                "And if one green bottle should accidentally fall,",
                "There'll be no green bottles hanging on the wall.",
            ])
        if index == 2:
            BOTTLE_SONG[-1] = "There'll be one green bottle hanging on the wall."
        if not index - 1 == start-take:
            BOTTLE_SONG.append("")
    return BOTTLE_SONG