def add(val):
    if isinstance(val, str):
        return  val + " + 1"
    elif isinstance(val, int):
        return val + 1
    elif isinstance(val, float):
        return val + 1.0
    else:
        return 42
