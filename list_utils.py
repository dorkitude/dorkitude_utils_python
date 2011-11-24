def dedupe_list(input_list, preserve_order=True):
    """

    Remove duplicates from the list, preserving order.

    :param input_list: list, the thing we need to dedupe
    :returns: list, a new copy of the input_list without duplicates

    """
    seen = set()
    return [ x for x in input_list if x not in seen and not seen.add(x)]
