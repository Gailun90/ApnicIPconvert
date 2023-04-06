import requests
import re


# 下载APNIC的IP地址分配文件
url = 'http://ftp.apnic.net/apnic/stats/apnic/delegated-apnic-latest'
response = requests.get(url)
content = response.text
pattern = r'apnic\|CN\|ipv4\|(\d+\.\d+\.\d+\.\d+)\|(\d+)\|.*\|a.*'
matches = re.findall(pattern, content)
formatted_ips = [f'{ip}/{mask}' for ip, mask in matches]
with open('ip.txt', 'w') as f:
    for ip in formatted_ips:
        f.write(ip + '\n')
