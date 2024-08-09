def create_strings_from_characters(frequencies, string1, string2):
    can_create_string1 = can_create_frm_freq(frequencies, string1)
    can_create_string2 = can_create_frm_freq(frequencies, string2)

    if (not can_create_string1) or (not can_create_string2):
        if can_create_string1 or can_create_string2:
            return 1

        return 0
    # Write your code here.
    for ch in string1 + string2:
        if ch not in frequencies or frequencies[ch] == 0:
            return 1

        frequencies[ch] -= 1

    return 2


def can_create_frm_freq(frequencies, string):
    for ch in set(string):
        if string.count(ch) > frequencies.get(ch,0):
            return False

    return True
