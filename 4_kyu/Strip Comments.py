# https://www.codewars.com/kata/51c8e37cee245da6b40000bd

def strip_comments(string, markers):
    s_list = string.split("\n")
    n_list = []

    for item in s_list:
        s = ""
        for char in item:
            if char in markers:
                break
            else:
                s = s + char
        n_list.append(s.strip())
    print("\n".join(n_list))
    return "\n".join(n_list)


# Second variation
def solution(string, markers):
    lines = string.split('\n')
    for i, line in enumerate(lines):
        for marker in markers:
            index = line.find(marker)
            if index != -1:
                line = line[:index]
        lines[i] = line.rstrip(' ')
    return '\n'.join(lines)


strip_comments('\tlemons\nbananas\n=\n? - ?',
               ['!', '^', '=', '-', '?', '#', "'", ','])
