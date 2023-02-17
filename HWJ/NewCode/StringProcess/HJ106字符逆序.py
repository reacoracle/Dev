input_string = input()

# res = ''
# for i in range(len(input_string)):
#     res += input_string[len(input_string) - i -1]
# print(res)

res = ''.join(input_string[len(input_string) - i - 1] for i in range(len(input_string)))
print(res)
