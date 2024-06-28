from typing import NoReturn
def stop_execution() -> NoReturn:
    raise SystemExit("Stopping the program")

try:
    stop_execution()
except SystemExit as e:
    print(e)

# Output: Stopping the program
"""
Here, stop_execution is annotated with NoReturn, 
indicating it will never return a value and will instead raise a SystemExit exception to terminate the program.
"""
