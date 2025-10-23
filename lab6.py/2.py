
import os

path = 'path'

print("just_directories:")
print([
    name for name in os.listdir(path)
    if os.path.isdir(os.path.join(path, name))
])

print("\njust_files:")
print([
    name for name in os.listdir(path)
    if not os.path.isdir(os.path.join(path, name))
])

print("\ndirectories :")
print([
    name for name in os.listdir(path)
])

import os
print('exist:', os.access('path', os.F_OK))
print('readable:', os.access('path', os.R_OK))
print('writable:', os.access('path', os.W_OK))
print('executable:', os.access('path', os.X_OK))

import os

p = input("path: ")

if os.path.exists(p):
    print("path there!")
    print("directory:", os.path.dirname(p))
    print("filename:", os.path.basename(p))
else:
    print("no path")

with open(r"random_path", 'r') as fp:
    for count, line in enumerate(fp):
        pass
print('in total', count + 1)

lines = ["alpha", "beta", "omega"] 
with open('random_file.txt', 'w') as f:
    for line in lines:
        f.write(f"{line}\n")

for i in range(0,26):
    alphabetLeter = chr(65+i)
    with open(f"{alphabetLeter}.txt", 'w') as fio:
        print(f"{alphabetLeter}.txt")


import shutil

a_path = 'random.txt'
b_path = 'random_dest.txt'
shutil.copy2(a_path, b_path)


import os

p = input("way to: ")

if os.path.exists(p):
    if os.access(p, os.R_OK) and os.access(p, os.W_OK):
        os.remove(p)
        print("everything_is_ok")
    else:
        print("okak")
else:
    print("cringe")