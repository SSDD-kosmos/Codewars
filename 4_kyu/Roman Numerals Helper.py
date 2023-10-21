# https://www.codewars.com/kata/51b66044bce5799a7f000003/train/python

class RomanNumerals:
    sym = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    @staticmethod
    def to_roman(val: int) -> str:
        result = ''
        counter = 0

        while val:
            div = val // RomanNumerals.num[counter]
            val %= RomanNumerals.num[counter]
            while div:
                result += RomanNumerals.sym[counter]
                div -= 1
            counter += 1
        return result

    @staticmethod
    def from_roman(roman_num: str) -> int:
        result = 0
        for ind, value in enumerate(roman_num):
            first_num = RomanNumerals.num[RomanNumerals.sym.index(value)]
            second_num = RomanNumerals.num[RomanNumerals.sym.index(roman_num[ind + 1]) if ind + 1 != len(
                roman_num) else -1]
            if first_num >= second_num:
                result += first_num
            else:
                result -= first_num
        return result
