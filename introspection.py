"""
useful functions for introspection
"""

from .list_utils import dedupe_list


def extract_classes(clazz):
    """

    Find all parent classes, anywhere in the inheritance tree.

    :param clazz: class, the thing to crawl through 
    
    Returns a list of all base classes in the inheritance tree

    """

    extracted = [clazz]

    for base in clazz.__bases__:
        extracted += extract_classes(base)

    # no need to include 'object'
    if object in extracted:
        extracted.remove(object)

    return dedupe_list(extracted, preserve_order=True)


