import sys


for line in sys.stdin:
    string_list = line.split()
    for item in string_list:
        # 处理逻辑
        if '.' in str(item):
            # 正向转换
            num_list = str(item).split('.')
            # 转2进制字符串并补全
            total_bin_num = ''
            for num in num_list:
                bin_num = bin(int(num))[2:]
                bin_num = '0' * (8 - len(bin_num)) + bin_num
                total_bin_num += bin_num
            print(int(total_bin_num, 2))
        else:
            # 反向转换
            bin_string = bin(int(item))[2:]
            bin_string = '0' * (32 - len(bin_string)) + bin_string
            int_string = ''
            for index in range(4):
                ele = bin_string[index * 8: (index + 1) * 8]
                int_string += f"{int(ele, 2)}."
            print(int_string[:-1])


