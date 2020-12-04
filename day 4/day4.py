import dataclasses
import re
import typing


@dataclasses.dataclass
class Passport:
    byr: int
    iyr: int
    eyr: int
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: str = ""

    def valid_byr(self) -> bool:
        return 1920 <= int(self.byr) <= 2002

    def valid_iyr(self) -> bool:
        return 2010 <= int(self.iyr) <= 2020

    def valid_eyr(self) -> bool:
        return 2020 <= int(self.eyr) <= 2030

    def valid_hgt(self) -> bool:
        if self.hgt.endswith("in"):
            return 59 <= int(self.hgt.strip("in")) <= 76
        elif self.hgt.endswith("cm"):
            return 150 <= int(self.hgt.strip("cm")) <= 193
        else:
            return False

    def valid_hcl(self) -> bool:
        return bool(re.compile(r"^#[0-9a-f]{6}$").match(self.hcl))

    def valid_ecl(self) -> bool:
        return self.ecl in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    def valid_pid(self) -> bool:
        return bool(re.compile(r'^[0-9]{9}$').match(self.pid))

    def valid(self) -> bool:
        return self.valid_byr() and self.valid_iyr() and self.valid_eyr() and self.valid_hgt() and self.valid_hcl() and self.valid_ecl() and self.valid_pid()


def make_passport(**kwargs) -> typing.Optional[Passport]:
    try:
        response = Passport(**kwargs)
    except:
        return None
    return response


def read_input() -> typing.List[Passport]:
    entries = list()
    accumulator = {}
    with open("input.txt") as filehandle:
        for line in filehandle:
            line = line.strip()
            if not line:
                p = make_passport(**accumulator)
                if p:
                    entries.append(p)
                accumulator = {}
            values = line.split()
            for value in values:
                key, val = value.split(":")
                key = key.strip()
                val = val.strip()
                accumulator[key] = val
    if accumulator:
        p = make_passport(**accumulator)
        if p:
            entries.append(p)
    return entries


passports = read_input()

# part 1, answer: 226
print(len(passports))

# part 2, answer: 160
print(sum(1 for passport in passports if passport.valid()))
