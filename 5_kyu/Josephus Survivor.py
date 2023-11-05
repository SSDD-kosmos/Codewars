# https://www.codewars.com/kata/555624b601231dc7a400017a/train/python

def josephus_survivor(n, k):
    josep = list(range(1, n + 1))
    counter = (k - 1)
    while len(josep) > 1:
        while counter >= len(josep):
            counter = counter - len(josep)
        del josep[counter % n]
        counter += k - 1
    return josep[0]


josephus_survivor(7, 3)
