# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

# Не решено

def sum_of_intervals(intervals):
    output = set([])
    for interval in intervals:
        output.update(range(interval[0], interval[1]))
    return len(output)


sum_of_intervals([(1, 5), (6, 10)])
