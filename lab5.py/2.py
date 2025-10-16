import re

txt = "yoy, sobaki, ya naruto uzumaki"
pattern1 = r'ab*'
match1 = re.search(pattern1, txt)
print(match1.group() if match1 else "No match")

txt = "rainer_sit_down"
pattern2 = r'ab{2,3}'
match2 = re.search(pattern2, txt)
print(match2.group() if match2 else "No match")

txt = "tanjiro_top"
pattern3 = r'[a-z]+(?:_[a-z]+)*'
matches3 = re.findall(pattern3, txt)
print(matches3)

txt = "toji apple moment"
pattern4 = r'[A-Z][a-z]+'
matches4 = re.findall(pattern4, txt)
print(matches4)

txt = "gojo satoru arrived at 20:31"
pattern5 = r'a.*b'
matches5 = re.findall(pattern5, txt)
print(matches5)

txt = "naruto therapy"
pattern6 = r'[ ,.]'
txt_replaced = re.sub(pattern6, ":", txt)
print(txt_replaced)

snake_str = "baka baka"
camel_case = ''.join(x.title() if i != 0 else x for i, x in enumerate(snake_str.split('_')))
print(camel_case)

txt = "gruzovik san"
pattern8 = r'(?=[A-Z])'
split_caps = re.split(pattern8, txt)
print(split_caps)

txt = "leave me alone"
pattern9 = r'([a-z])([A-Z])'
txt_with_spaces = re.sub(pattern9, r'\1 \2', txt)
print(txt_with_spaces)

camel_str = "muda muda muda"
snake_case = re.sub('([a-z])([A-Z])', r'\1_\2', camel_str).lower()
print(snake_case)
