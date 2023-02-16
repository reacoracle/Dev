import sys

for line in sys.stdin:
    input_lst = line.split()
    for password in input_lst:
        # pass indi
        is_digit, is_lower, is_upper, is_other = False, False, False, False
        for ele in password:
            if ele.isdigit():
                is_digit = True
            elif ele.islower():
                is_lower = True
            elif ele.isupper():
                is_upper = True
            else:
                is_other = True
        type_flag = is_digit + is_lower + is_upper + is_other
        # duplicate sub str
        duplicate_flag = False
        for i in range(len(password) - 3):
            if password.count(password[i: i + 3]) > 1:
                duplicate_flag = True
        if len(password) > 8 and type_flag >=3 and not duplicate_flag:
            print('OK')
        else:
            print('NG')

# import sys
# import contextlib
#
# with contextlib.suppress(Exception):
#     while True:
#         line = sys.stdin.readline().strip()
#         # if line == '':
#         #     break
#         lines = line.split()
#         print(lines)
