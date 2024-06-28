import random
import re

# Set a seed for reproducibility
random.seed(42)

# Generate a random float in the range [0.0, 1.0)
random_float = random.random()
print(f"Random float: {random_float}")

# Generate a random float in the range [1.5, 2.5]
random_uniform = random.uniform(1.5, 2.5)
print(f"Random float between 1.5 and 2.5: {random_uniform}")

# Generate a random integer between 10 and 50
random_int = random.randint(10, 50)
print(f"Random integer between 10 and 50: {random_int}")

# Generate a random integer from range(0, 100) with step 5
random_range = random.randrange(0, 100, 5)
print(f"Random integer from range(0, 100) with step 5: {random_range}")

# Random choice from a list
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
random_choice = random.choice(fruits)
print(f"Random choice from list: {random_choice}")

# Random choices with replacement
random_choices = random.choices(fruits, k=3)
print(f"Random choices with replacement: {random_choices}")

# Random sample without replacement
random_sample = random.sample(fruits, k=3)
print(f"Random sample without replacement: {random_sample}")

# Shuffle a list
random.shuffle(fruits)
print(f"Shuffled list: {fruits}")

# Generate a random Gaussian distribution with mean 0 and standard deviation 1
random_gauss = random.gauss(0, 1)
print(f"Random Gaussian distribution with mean 0 and std 1: {random_gauss}")





# Sample text
text = "The rain in Spain falls mainly in the plain. Call me at 123-456-7890 or 987-654-3210."

# Find all phone numbers in the text
phone_numbers = re.findall(r'\d{3}-\d{3}-\d{4}', text)
print(f"Phone numbers found: {phone_numbers}")

# Substitute phone numbers with a placeholder
text_with_placeholders = re.sub(r'\d{3}-\d{3}-\d{4}', '[PHONE]', text)
print(f"Text with placeholders: {text_with_placeholders}")

# Split the text at each sentence
sentences = re.split(r'\.\s*', text)
print(f"Sentences: {sentences}")

# Extract all words starting with a capital letter
capital_words = re.findall(r'\b[A-Z][a-z]*\b', text)
print(f"Words starting with a capital letter: {capital_words}")

# Check if the text starts with 'The'
starts_with_the = bool(re.match(r'^The', text))
print(f"Text starts with 'The': {starts_with_the}")

# Extract the first word in each sentence
first_words = re.findall(r'\b\w+', text)
print(f"First words in each sentence: {first_words}")

# Compile a regular expression for repeated use
pattern = re.compile(r'\bin\b')
matches = pattern.findall(text)
print(f"Occurrences of 'in': {matches}")

# Find the position of the word 'Spain'
match = re.search(r'Spain', text)
if match:
    print(f"Found 'Spain' at position: {match.start()}")