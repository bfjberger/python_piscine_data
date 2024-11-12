
def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    '''bmi is you heigth to weigth ratio, (BMI) body mass index. formaula
    is : BMI = kg/m2'''

    # ensure both are lists
    if not isinstance(height, list) or not isinstance(weight, list):
        raise AssertionError("both arguments must be list")
    # check if the two lists is the same size:
    if len(height) != len(weight):
        raise AssertionError("both lists must be same size")
    for w, h in zip(weight, height):
        if not (isinstance(h, (float, int))):
            raise AssertionError("height must be only int or float")
        if not (isinstance(w, (float, int))):
            raise AssertionError("weight must be only int or float")
    res_list = [w / (h**2) for w, h in zip(weight, height)]
    return res_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    # return a list of if b is above the linit while b in bmi list,
    # else it is false
    return [b > limit for b in bmi]

# height = [2.71, 1.15, 1.91]
# weight = [165.3, 38.4, 92.4]
# bmi = give_bmi(height, weight)

# print(bmi, type(bmi))
