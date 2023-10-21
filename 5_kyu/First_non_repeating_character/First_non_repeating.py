def first_non_repeating_letter(s):
    result = [x for x in s if s.lower().count(x.lower()) == 1]
    return result[0] if result else ''


first_non_repeating_letter('aaAs')
