import math

item_1 = 25
item_2 = 20
result_sum = item_1 + item_2
print(result_sum)

result_subtr = item_1 - item_2
print(result_subtr)

result_multi = item_1 * item_2
print(result_multi)

result_exp = item_1**item_2
print(result_exp)

result_m_exp = pow(item_1, item_2)
print(result_m_exp)

result_s_root = item_1 ** (0.5)
print(result_s_root)

result_m_s_root = math.sqrt(item_1)
print(result_m_s_root)

result_mp_s_root = pow (item_2,(1/2))
print(result_mp_s_root)



numType = "even" if item_1 % 2 == 0 else "odd"
print(numType)

numType = "even" if item_2 % 2 == 0 else "odd"
print(numType)


result_division = item_1/item_2
print(result_division)

result_m_floor = round(result_division)
print(result_m_floor)

result_m_ceil = math.ceil(result_division)
print(result_m_ceil)

result_no_division_loss = item_1//item_2
print(result_no_division_loss)

result_division_loss = item_1 % item_2
print(result_division_loss)

item_3 = 20
item_3 +=10
print(item_3)

item_3 -= 5
print(item_3)

item_3 *= 3
print(item_3)

item_3 /= 2
print(item_3)

item_3 **= 2
print(item_3)

item_3 **= 0.5
print(item_3)

item_3 %= 2
print(item_3)

b_item_t = True
b_item_f = False
b_item_relult_sum = b_item_t + b_item_f
print(b_item_relult_sum)

b_item_relult_subtr =  b_item_t - b_item_f
print(b_item_relult_subtr)

b_item_relult_multi = b_item_t * b_item_f
print(b_item_relult_multi)


b_item_1_int = int (b_item_t)
print(type (b_item_1_int))

b_item_2_int = int (b_item_f)
print(type(b_item_2_int))

b_item_relult_division = b_item_t / b_item_f
print(b_item_relult_division)