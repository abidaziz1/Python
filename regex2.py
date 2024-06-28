import re

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$'
    if re.match(pattern, password):
        return True
    else:
        return False
passwords = ["Password123!", "password", "PASSWORD123", "Pass123", "Pass123!"]
results = [validate_password(pw) for pw in passwords]
print(results)

'''
Suppose we want to validate a password with the following criteria:
At least 8 characters long.
Contains both uppercase and lowercase letters.
Includes at least one numerical digit.
Contains at least one special character (e.g., @, #, $, %).
'''
#Extracting Dates from a Text
text = "John was born on 12/04/1995, and his sister on 15/07/1998."
pattern= r'\b\d{2}/\d{2}/\d{4}\b'
dates= re.findall(pattern,text)
print(dates)

#Parsing Log File Entries
log_entry = "Error [2024-06-19 10:45:32] - Something went wrong"
pattern = r'ERROR \[(.*?)\] - (.*)'
match= re.search(pattern, log_entry)
if match:
    timestamp = match.group(1)
    message = match.group(2)
    print(f"Timestamp: {timestamp}")
    print(f"Message: {message}")


#Finding URLs in a String
text = "Check out https://example.com and http://test.com for more information."
pattern = r'https?://[^\s]+'
urls = re.findall(pattern, text)
print(urls)


#Extracting Hashtags from a Tweet
tweet = "Loving the new features in #Python3! #coding #programming"
pattern = r'#\w+'
hashtags = re.findall(pattern, tweet)
print(hashtags)


#Splitting a Paragraph into Sentences
paragraph = "Hello world! How are you doing? I hope everything is fine. Have a great day."
pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s'
sentences = re.split(pattern, paragraph)
print(sentences)


#Matching HTML Tags
html = "<html><body><h1>Title</h1><p>This is a paragraph.</p></body></html>"
pattern = r'<[^>]+>'
tags = re.findall(pattern, html)
print(tags)


#Swapping First and Last Name
name = "Doe, John"
pattern = r'(\w+), (\w+)'
new_name = re.sub(pattern, r'\2 \1', name)
print(new_name)


#Removing Extra Whitespace
text = "This   is  a   sentence  with    irregular   spaces."
pattern = r'\s+'
cleaned_text = re.sub(pattern, ' ', text).strip()
print(cleaned_text)


#Finding Repeated Words
text = "This is is a test test string string."
pattern = r'\b(\w+)\s+\1\b'
repeated_words = re.findall(pattern, text)
print(repeated_words)


#Reformatting Dates
text = "Today's date is 19-06-2024."
pattern = r'(\d{2})-(\d{2})-(\d{4})'
new_text = re.sub(pattern, r'\3/\2/\1', text)
print(new_text)
