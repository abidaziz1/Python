def handle_status_code(status_code):
    match status_code:
        case 200:
            print("OK")
        case 404:
            print("Not Found")
        case 500:
            print("Server Error")
        case _:
            print("Unknown Error")
            
# Example usage
print(handle_status_code(200))  ## Output: OK
print(handle_status_code(404))# Output: Not Found
print(handle_status_code(123))# Output: Unknown Status Code


def describe_value(value):
    match value:
        case int():
            return f"Integer: {value}"
        case str():
            return f"String: {value}"
        case float():
            return f"Float: {value}"
        case list() if all(isinstance(item, int) for item in value):
            return f"List of integers: {value}"
        case _:
            return f"Unknown type: {type(value)}"
print(describe_value(42))           # Output: Integer: 42
print(describe_value("hello"))      # Output: String: hello
print(describe_value([1, 2, 3]))    # Output: List of integers: [1, 2, 3]
print(describe_value([1, "a", 3]))  # Output: Unknown type

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def describe_point(point):
    match point:
        case Point(x, y):
            return f"Point with x={x}, y={y}"
        case _:
            return "Not a point"

p = Point(3, 4)
print(describe_point(p))  # Output: Point with x=3, y=4



def process_data(data):
    match data:
        case {"type": "point", "x": x, "y": y}:
            return f"Point at ({x}, {y})"
        case {"type": "circle", "radius": r}:
            return f"Circle with radius {r}"
        case _:
            return "Unknown shape"

print(process_data({"type": "point", "x": 1, "y": 2}))  # Output: Point at (1, 2)
print(process_data({"type": "circle", "radius": 5}))   # Output: Circle with radius 5
