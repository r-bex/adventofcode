import sys
sys.path.append("..")
from utils.utils import load_input, chunk_lines_by_blanks

from functools import reduce

from validators import number_validator, regex_validator, height_validator, eye_colour_validator


class Passport:
    EXPECTED_FIELDS = {
        'byr':
        lambda s: number_validator(1920, 2002, s),
        'iyr':
        lambda s: number_validator(2010, 2020, s),
        'eyr':
        lambda s: number_validator(2020, 2030, s),
        'ecl':
        lambda s: eye_colour_validator(
            s, ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']),
        'hcl':
        lambda s: regex_validator(r"^#[a-f0-9]{6,9}$", s),
        'pid':
        lambda s: regex_validator(r"^\d{9}$", s),
        'hgt':
        lambda s: height_validator(s)
    }

    def __init__(self, supplied_fields):
        self.supplied_fields = supplied_fields

    def is_valid(self):
        # check all required fields are present
        all_fields_present = all([
            field in self.supplied_fields.keys()
            for field in self.EXPECTED_FIELDS.keys()
        ])

        if not all_fields_present:
            return False
        else:
            # check all fields pass validation
            all_fields_valid = all([
                validation_func(self.supplied_fields[field_name]) for
                field_name, validation_func in self.EXPECTED_FIELDS.items()
            ])
            return all_fields_valid

    @classmethod
    def from_lines(cls, lines):
        # parse fields from lines
        kv_pairs = reduce(lambda l, r: l + r, [l.split(" ") for l in lines])
        fields = {kv.split(":")[0]: kv.split(":")[1] for kv in kv_pairs}
        return cls(fields)


def count_valid_passports(lines):
    line_groups = chunk_lines_by_blanks(lines)
    passports = [Passport.from_lines(line_group) for line_group in line_groups]
    valid_passports = list(filter(lambda p: p.is_valid(), passports))
    return len(valid_passports)


if __name__ == "__main__":
    # run test against provided example
    example_input = load_input(path="example.txt", remove_empty_lines=False)
    assert count_valid_passports(example_input) == 4

    # run against real data
    values = load_input(remove_empty_lines=False)
    num_valid_passports = count_valid_passports(values)
    print("num valid: {}".format(num_valid_passports))
