
import math
from decimal import Decimal
import numpy as np

# 标准差算法实现
def func_calculate_std(list_: list) -> Decimal:
    import math
    counter: int = 0
    grid: Decimal = Decimal(0)
    total_value: Decimal = Decimal(0)
    if len(list_) <= 1:
        std = Decimal(0)
    else:
        for value in list_:
            counter += 1
            value_lower = value - grid
            grid = grid + (value_lower / counter)
            total_value = total_value + (value_lower * (value - grid))
        std = math.sqrt(total_value / (counter - 1))
    return std

# 验证
res = func_calculate_std([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(res)

res_1 = np.std([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ddof=1)
print(res_1)


# 实现正态分布
def probability_density_function(x, std, average):
    parameter = 1 / (math.sqrt(2 * 3.1415926) * std)
    parameter_exp = math.exp(-((x - average) ** 2 / (2 * average ** 2)))
    return parameter * parameter_exp

# print(probability_density_function(5.208369439657385, 6.010407640085654, 29.25))
# print(probability_density_function(8.4139201810364, 6.010407640085654, 29.25))
# print(probability_density_function(10.016695551725906, 6.010407640085654, 29.25))
# print(probability_density_function(11.619470922415413, 6.010407640085654, 29.25))
# print(probability_density_function(13.22224629310492, 6.010407640085654, 29.25))
# print(probability_density_function(14.825021663794427, 6.010407640085654, 29.25))
# print(probability_density_function(16.427797034483934, 6.010407640085654, 29.25))
# print(probability_density_function(18.03057240517344, 6.010407640085654, 29.25))
# print(probability_density_function(19.633347775862948, 6.010407640085654, 29.25))
# print(probability_density_function(21.236123146552455, 6.010407640085654, 29.25))
# print(probability_density_function(22.83889851724196, 6.010407640085654, 29.25))
# print(probability_density_function(24.44167388793147, 6.010407640085654, 29.25))
# print(probability_density_function(, 6.010407640085654, 29.25))
# print(probability_density_function(, 6.010407640085654, 29.25))
# print(probability_density_function(, 6.010407640085654, 29.25))
# print(probability_density_function(, 6.010407640085654, 29.25))


# 26.044449258620975
# 27.647224629310482
# 29.24999999999999
# 30.852775370689496
# 32.45555074137901
# 34.058326112068514
# 35.66110148275802
# 37.26387685344753
# 38.866652224137034
# 40.46942759482654
# 42.07220296551605
# 43.674978336205555
# 45.27775370689506
# 46.88052907758457
# 48.483304448274076
# 50.08607981896358
# 51.68885518965309
# 53.2916305603426

# x = 5.208369439657385
# while x <= 53.2916305603426:
#     print(probability_density_function(x, 6.010407640085654, 29.25))
#     x += 1.6027753706895074