#make set
def make_set(data):
    if data is None:
        return []
    unique_elements = []
    for item in data:
        if item not in unique_elements:
            unique_elements.append(item)
    return unique_elements

#check if is set
def is_set(data):
    if data is None:
        return False
    seen = []
    for item in data:
        if item in seen:
            return False
        seen.append(item)
    return True

#union
def union(setA, setB):
    if not is_set(setA) or not is_set(setB):
        return []
    result = make_set(setA + setB)
    return result

#intersection
def intersection(setA, setB):
    if not is_set(setA) or not is_set(setB):
        return []
    result = []
    for item in setA:
        if item in setB and item not in result:
            result.append(item)
    return result