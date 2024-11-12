def NULL_not_found(object: any) -> int:
    # check if the object is null, and returns 0 if right
    # else return 1
    if object is None :
        print(type(object))
        return(0)
    else:
        print(type(object))
        return(1)
