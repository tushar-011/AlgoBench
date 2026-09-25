def bubble_sort(data):
    data = data.copy()

    n = len(data)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = (
                    data[j + 1],
                    data[j]
                )

                swapped = True

        if not swapped:
            break

    return data


def insertion_sort(data):
    data = data.copy()

    for i in range(1, len(data)):

        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:

            data[j + 1] = data[j]

            j -= 1

        data[j + 1] = key

    return data


def merge_sort(data):
    if len(data) <= 1:
        return data

    middle = len(data) // 2

    left = merge_sort(
        data[:middle]
    )

    right = merge_sort(
        data[middle:]
    )

    return merge(
        left,
        right
    )


def merge(left, right):
    result = []

    i = 0
    j = 0

    while (
        i < len(left)
        and
        j < len(right)
    ):

        if left[i] <= right[j]:

            result.append(
                left[i]
            )

            i += 1

        else:

            result.append(
                right[j]
            )

            j += 1

    result.extend(
        left[i:]
    )

    result.extend(
        right[j:]
    )

    return result


def quick_sort(data):

    if len(data) <= 1:
        return data

    pivot = data[
        len(data) // 2
    ]

    left = [
        item
        for item in data
        if item < pivot
    ]

    middle = [
        item
        for item in data
        if item == pivot
    ]

    right = [
        item
        for item in data
        if item > pivot
    ]

    return (
        quick_sort(left)
        + middle
        + quick_sort(right)
    )