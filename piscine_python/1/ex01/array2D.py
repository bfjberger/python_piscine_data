from numpy import shape


def slice_me(family: list, start: int, end: int) -> list:  # your code here
    """"slice_me function slices a 2D list and returns a new 2D list"""
    # using shape attribute of numpy to print list shape
    print(f"My shape is :{shape(family)}")
    # slicing the list in irder of start and end
    if start != 0:
        family = family[start:]
    if end != 0:
        family = family[:end]
    print(f"My new shape is :{shape(family)}")
    return family


# test my buildong code:

# test_list = [[1.80, 78.4],
#             [2.15, 102.7],
#             [2.10, 98.5],
#             [1.88, 75.2]]
# slice_me(test_list, 0, 2)
