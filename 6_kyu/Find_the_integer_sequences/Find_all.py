def find_sequences(n):
    result_list = []

    for el in range(1, n // 2 + 1):
        i = el
        res_sum = 0
        while res_sum < n:
            res_sum += i
            i += 1
            if res_sum == n:
                result_list.append(list(range(el, i)))

    result_list.reverse()
    print(result_list)
    return result_list


find_sequences(15)
