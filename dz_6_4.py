import sys

with open('users.csv', 'r', encoding='utf-8') as f1, open('hobbies.csv', 'r', encoding='utf-8') as f2, \
        open('users_hobbies.txt', 'w', encoding='utf-8') as f3:
    for line_f1 in f1:
        line_f2 = f2.readline().strip()
        if not line_f2:
            line_f2 = None
        f3.write(f'{line_f1.strip()}: {line_f2}\n')
    content = f2.read()
    if content:
        sys.exit(1)
