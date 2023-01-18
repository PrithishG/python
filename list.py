my_list = ["jan","feb","mar","apr","may","jun","jul","aug"]
# print (my_list[0])
my_list.append("sept")

print (set(my_list))
print(type(my_list))

if "jan" in my_list and "aug" in my_list:
    print("jan","sept")

for i in range(len(my_list)):
    if my_list[i] == 'jan' or my_list[i] == 'sept':
        print("output" + ":" + "jan", "sept")
    elif my_list[i] == 'nov':
        print("not found")
    else:
        print("error")


