def get_delimited_slices(string, delimiter):
    first_idx = string.find(delimiter)
    if first_idx < 0 or delimiter not in string:
        return ['', '', string]
    
    first_slice = string[0:first_idx]
    if first_idx == 0:
        new_str = string[len(delimiter):]
    else:
        new_str = string.split(first_slice)[1][len(delimiter):]

    second_idx = new_str.find(delimiter)
    if second_idx < 0:
        raise Exception("no matching closing delimiter was found")
    delim_slice = new_str[:second_idx]

    remainder_slice = new_str[second_idx + len(delimiter):]

    return [first_slice, delim_slice, remainder_slice]