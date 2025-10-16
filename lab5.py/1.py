import re

with open("/mnt/data/a.txt", "r", encoding="utf-8") as file:
    content = file.read()

pattern1 = r'ab*'
match1 = re.search(pattern1, content)
if match1:
    print("found! - ", match1.group())
else:
    print("no found")

pattern2 = r'ab{2,3}'
match2 = re.search(pattern2, content)
if match2:
    print("found! - ", match2.group())
else:
    print("no found")

pattern3 = r'[a-z]+(?:_[a-z]+)*'
matches3 = re.findall(pattern3, content)
if matches3:
    print("found! - ", matches3)
else:
    print("no found -")

pattern4 = r'[A-Z][a-z]+'
matches4 = re.findall(pattern4, content)
if matches4:
    print("foubd! - ", matches4)
else:
    print("no found")

pattern5 = r'a.*b'
matches5 = re.findall(pattern5, content)
if matches5:
    print("found! - ", matches5)
else:
    print("no found")

pattern6 = r'[ ,.]'
content_replaced = re.sub(pattern6, ":", content)
print("after replace - ", content_replaced)

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

snake_str = "example_snake_case_string"
camel_case = snake_to_camel(snake_str)
print("mutation - ", camel_case)

pattern8 = r'(?=[A-Z])'
split_at_caps = re.split(pattern8, content)
print("splitting - ", split_at_caps)

pattern9 = r'([a-z])([A-Z])'
content_with_spaces = re.sub(pattern9, r'\1 \2', content)
print("w/spaces - ", content_with_spaces)

def camel_to_snake(camel_str):
    result = re.sub('([a-z])([A-Z])', r'\1_\2', camel_str)
    return result.lower()

camel_str = "exampleCamelCaseString"
snake_case = camel_to_snake(camel_str)
print("mutation - ", snake_case)

