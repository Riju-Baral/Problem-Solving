# def reverse(str):
#     str=str[::-1]
#     return str
# s="Hello World"
# print(reverse(s))

# def reverse(str):
#     str=""
#     for i in str:
#         str = i+str
#     return str
# s="Hello World"
# print(reverse(s))

def reverse (string):
    reverse_string=""
    count = len(string)
    while count > 0:   
        reverse_string+= string[count-1] 
        count = count - 1 
    return reverse_string
s="Hello World"
print(reverse(s))
