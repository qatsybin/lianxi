# 列表
# list_lianxi = [1, 2, 3, 5, 4, 6, 8, 7, 9, 0]
# list_lianxi.append(0)
# list_lianxi.insert(2, 9)
# list_lianxi.remove(9)
# list_lianxi.pop(9)
# list_lianxi.sort()
# # 降序排序
# list_lianxi.sort(reverse=True)
# list_lianxi.reverse()
# print(list_lianxi)
# list_pingfang=[]
# for i in range(4):
#     list_pingfang.append(i**2)
# print(list_pingfang)
# list_pingfang2 = [j ** 2 for j in range(1, 4)]
# print("list_pingfang", list_pingfang2)
# list_pingfang3 = [i ** 2 for i in range(1, 4)]
# print(list_pingfang3)
# 元组

# 元组不可变特性   不可替换, 元组中嵌套列表可以改变
# tuple_a = (1, 2, 3, 1)
# # print(tuple_a.count(1))
# print(tuple_a.index(3))   #索引使用

# 集合
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6, 6, 7}
# print(a.union(b))
# print(a.intersection(b))
# print(set(b))  # 去重

# 字典
# dict_zidian = {}
# dict_zidian2 = dict(a=1, b=2)
# print(dict_zidian)
# print(type(dict_zidian))
# print(dict_zidian2)
# print(type(dict_zidian2))


# a = {"a": 1, "b": 2, "c": 3}
# print(a.keys())
# print(a.values())
# print(a.pop("a"))
# print(a)
# a = {}
# b = a.fromkeys([1, 2, 3], "a")    # 赋值
# print(b)

print({i: i * 2 for i in range(1, 4)})  # 字典推导式
