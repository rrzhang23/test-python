func_dict = {}
with open("函数日志") as lines:
    for line in lines:
        str = line.replace('\n', '')
        if str in func_dict.keys():
            func_dict[str] = func_dict[str] + 1
        else:
            func_dict[str] = 1

print(func_dict)

func_list = sorted(func_dict.items(), key=(lambda x: x[1]), reverse=False)
print(func_list)
for i in func_list:
    print(i[0], i[1])
