def find_duplicate(nums):
    if not nums or len(nums) < 2:
        return False

    count = {}

    for number in nums:
        if type(number) == str or number < 0:
            return False

        if number in count:
            return number
        else:
            count[number] = 1

    return False
