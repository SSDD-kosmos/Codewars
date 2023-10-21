def number_group():
    n = 1000000000
    group_by_commas(n)


def group_by_commas(n):
    formatted_number = f'{n:,}'
    return formatted_number


number_group()
