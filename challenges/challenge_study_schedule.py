def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    count = 0
    for period in permanence_period:
        if type(period[0]) != int or type(period[1]) != int:
            return None
        if target_time >= period[0] and target_time <= period[1]:
            count += 1
    return count
    raise NotImplementedError
