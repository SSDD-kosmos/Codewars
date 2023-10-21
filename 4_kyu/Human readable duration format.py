# https://www.codewars.com/kata/52742f58faf5485cae000b9a

def format_duration(seconds):
    words = ['years', 'days', 'hours', 'minutes', 'seconds']

    if not seconds:
        return 'now'
    else:
        m, s = divmod(seconds, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        y, d = divmod(d, 365)

        time_readable = [y, d, h, m, s]
        res_str = ''

        for el in time_readable:
            if el > 1:
                res_str += f', {el} {words[time_readable.index(el)]}'
                time_readable[time_readable.index(el)] += 1000000000
            elif el == 1:
                res_str += f', {el} {words[time_readable.index(el)][:-1]}'
                time_readable[time_readable.index(el)] += 1000000000

        if res_str[2:].rfind(',') > 0:
            return res_str[2:res_str.rfind(',')] + ' and' + res_str[res_str.rfind(',')+1:]
        else:
            return res_str[2:]