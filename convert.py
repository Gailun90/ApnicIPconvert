import ipaddress

# 打开ip.txt文件和output.txt文件
with open('ip.txt', 'r') as f, open('output.txt', 'w') as fout:
    for line in f:
        line = line.strip()  # 删除行末的换行符
        items = line.split('/')  # 对每行进行分割
        ip_address = items[0]  # 取第一个元素作为IPv4地址
        ip_count = 2 - int(items[1])  # 取第二个元素并转换为整数作为IP个数
        subnet_mask = 32 - ip_count.bit_length()  # 计算子网掩码的值
        ip_address = ipaddress.IPv4Address(ip_address)  # 将IPv4地址转换为IPv4Address对象
        ip_network = ipaddress.IPv4Network((ip_address, subnet_mask))  # 将IPv4地址和子网掩码转换为IPv4Network对象
        cidr_notation = str(ip_network.with_prefixlen)  # 将IPv4Network对象转换为CIDR表示法
        fout.write(cidr_notation + '\n')  # 将CIDR表示法写入output.txt文件
