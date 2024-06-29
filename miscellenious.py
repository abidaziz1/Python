from typing import Dict, Never
def get_users() -> Dict[int,str]:
    users: Dict[int,str] = {1:'Bob', 2:'Jef',3:'Tom'}
    return users
print(get_users())

def sum_numbers(*numbers: float)-> float:
    print(numbers)
    return sum(numbers)
print(sum_numbers(1,2,3,4,5,10,20))
#*numbers syntax allows the function to accept any number of float arguments.

def join_text(*strings: str, sep: str = ' ') -> str:
    print(strings)
    return sep.join(strings)
def main() -> None:
    print(join_text('A', 'B', 'C', 'D', sep='-'))
    print(join_text('A', sep='-'))
    print(join_text('A', 'B', 'C', 'D', 'Z', sep='/'))
if __name__ == '__main__':
    main()

def get_users() -> Dict[int, str]:
    users: Dict[int, str] = {1: 'Bob', 2: 'Jef', 3: 'Tom'}
    return users
def display_users(users: Dict[int, str]) -> None:
    for k, v in users.items():
        print(k, v, sep=': ')
def main() -> None:
    users: Dict[int,str] = get_users()
    display_users(users)
if __name__ == '__main__':
    main()


n: int = 1000000000
print(f'{n:_}')
print(f'{n:,}')


def dangerous_code() -> Never:
    raise ValueError('Bad value')
try:
    dangerous_code()
except ValueError as e:
    print(f'Yo, you messed up: "{e}"')



a: int = 10
b: int = 0
my_var: str = 'Bob says hi'
print(f'{bool(a)=}')
print(f'{bool(b)=}')
print(f'{bool(my_var)=}')


var: str = 'var'
print(f'{var:_>20}')
print(f'{var:#<20}')
print(f'{var:|^20}')
