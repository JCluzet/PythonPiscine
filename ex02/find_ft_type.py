def all_thing_is_obj(object: any) -> int:
    # if its a list print List : <class 'list'>
    if isinstance(object, list):
        print("List : <class 'list'>")
    elif isinstance(object, tuple):
        print("Tuple : <class 'tuple'>")
    elif isinstance(object, set):
        print("Set : <class 'set'>")
    elif isinstance(object, dict):
        print("Dict : <class 'dict'>")
    elif isinstance(object, str):
        print(object + " is in the kitchen : <class 'str'>")
    else:
        print("Type not found")
    return 42