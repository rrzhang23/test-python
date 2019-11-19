file_dict = {}
with open("my_sys_file") as lines:
# with open("os0file_file") as lines:
    for line in lines:
        str = line.replace('\n', '')
        if str in file_dict.keys():
            file_dict[str] = file_dict[str] + 1
        else:
            file_dict[str] = 1

print(file_dict)

file_list = sorted(file_dict.items(), key=(lambda x: x[0]), reverse=False)
print(file_list)
for i in file_list:
    print(i[0])
