'''
Write a program to Sort given N numbers (Use only loop structures and Conditions to sort the elements.
Use Bubble sort / Selection sort technique to sort the elements of List) Note: Don't use built in functions to sort.
'''
num = input("Enter the length of the list")
list_num=[]
for i in range (0,int(num)):
    x = input("Enter the number of the list")
    list_num.append(int(x))
print("LIST OF THE NUMBERS",list_num)

for i in range (0,int(num)-1):
    if list_num[i] > list_num[i+1]:
        a = list_num[i+1]
        list_num[i + 1]=list_num[i]
        list_num[i]=a
print("list bubble sort",list_num)




