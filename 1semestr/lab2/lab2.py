import math


#
# for x in range(150, 350, 5):
#     x = x * 0.01
#     if x < 2.2:
#         print(math.log10(math.log(x) + math.log2(x)))
#     elif x < 3:
#         sin = math.sin(x)
#         cos = math.cos(x)
#         print((cos ** 2 + cos / sin) ** (1 / 4))
#     else:
#         print(math.atan(1 / x))


# interval [1.1, 3.5]
# step 0.1
# error 0.001


def get_number(k, x):
    return (-1) ** (k + 1) * math.cos(k * x) / (x + 2 * k) ** 3


addition = 0
for x in range(11, 35, 1):
    k = 1
    x = x * 0.1
    while True:
        if get_number(k, x) > 0.0001:
            break
        addition = + get_number(k, x)
        k = k + 1
    print(f"sum is: {addition}, x = {x}")
    addition = 0