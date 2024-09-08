from math import isnan
def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: None <class 'NoneType'>")
    elif isinstance(object, float) and isnan(object):
        print("Cheese: nan <class 'float'>")
    elif isinstance(object, int) and object == 0 and object is not False:
        print("Zero: 0 <class 'int'>")
    elif object == '':
        print("Empty:  <class 'str'>")
    elif isinstance(object, bool) and object == False:
        print("Fake: False <class 'bool'>")
    else:
        print("Type not found")
        return 1
    return 0