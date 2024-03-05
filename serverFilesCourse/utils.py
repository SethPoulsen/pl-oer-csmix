# TODO: find where this is used and replace it with repr_X_pl
def get_2d_array_repr_for_pl(arr, prefix="np."):
    code = prefix + arr.__repr__()
    spaces = code.find("[", code.find("[") + 1)
    code = code.replace("       ", " " * spaces)
    code = code.replace("nan", "np.nan")
    return code


def repr_X_pl(X):
    X = repr(X)
    spaces = X.find("[", X.find("[") + 1)
    X = X.replace("       ", "       " + " " * spaces)
    X = X.replace("nan", "np.nan")
    return "X = np." + X


def repr_x_pl(x, name="x"):
    x = repr(x)
    x = "".join(x.split())
    x = x.replace(",", ", ")
    return name + " = np." + x


def repr_y_pl(y):
    y = repr(y)
    y = "".join(y.split())
    y = y.replace(",", ", ")
    return "y = np." + y


def grade(data):
    data["feedback"]["show_full_answer"] = False
    if data["score"] == 1:
        data["feedback"]["show_full_answer"] = True
