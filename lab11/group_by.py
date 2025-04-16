def group_by(f, target_list):
    result = {}
    for item in target_list:
        key = f(item)
        result.setdefault(key, []).append(item)
    return result