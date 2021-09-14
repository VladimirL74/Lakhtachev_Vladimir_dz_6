import sys
import json

result = {}
with open('users.csv', 'r', encoding='utf-8') as f1, open('hobbies.csv', 'r', encoding='utf-8') as f2:
    for line_f1 in f1:
        line_f2 = f2.readline().strip()
        if not line_f2:
            line_f2 = None
        if line_f1 not in result:
            result[line_f1.strip()] = line_f2
    content = f2.read()
    if content:
        sys.exit(1)

with open('result.json', 'w', encoding='utf-8') as result_file:
    result_str = json.dumps(result, ensure_ascii=False)
    result_file.write(result_str)
with open('result.json', 'r', encoding='utf-8') as f:
    content = f.read()
    res = json.loads(content)
print(res)
