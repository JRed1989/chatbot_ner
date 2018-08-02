def structure_es_result(result):
    structured_result = []
    # The list around result.keys() is to make it compatible to python3
    key_list = list(result.keys())
    key_list.sort()
    for value in key_list:
        structured_result.append({'value': value, 'variants': result[value]})
    return structured_result
