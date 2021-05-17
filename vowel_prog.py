'''
Write a program to check how many ovals present in the given string.
That is, count the number of " a e i o u" in the given string and print the numbers against each
'''
word= "This is Python"
list_w=list(word)
count =0
vowels=['a','e','i','o','u']
for i in list_w:
    if i in vowels:
        print("Vowels is value", i)
        count = count+1

print("count is ", count)