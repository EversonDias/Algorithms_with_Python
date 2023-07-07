def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def is_anagram(first_string, second_string):
    first_string_order = ''.join(merge_sort(first_string.lower()))
    second_string_order = ''.join(merge_sort(second_string.lower()))

    string_equal = first_string_order != second_string_order
    string_empty = not first_string_order and not second_string_order
    if string_equal or string_empty:
        return first_string_order, second_string_order, False
    return first_string_order, second_string_order, True
