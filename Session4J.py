"""
    RegEx Module
        Regular Expressions

"""
import re

text = "Hey John. I am 18 years old now. I hope to see you at 3 on 12th december 2020"
pattern = '\d+'

result = re.findall(pattern, text)
print(result)

# result = re.split(pattern, text)
# result = re.split(pattern, text, 1)
result = re.split(pattern, text, 2)
print(result)

user_input = "hello this is" \
             "harry\nhope to see you soon"
pattern = '\s+'

replaced_string = re.sub(pattern, '-', user_input)
print(replaced_string)

text = "Hello, Thi is Awesome"
match = re.search('\AHello', text)
if match:
    print("Pattern Found")
else:
    print("Pattern Not Found")


data = 'John\r Coffee Shop\nRedwood Shores'
result = re.findall('[\r\n]', data)
print(result)

# validate this with regular expressions :)
email = "abc@example.com"

# list out all the words starting from vowels :)
text = "hello dear john, errors are a part of life and you must enjoy coding"
