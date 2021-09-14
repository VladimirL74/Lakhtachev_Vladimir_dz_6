import requests

result = []
response = requests.get("https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs")
content = response.content.decode(encoding=response.encoding)
with open('nginx_logs.txt', 'w', encoding='utf-8') as f:
    f.write(content)
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    for line in f:
        ln = line.split()
        result.append((ln[0], ln[5].strip('"'), ln[6]))
print(*result, sep='\n')
