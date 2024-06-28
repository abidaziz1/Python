import re
result = re.match(r'hello', 'hello world')
print(result)
result = re.search(r'world', 'hello world')
print(result)

result = re.findall(r'\d+', 'There are 2 apples and 5 oranges.')
print(result)

result = re.sub(r'apples', 'bananas', 'I like apples.')
print(result)

matches = re.finditer(r'\d+', 'There are 2 apples and 5 oranges.')
for match in matches:
    print(match.group())

result = re.split(r'\s+', 'Split this sentence into words.')
print(result)


pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
email = 'test@example.com'
if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")


text = "apple;orange,banana|grape"
pattern = r'[;|,]'
fruits = re.split(pattern, text)
print(fruits)


text = "Call me at 123-456-7890 or 987-654-3210."
pattern = r'\d{3}-\d{3}-\d{4}'
phone_numbers = re.findall(pattern, text)
print(phone_numbers)


text = "My phone number is 123-456-7890."
pattern = r'(\d{3})-(\d{3})-(\d{4})'
match = re.search(pattern, text)
if match:
    print("Full match:", match.group())
    print("Area code:", match.group(1))
    print("Phone number:", match.group(2), match.group(3))


