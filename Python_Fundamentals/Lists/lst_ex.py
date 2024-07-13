# Write your code here.

# You'll have to use the following strings:
# 1) "Enter a string: "
# 2) "Enter a number: "
str_list = []
index_lst =[]
for i in range(5):
    str_list.append(input("Enter a string: "))
for i in range(3):
    index_lst.append(input("Enter a number: "))
print(str_list[int(float(index_lst[0]))] + str_list[int(float(index_lst[1]))] + str_list[int(float(index_lst[2]))])
