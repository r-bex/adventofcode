import re


def number_validator(min_val, max_val, string_val):
    try:
        n = int(string_val)
        return n >= min_val and n <= max_val
    except ValueError:
        return False


def regex_validator(pattern, string_val):
    p = re.compile(pattern)
    return bool(p.match(string_val))


def eye_colour_validator(string_val, allowed_colours):
    return string_val in allowed_colours


def height_validator(string_val, min_cm=150, max_cm=193, min_in=59, max_in=76):
    height_pattern = r"\d+(cm|in)"
    if regex_validator(height_pattern, string_val):
        if string_val[-2:] == "cm":
            return number_validator(min_cm, max_cm, string_val[:-2])
        else:
            return number_validator(min_in, max_in, string_val[:-2])
    else:
        return False