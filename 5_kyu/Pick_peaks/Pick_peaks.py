def pick_peaks(arr):
    pos = []
    peaks = []
    arr.append(10000)
    for i in range(1, len(arr) - 2):
        counter = 1
        while arr[i] == arr[i + counter]:
            counter += 1
        if arr[i - 1] < arr[i] > arr[i + counter]:
            peaks.append(arr[i])
            pos.append(i)

    print({
        'pos': pos,
        'peaks': peaks
    })
    return {
        'pos': pos,
        'peaks': peaks
    }


pick_peaks([1, 2, 5, 4, 3, 2, 3, 6, 4, 1, 2, 3, 3, 4, 5, 3, 2, 1, 2, 3, 5, 5, 4, 4])
