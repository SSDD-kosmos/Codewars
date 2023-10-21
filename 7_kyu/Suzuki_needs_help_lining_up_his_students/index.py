def std():
    string = 'Tadashi Takahiro Takao Takashi Takayuki Takehiko Takeo Takeshi Takeshi'

    lineup_students(string)


def lineup_students(string):
    students = string.split()
    students.sort()
    result = sorted(students, key=len)
    print(result[::-1])
    return result[::-1]


std()
