def all_thing_is_obj(obj: any) -> int:
    
    """
    Check if the given object is an instance of a class.
    Returns 42 if it is an object, otherwise returns 0.
    """
    if isinstance(obj, object) and not isinstance(obj, type):
        print(type(obj))
        return 42  # It is an object
    else:
        return 0  # It is not an object
    