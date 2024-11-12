def ispunct(c):
    """
    ispunct check if the caracter c is in the list punctuation_marks
    and return c if true
    """
    punctuation_marks = '''!"#$%&'()*+,-./:;<=>?@[]\\^_`{|}~'''
    return c in punctuation_marks