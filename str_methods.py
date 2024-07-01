def demonstrate_string_methods():
    s = "hello"
    print(f"Original string: {s}")

    # capitalize
    print(f"capitalize(): {s.capitalize()}")  # Output: "Hello"

    # casefold
    print(f"casefold(): {s.casefold()}")  # Output: "hello"

    # center
    print(f"center(10, '-'): {s.center(10, '-')}")  # Output: "--hello---"

    # count
    s2 = "hello world"
    print(f"count('o'): {s2.count('o')}")  # Output: 2

    # encode
    print(f"encode(): {s.encode()}")  # Output: b'hello'

    # endswith
    print(f"endswith('lo'): {s.endswith('lo')}")  # Output: True

    # expandtabs
    s3 = "hello\tworld"
    print(f"expandtabs(4): {s3.expandtabs(4)}")  # Output: "hello   world"

    # find
    print(f"find('o'): {s2.find('o')}")  # Output: 4

    # format
    s4 = "Hello, {}!"
    print(f"format('world'): {s4.format('world')}")  # Output: "Hello, world!"

    # format_map
    s5 = "Hello, {name}!"
    print(f"format_map({{'name': 'world'}}): {s5.format_map({'name': 'world'})}")  # Output: "Hello, world!"

    # index
    print(f"index('o'): {s2.index('o')}")  # Output: 4

    # isalnum
    s6 = "hello123"
    print(f"isalnum(): {s6.isalnum()}")  # Output: True

    # isalpha
    print(f"isalpha(): {s.isalpha()}")  # Output: True

    # isascii
    print(f"isascii(): {s.isascii()}")  # Output: True

    # isdecimal
    s7 = "12345"
    print(f"isdecimal(): {s7.isdecimal()}")  # Output: True

    # isdigit
    print(f"isdigit(): {s7.isdigit()}")  # Output: True

    # isnumeric
    print(f"isnumeric(): {s7.isnumeric()}")  # Output: True

    # isidentifier
    print(f"isidentifier(): {s.isidentifier()}")  # Output: False

    # islower
    print(f"islower(): {s.islower()}")  # Output: True

    # isprintable
    print(f"isprintable(): {s.isprintable()}")  # Output: True

    # isspace
    s8 = "   "
    print(f"isspace(): {s8.isspace()}")  # Output: True

    # istitle
    s9 = "Hello World"
    print(f"istitle(): {s9.istitle()}")  # Output: True

    # isupper
    s10 = "HELLO"
    print(f"isupper(): {s10.isupper()}")  # Output: True

    # join
    s11 = "-"
    print(f"join(['hello', 'world']): {s11.join(['hello', 'world'])}")  # Output: "hello-world"

    # ljust
    print(f"ljust(10, '-'): {s.ljust(10, '-')}")  # Output: "hello-----"

    # lower
    s12 = "HELLO"
    print(f"lower(): {s12.lower()}")  # Output: "hello"

    # lstrip
    s13 = "   hello"
    print(f"lstrip(): {s13.lstrip()}")  # Output: "hello"

    # maketrans / translate
    trans = str.maketrans('h', 'j')
    print(f"translate(maketrans('h', 'j')): {s.translate(trans)}")  # Output: "jello"

    # partition
    print(f"partition(' '): {s2.partition(' ')}")  # Output: ('hello', ' ', 'world')

    # removeprefix
    s14 = "hello world"
    print(f"removeprefix('hello'): {s14.removeprefix('hello')}")  # Output: " world"

    # removesuffix
    print(f"removesuffix('world'): {s14.removesuffix('world')}")  # Output: "hello "

    # replace
    print(f"replace('world', 'there'): {s14.replace('world', 'there')}")  # Output: "hello there"

    # rfind
    print(f"rfind('o'): {s2.rfind('o')}")  # Output: 7

    # rindex
    print(f"rindex('o'): {s2.rindex('o')}")  # Output: 7

    # rjust
    print(f"rjust(10, '-'): {s.rjust(10, '-')}")  # Output: "-----hello"

    # rpartition
    s15 = "hello world hello"
    print(f"rpartition(' '): {s15.rpartition(' ')}")  # Output: ('hello world', ' ', 'hello')

    # rsplit
    print(f"rsplit(' ', 1): {s15.rsplit(' ', 1)}")  # Output: ['hello world', 'hello']

    # rstrip
    s16 = "hello   "
    print(f"rstrip(): {s16.rstrip()}")  # Output: "hello"

    # split
    print(f"split(): {s2.split()}")  # Output: ['hello', 'world']

    # splitlines
    s17 = "hello\nworld"
    print(f"splitlines(): {s17.splitlines()}")  # Output: ['hello', 'world']

    # startswith
    print(f"startswith('he'): {s.startswith('he')}")  # Output: True

    # strip
    s18 = "   hello   "
    print(f"strip(): {s18.strip()}")  # Output: "hello"

    # swapcase
    s19 = "Hello"
    print(f"swapcase(): {s19.swapcase()}")  # Output: "hELLO"

    # title
    print(f"title(): {s2.title()}")  # Output: "Hello World"

    # upper
    print(f"upper(): {s.upper()}")  # Output: "HELLO"

    # zfill
    s20 = "42"
    print(f"zfill(5): {s20.zfill(5)}")  # Output: "00042"

if __name__ == "__main__":
    demonstrate_string_methods()
