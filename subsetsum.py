

#subset sum problem, nearest number to t
subset = []
do_list = []
subset_length = int(input("Length of subset list?"))

for i in range(subset_length):
    sss = int(input("item {} : ".format(i)))
    subset.append(sss)
    print(subset)
    
    for i in range (len(subset)):
        add_up = sss+subset[i]
        do_list.append(int(add_up))
        add_up = 0

t = int(input("sum ?"))
for i in range(len(do_list)):
    if do_list[i]>= t :
        index = i-1
    else:
        pass

print(do_list[index])