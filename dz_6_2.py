source = []
result = {}

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        ls = line.split()
        ip = ls[0]
        if ip not in result:
            result[ip] = 1
        else:
            result[ip] += 1
print(result)

n = 0
k = ''
for key, value in result.items():
    if value > n:
        n = value
        k = key
print(k, n)
