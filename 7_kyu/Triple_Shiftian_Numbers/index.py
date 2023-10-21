def triple_shiftian(base, n):
    if n > 2:
        el = 3
        while el != n+1:
            res_triple_shiftian = 4*base[el - 1] - 5*base[el - 2] + 3*base[el - 3]
            base.append(res_triple_shiftian)
            el += 1
        return base[-1]

    else:
        return base[n]
