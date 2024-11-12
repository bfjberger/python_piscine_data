from sys import argv

def take_arg():
    if len(argv) == 1 :
        return(0)
    if len(argv) > 1 and len(argv) < 3 :
        num = argv[1]
        try:
            num = int(num)
            if num % 2 == 0:
                print("I'm Even.")
            else:
                print("I'm Odd.")
        except:
            print("AssertionError: argument is not an integer")
    else:
        print("AssertionError: more than one argument is provided")
    
take_arg()