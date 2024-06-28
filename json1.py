import json  

print(json.dumps({"name": "John", "age": 36}))
# First example, python to json string. json.dumps() to convert a Python dictionary to a JSON string.
x= {
    "name": "json",
    "age": 36,
    "address": {
        "city": "Dhaka",
        "country": "Bangladesh"
    },
    "married": True,
    "children": False,
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
    
}
print(json.dumps(x, indent=4, separators=(",", ": "),sort_keys=True))

#json to python

json_string = '{"name": "John", "age": 36}'
python_dict = json.loads(json_string)
print(python_dict)  # Output: {'name': 'John', 'age': 36}

"""
JSON is a lightweight, human-readable data interchange format. It's used to exchange data between web servers, web applications, and mobile apps.
JSON is language-independent, meaning it can be used with many programming languages, including Python, JavaScript, Java, and more.
"""
