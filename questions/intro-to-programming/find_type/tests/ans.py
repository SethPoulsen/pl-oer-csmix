def find_type(a):
    try:
        len(a)
        return "str"
    except:
        return "int"
    