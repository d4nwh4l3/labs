def zipmap(key_list, value_list, override=False):
    if not override and len(set(key_list)) != len(key_list):
        return {}

    if len(key_list) > len(value_list):
        value_list += [None] * (len(key_list) - len(value_list))

    pairs = list(map(lambda kv: (kv[0], kv[1]), zip(key_list, value_list)))
    return dict(pairs)