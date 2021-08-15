def to_number(string):
    try:
        return int(string)
    except ValueError:
        return float(string)