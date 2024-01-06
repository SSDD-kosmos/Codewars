# https://www.codewars.com/kata/528d36d7cc451cd7e4000339/train/python

def most_money(students):
    names = []
    totals = []

    for student in students:
        names.append(student.name)
        totals.append(student.fives*5 + student.tens*10 + student.twenties*20)
    maximum = max(totals)
    if maximum*len(totals) == sum(totals) and len(students) > 1:
        return 'all'
    index = totals.index(maximum)
    return names[index]
