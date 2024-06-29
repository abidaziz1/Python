import logging
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO)

def get_users() -> Dict[int, str]:
    users: Dict[int, str] = {1: 'Bob', 2: 'Jef', 3: 'Tom'}
    logging.info(f"Users fetched: {users}")
    return users

def display_users(users: Dict[int, str]) -> None:
    for k, v in users.items():
        logging.info(f"User ID: {k}, Name: {v}")

def sum_numbers(*numbers: float) -> float:
    logging.info(f"Numbers received for summing: {numbers}")
    result = sum(numbers)
    logging.info(f"Sum result: {result}")
    return result

def join_text(*strings: str, sep: str = ' ') -> str:
    logging.info(f"Strings to join: {strings} with separator '{sep}'")
    result = sep.join(strings)
    logging.info(f"Joined text: {result}")
    return result

def example_kwargs(*, param1: int, param2: str) -> str:
    return f"param1: {param1}, param2: {param2}"

def example_args(*args: int) -> int:
    return sum(args)

def main() -> None:
    users: Dict[int, str] = get_users()
    display_users(users)

    print(sum_numbers(1, 2, 3, 4, 5, 10, 20))
    
    print(join_text('A', 'B', 'C', 'D', sep='-'))
    print(join_text('A', sep='-'))
    print(join_text('A', 'B', 'C', 'D', 'Z', sep='/'))

    print(example_kwargs(param1=1, param2="example"))
    print(example_args(1, 2, 3, 4))

if __name__ == '__main__':
    main()



