'''
Write a program to check given string is Palindrome or not.
That is reverse the given string and check whether it is same as original string, if so then it is palindrome.
'''

#x = input("Enter the word")
x= "malayalam"
len_w = len(x) -1
y = len_w//2
print(y)
list_w = list(x)
print(list_w,len_w)
for k in range (0,y):
    print("k and len_w",k,len_w)
    print("starting value", list_w[k])
    print("Ending Value ", list_w[len_w])
    print("******\n")
    if list_w[k]==list_w[len_w]:
        print("pallindrome")
    else:
        print("SORRY")
        break
    len_w = len_w-1
