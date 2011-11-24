import re
import string


def camel_to_snake(camel_case_input):
    """

    Converts a CamelCaseString to an underscore_separate_string

    :param camel_case_input: a CamelCaseString for conversion
    :returns: string, the underscore_delimited version of the input

    """

    # remove spaces:
    s1 = camel_case_input.replace(" ", "")

    # insert an underscore before any capital letter that's followed by a chain
    # of lowercase letters:
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s1)

    # insert an underscore *after* any lowercase letter that's immediately
    # followed by a capital letter:
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def snake_to_mixed(underscore_input):
    """
    mixedCaseLooksLikeThis
    """

    word_list = underscore_input.split('_')
    word_count = len( word_list )
    if word_count > 1:
        for i in range(1, word_count):
            word_list[i] = string.capwords( word_list[i] )
    ret = ''.join(word_list)
    return ret

def snake_to_camel(input_string):
    """
    CamelCaseLooksLikeThis
    """

    # replace spaces with underscores
    #input_string = input_string.replace(" ", "_")
    input_string = re.sub("\ +", "_", input_string)

    # insert an underscore before any capital letter that's followed by
    # a lowercase letter:
    input_string = re.sub('(.)([A-Z][a-z])', r'\1_\2', input_string)

    # strip special characters
    input_string = re.sub('[\W]+', '', input_string)

    # capitalize each word
    input_string = string.capwords(input_string, "_")
    word_list = input_string.split("_")

    input_string = ''.join(word_list)

    return input_string
